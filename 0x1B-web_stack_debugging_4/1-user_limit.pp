# To open files without error

exec {'Updating limits to Holberton User':
  command  => "sed -i 's/holberton soft nofile.*/holberton soft nofile 7000/' /etc/security/limits.conf",
  provider => shell
}
exec {'Updating limit to Holberton User':
  command  => "sed -i 's/holberton hard nofile.*/holberton hard nofile 7000/' /etc/security/limits.conf",
  provider => shell
}
