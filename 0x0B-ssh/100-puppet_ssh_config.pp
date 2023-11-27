# manifest testing

file { '/etc/ssh/ssh_config':
  ensure => present,
}
exec { 'Turn off passwd auth':
  command => '/usr/bin/echo -e "\tPasswordAuthentication no" >> /etc/ssh/ssh_config',
  returns => [0, 1],
}
exec { 'Delare identity file':
  command => '/usr/bin/echo -e "\tIdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
  returns  => [0, 1],
}
