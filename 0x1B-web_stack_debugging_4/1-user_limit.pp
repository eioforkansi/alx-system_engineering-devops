# Enable the user holberton to login and open files without error.

# Increase hard file limit for Holberton user.
exec {'increase-hard-file0limit-for-holberton-uer':
    command => 'sed -i "/holberton hard/s/5/5000/" /etc/security/limits.conf',
    path    => '/usr/local/bin/:/bin/'
}

# Increase soft file limit for Holbertin user.
exec {'increase-soft-file-limiti-for-holberton-user':
    command => 'sed -i "/holberton soft/s/4/5000/" /etc/security/limits.conf',
    path    => '/usr/local/bin/:/bin/'

}
