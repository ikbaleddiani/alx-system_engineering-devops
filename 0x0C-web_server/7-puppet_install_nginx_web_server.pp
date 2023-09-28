# Manifest that configures an Nginx web server using Puppet

exec {'apt_update':
  command     => 'sudo apt-get update',
  path        => '/usr/bin:/usr/sbin',
  refreshonly => true,
}

package {'nginx':
  ensure  => 'installed',  
  require => Exec['apt_update'],
}

service {'nginx':
  ensure  => 'running',
  enable  => true,
  require => package['nginx'],
}

file {'/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => package['nginx'],
}

file_line {'redirect':
  path    => '/etc/nginx/sites-available/default',
  line    => 'location /redirect_me { return 301 https://www.youtube.com/; }',
  match   => '^\troot /var/www/html;$',
  ensure  => 'present',
  require => package['nginx'],
  notify  => Service['nginx'],
}
