# remove extra p in config file and add env variables to source
exec { 'typo and envvars':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php;
  	      source /etc/apache2/envvars",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
