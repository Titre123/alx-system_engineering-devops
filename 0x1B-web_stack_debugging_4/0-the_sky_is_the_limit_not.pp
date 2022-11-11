# puppet file to fix multiple request problem

exec { 'fix--for-nginx':
   command   => "sed -i 's/15/4096/' /etc/default/nginx",
   provider  => shell,
}

exec { 'restart nginx':
   command   => "service nginx restart",
   require   => Exec['fix--for-nginx'], 
   provider  => shell,
}
