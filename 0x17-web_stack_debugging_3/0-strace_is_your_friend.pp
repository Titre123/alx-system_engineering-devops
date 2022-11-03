# fix debugging problem
exec { 'replace':
  command => 'sed -i -e "s/class-wp-locale.phpp/class-wp-locale.php/g /var/www/html/wp-settings.php',
  return  => 0,
  path    => '/usr/bin',
}
