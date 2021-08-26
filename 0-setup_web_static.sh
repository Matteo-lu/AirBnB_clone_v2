#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
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
sudo sed -i '/server_name_;/ a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\t}' /etc/nginx/sites-available/default
sudo service nginx restart
