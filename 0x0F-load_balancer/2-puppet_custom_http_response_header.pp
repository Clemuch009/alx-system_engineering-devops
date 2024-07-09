# 2-puppet_custom_http_response_header.pp
# Puppet manifest to configure Nginx with a custom HTTP header

node default {
  # Ensure the Nginx package is installed
  package { 'nginx':
    ensure => installed,
  }

  # Ensure the Nginx service is running and enabled
  service { 'nginx':
    ensure     => running,
    enable     => true,
    require    => Package['nginx'],
  }

  # Create the Nginx configuration file with a custom HTTP header
  file { '/etc/nginx/conf.d/custom_header.conf':
    ensure  => file,
    content => template('nginx/custom_header.conf.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  # Ensure the Nginx default site configuration file is present
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    require => Package['nginx'],
    notify  => Service['nginx'],
  }
}

# Create the custom_header.conf.erb template
file { '/etc/puppetlabs/code/environments/production/modules/nginx/templates/custom_header.conf.erb':
  ensure  => file,
  content => "add_header X-Served-By <%= @hostname %>;",
}

# Generate the hostname fact for use in the template
$hostname = $facts['hostname']

