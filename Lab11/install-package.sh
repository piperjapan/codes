#!/bin/bash
yum install -y httpd python-pip
systemctl start httpd
yum install -y mod_wsgi
pip install flask
rm -f /etc/httpd/conf.d/myweb.conf
rm -f /var/www/wsgi.py
rm -f /var/www/app.py