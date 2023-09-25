# SSH client configuration file
file {'SSH client config':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  content =>'
# SSH client configuration file


Host 54.90.57.9
    PasswordAuthentication no
    IdentityFile ~/.ssh/school',
}
