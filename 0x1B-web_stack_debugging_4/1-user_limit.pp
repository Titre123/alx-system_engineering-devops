# Puppet file to confiure user holberton limits

exec { 'change-os-configuration-for-holberton-user':
  command  => 'sed -i "s/nofile 4/nofile 1024/" /etc/security/limits.conf',
  provider => shell,
}

exec { 'change-os-configuration-for-holberton':
  command  => 'sed -i "s/nofile 5/nofile 2048/" /etc/security/limits.conf',
  require  => Exec['change-os-configuration-for-holberton-user'],
  provider => shell,
}
