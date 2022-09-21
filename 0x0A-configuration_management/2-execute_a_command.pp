# puppet script to kill killmenow process
exec{ 'kill process':
  command  => 'pkill killmenow',
  path     => ['/usr/bin', '/usr/sbin'],
  provider => 'shell'
}
