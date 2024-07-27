# This manifest uses the exec resource to kill a process named 'killmenow'
exec { 'kill_process':
  command => '/usr/bin/pkill -f killmenow',
  path    => ['/usr/bin', '/usr/local/bin'],
  unless  => 'pgrep -f killmenow',
}
