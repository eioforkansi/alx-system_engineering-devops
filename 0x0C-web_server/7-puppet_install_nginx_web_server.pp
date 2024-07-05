# This Puppet manifest installs and configure an Nginx server. Also performs a 301 redirect when querying /redirect_me.

# Ensure nginx package is installed
package { 'nginx':
    ensure => installed,
}

# Create the index.html file with "Hello World!" content
file { '/var/www/html/index.html':
    ensure  => present,
    content => 'Hello World!',
}

# Create a custom 404 error page
file { '/var/www/html/error_404.html':
    ensure  => present,
    content => "Ceci n'est pas une page",
}

# Create the default site configuration for nginx
file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm;

    location /redirect_me {
        return 301 https://youtube.com/;
    }


    error_page 404 /error_404.html;
    location /404 {
    root /var/www/html;
        internal;
    }
    }",
    require => Package['nginx'],
    notify  => Service['nginx'],
}

# Create a symbolic link to enable the site
file { '/etc/nginx/sites-enabled/default':
    ensure => link,
    target => '/etc/nginx/sites-available/default',
    notify => Service['nginx'],
}

# Ensure nginx service is running and enabled
service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/sites-enabled/default'],

}
