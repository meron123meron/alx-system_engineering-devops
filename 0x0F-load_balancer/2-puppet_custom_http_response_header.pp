#  automate the task of creating a custom HTTP header response, but with Puppet.
#The name of the custom HTTP header must be X-Served-By
#The value of the custom HTTP header must be the hostname of the server Nginx is running on

exec { 'command':
  command  => 'apt-get -y update;
  apt-get -y install nginx;
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  service nginx restart',
}
