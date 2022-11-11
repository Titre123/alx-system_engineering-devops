# puppet file to fix multiple request problem

exec { 'fix--for-nginx':
  $comm = 's/15/4096/'
  command   => "sed -i $comm /etc/default/nginx",
  provider  => shell,
}

exec { 'restart nginx':
  command   => 'service nginx restart',
  require   => Exec['fix--for-nginx'],
  provider  => shell,
}
