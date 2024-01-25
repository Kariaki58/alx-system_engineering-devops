# nginx_setup.pp

class nginx_setup {

  # Update package lists
  package { 'update_packages':
    name   => 'apt',
    ensure => latest,
  }

  # Upgrade packages
  package { 'upgrade_packages':
    name   => 'apt',
    ensure => latest,
  }

  # Install nginx
  package { 'nginx':
    ensure => installed,
  }

  # Start nginx service
  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
  }

  # Set permissions on /var/www
  file { '/var/www':
    ensure  => directory,
    owner   => 'root',
    group   => 'root',
    mode    => '0755',
    recurse => true,
  }

  # Allow Nginx HTTP traffic
  exec { 'allow_nginx_http':
    command => 'ufw allow "Nginx HTTP"',
    path    => '/bin:/usr/bin',
    unless  => 'ufw status | grep "Nginx HTTP"',
    require => Package['ufw'],
  }

  # Create Nginx configuration file
  file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => @("EOF"),
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    add_header X-Served-By $HOSTNAME;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files $uri $uri/ =404;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /custom_404.html;
    location = /custom_404.html {
        root /var/www/html;
        internal;
    }
}
EOF
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  # Create Hello World and custom 404 pages
  file { '/var/www/html/index.nginx-debian.html':
    ensure  => present,
    content => 'Hello World!',
  }

  file { '/var/www/html/custom_404.html':
    ensure  => present,
    content => 'Ceci n\'est pas une page',
  }

}

# Include the class to apply the configuration
include nginx_setup

