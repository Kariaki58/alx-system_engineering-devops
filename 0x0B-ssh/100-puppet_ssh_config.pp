file { "append to puppet":
  path    => "/home/mi4/.ssh/config",
  ensure  => present,
  content => "Host ubuntuserver\n\tHostname 107.23.113.143\n\tUser ubuntu\n\tPasswordAuthentication no\n",
}
