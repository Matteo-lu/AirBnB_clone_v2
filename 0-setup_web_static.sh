#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.
if [ ! -x /usr/sbin/nginx ]; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo tee -a /data/web_static/releases/test/index.html > /dev/null << END
<html >
<head >
</head >
<body >
Holberton School
</body >
</html >
END
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i '57 i \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
