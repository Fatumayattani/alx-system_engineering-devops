class nginx_custom_http_response_header {

  # Set the name of the custom HTTP header
  $header_name = 'X-Served-By'

  # Get the hostname of the machine Nginx is running on
  $server_hostname = $::hostname

  # Configure Nginx to include the custom HTTP header
  file { '/etc/nginx/conf.d/custom-http-header.conf':
    content => "add_header ${header_name} ${server_hostname};",
    mode    => '0644',
    owner   => 'root',
    group   => 'root',
    notify  => Service['nginx'],
  }
}
