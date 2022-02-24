# increases the nginx limit to 2000
exec { 'fix file limit':
  onlyif  => 'test -e /etc/default/nginx',
  command => 'sed -i 's/15/2000/' /etc/default/nginx; service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
