# Using Puppet, create a file in /tmp
# syntax : ressource_type {'name': attribute => value, ..., ..., }
file {'create school':
  path    => '/tmp/school',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
