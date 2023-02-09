#Enable the user holberton to login and open files without error
exec { 'increase-hard-file-limit-for-holberton-user':
  command  => 'sudo sed -i \'s/nofile 5/nofile 30000/\' /etc/security/limits.conf',
  provider => shell,
}
exec { 'increase-soft-file-limit-for-holberton-user':
  command  => 'sudo sed -i \'s/nofile 4/nofile 10000/\' /etc/security/limits.conf',
  provider => shell,
}
