#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.
REQUIRED_PKG="nginx"
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG|grep "install ok installed")
if [ "" = "$PKG_OK" ]; then
	#sudo apt-get update
	#sudo apt-get -y upgrade
  	sudo apt-get -y install $REQUIRED_PKG
fi
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
sudo chown -R ubuntu /data/web_static/releases/test/index.html
sudo echo "If you see this it's because you just succeeded <3" >> /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo > /etc/nginx/sites-enabled/default
sudo echo -e "server {\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\t}\n}" >> /etc/nginx/sites-enabled/default
sudo nginx -s reload
