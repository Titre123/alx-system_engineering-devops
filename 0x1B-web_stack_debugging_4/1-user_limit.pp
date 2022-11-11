# puppet file to enable holberton user
user { 'holberton':
    ensure   => 'present',
    password => 'holberton',
}
