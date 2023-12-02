# Define class for Nginx installation and configuration
class nginx_config {

  package { 'nginx':
    ensure => installed,
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => "
      server {
          listen 80 default_server;
          listen [::]:80 default_server;

          root /var/www/html;
          index index.html index.htm index.nginx-debian.html;

          server_name _;

          location /redirect_me {
              return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
          }

          location / {
              try_files \$uri \$uri/ =404;
          }
      }
    ",
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
  }
}
include nginx_config
