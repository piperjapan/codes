#!/bin/bash
systemctl stop httpd
rm -f /etc/httpd/conf.d/myweb.conf
rm -f /var/www/wsgi.py
rm -f /var/www/app.py