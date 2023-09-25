#puppet code
file { '/etc/ssh/ssh_config':
   ensure   => file,
   content  => "Host 34.201.174.165\
         HostName 34.201.174.165\
         User ubuntu\
         IdentityFile ~/.ssh/school\
         PasswordAuthentication no",
}
