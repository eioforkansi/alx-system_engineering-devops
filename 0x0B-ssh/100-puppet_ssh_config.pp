# This Puppet manifest sets up client SSH configuration file so that you can connect to a server without typing a password.

file {  '/root/.ssh/config':
    ensure => file,
}

file_line { 'Host configuration':
    path => '/root/.ssh/config',
    line => 'Host ubuntu@18.210.15.231',
}

file_line { 'Set HostName':
    path  => '/root/.ssh/config',
    line  => '   HostName 18.210.15.231',
    match => '^  HostName',
}

file_line { 'Set User':
    path  => '/root/.ssh/config',
    line  => '  User ubuntu',
    match => '^ User',
}

file_line { 'Set IdentityFile':
    path  => '/root/.ssh/config',
    line  => '  IdentityFile ~/.ssh/school',
    match => '^  IdentityFile',
}

file_line { 'Disable Password Authentication':
    path  => '/root/.ssh/config',
    line  => '   PasswordAuthentication no',
    match => '^  PasswordAuthentication',
}
