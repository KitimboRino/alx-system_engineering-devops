# Automating project requirements using Puppet

# Install NGINX package
package { 'nginx':
  ensure => installed, # Ensure NGINX is installed on the system
}

# Modify NGINX configuration file to add a rewrite rule
file_line { 'install':
  ensure => 'present', # Ensure the line is present in the file
  path   => '/etc/nginx/sites-enabled/default', # Path to NGINX configuration file
  after  => 'listen 80 default_server;', # Insert the line after this specified line
  line   => 'rewrite ^/redirect_me https://www.github.com/KitimboRino permanent;', # Rewrite rule to be added
}

# Create an HTML file with "Hello World!" content
file { '/var/www/html/index.html':
  content => 'Hello World!', # Content of the HTML file
}

# Manage NGINX service
service { 'nginx':
  ensure  => running, # Ensure NGINX service is running
  require => Package['nginx'], # NGINX service depends on NGINX package being installed
}

