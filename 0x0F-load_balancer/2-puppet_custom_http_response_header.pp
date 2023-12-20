# Define a class for Nginx installation and configuration
class nginx_example {

  # Update the package lists
  package { 'update-package-list':
    ensure  => latest,
    name    => 'update',
    command => '/usr/bin/apt-get',
    require => Class['nginx_example::install_nginx'],
  }

  # Upgrade installed packages
  package { 'upgrade-packages':
    ensure  => latest,
    name    => 'upgrade',
    command => '/usr/bin/apt-get',
    require => Class['nginx_example::install_nginx'],
  }

  # Install Nginx
  class { 'nginx_example::install_nginx': }

  # Set permissions on /var/www
  file { '/var/www':
    ensure => directory,
    owner  => 'root',
    group  => 'root',
    mode   => '0755',
  }

  # Allow Nginx HTTP through UFW
  class { 'nginx_example::allow_nginx_http': }

  # Create Nginx server configuration
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('nginx_example/nginx.conf.erb'),
    require => Class['nginx_example::install_nginx'],
    notify  => Service['nginx'],
  }

  # Display a custom message
  exec { 'echo_hello_world':
    command => '/bin/echo "Hello World!" > /var/www/html/index.nginx-debian.html',
    require => Class['nginx_example::install_nginx'],
  }

  # Display a custom 404 page
  exec { 'echo_custom_404':
    command => '/bin/echo "Ceci n\'est pas une page" > /var/www/html/custom_404.html',
    require => Class['nginx_example::install_nginx'],
  }
}

class nginx_example::install_nginx {
  package { 'nginx':
    ensure  => installed,
    require => Exec['update-package-list', 'upgrade-packages'],
  }

  service { 'nginx':
    ensure     => running,
    enable     => true,
    hasstatus  => true,
    hasrestart => true,
    require    => Package['nginx'],
  }
}

class nginx_example::allow_nginx_http {
  exec { 'allow_nginx_http':
    command => '/usr/sbin/ufw allow "Nginx HTTP"',
    require => Class['nginx_example::install_nginx'],
  }
}

# ERB template for Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx_example/nginx.conf.erb'),
}

# Apply the nginx_example class
include nginx_example

