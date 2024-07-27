# This manifest installs Flask version 2.1.0 using the pip3 provider
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip',
}
