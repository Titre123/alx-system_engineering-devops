# puppet script to kill killmenow process
exec{ 'kill process':
  command => 'pkill killmenow',
  path    => './killmenow',
}
