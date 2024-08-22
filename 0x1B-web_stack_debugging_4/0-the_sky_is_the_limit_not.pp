# Increases the amount of traffic an Nginx server can handle.

# Increase the file descriptor limit for Ngnix
exec {'increase-ulimit-for-nginx':
    command => 'sed -i "s/15/4096/" /etc/default/nginx',
    path    => '/usr/local/bin/:/bin/'
} ->

# Restart Nginx service
exec {'nginx-restart':
    command => 'service nginx restart',
    path    => '/etc/init.d'
}
