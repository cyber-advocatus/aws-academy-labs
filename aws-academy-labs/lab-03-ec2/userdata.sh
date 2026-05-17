#!/bin/bash
# Lab 3 - User Data Script
# Instala Apache e cria página web simples

dnf install -y httpd
systemctl enable httpd
systemctl start httpd
echo '<html><h1>Hello From Your Web Server!</h1></html>' > /var/www/html/index.html
