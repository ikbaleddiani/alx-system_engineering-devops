# Manifest that configures an Nginx web server using Puppet

exec { 'apt_update':
  command     => 'apt-get update',
  path        => '/usr/bin:/usr/sbin',
  refreshonly => true,
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt_update'],
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

file_line { 'redirect':
  ensure  => 'present',
  line    => 'location / { return 200 "Hello World!"; }',
  match   => '^\troot /var/www/html;$',
  path    => '/etc/nginx/sites-available/default',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

file_line { 'redirect':
  ensure  => 'present',
  line    => 'location /redirect_me { return 301 https://www.youtube.com/; }',
  match   => '^\troot /var/www/html;$',
  path    => '/etc/nginx/sites-available/default',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

