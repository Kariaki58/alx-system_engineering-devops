# Define class for Nginx installation and configuration
class nginx_config {

  package { 'nginx':
    ensure => installed,
  }

  exec { 'echo tee index.nginx-debian.html':
    command => "/usr/bin/echo 'Hello World!' | sudo /usr/bin/tee /var/www/html/index.nginx-debian.html"
  }
  
  exec { "404 not found page":
    command => "/usr/bin/echo 'Ceci n\'est pas une page' | sudo /usr/bin/tee /var/www/html/custom_404.html"
  }
  
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => "
      server {
          listen 80 default_server;
          listen [::]:80 default_server;
          
          add_header X-Served-By $hostname;
	  
          root /var/www/html;
          index index.html index.htm index.nginx-debian.html;

          server_name _;
          
          location / {
              try_files \$uri \$uri/ =404;
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
