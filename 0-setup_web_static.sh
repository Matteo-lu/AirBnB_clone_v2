#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.
REQUIRED_PKG="nginx"
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG|grep "install ok installed")
if [ "" = "$PKG_OK" ]; then
	sudo apt-get update
	sudo apt-get -y upgrade
  	sudo apt-get -y install $REQUIRED_PKG
fi
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
sudo tee -a /data/web_static/releases/test/index.html > /dev/null << END
<html >
<head >
</head >
<body >
Holberton School
</body >
</html >
END
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i '/$hostname;/ a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\t}' /etc/nginx/sites-available/default
sudo service nginx restart
