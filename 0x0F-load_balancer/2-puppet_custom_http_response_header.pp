# init.pp

class nginx_setup {
  package { 'nginx':
    ensure  => 'installed',
    before  => Service['nginx'],
  }

  service { 'nginx':
    ensure    => 'running',
    enable    => true,
    require   => Package['nginx'],
  }

  file { '/var/www':
    ensure => 'directory',
    mode   => '0755',
  }

  exec { 'chmod_www_directory':
    command => 'chmod -R 755 /var/www',
    path    => '/bin:/usr/bin',
    require => File['/var/www'],
  }

  class { 'ufw':
    before => Class['nginx_setup'],
  }

  ufw::allow { 'Nginx HTTP':
    before => Service['nginx'],
  }

  file { '/var/www/html/index.nginx-debian.html':
    ensure  => 'file',
    content => 'Hello World!',
    require => Package['nginx'],
  }

  file { '/var/www/html/custom_404.html':
    ensure  => 'file',
    content => 'Ceci n\'est pas une page',
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => 'file',
    content => template('nginx/default.erb'),
    notify  => Service['nginx'],
  }
}

class { 'nginx_setup': }


server {
    listen 80 default_server;
    listen [::]:80 default_server;
    
    add_header X-Served-By $hostname;
    
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
