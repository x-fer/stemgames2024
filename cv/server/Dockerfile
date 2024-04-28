FROM php:8.3-rc-apache-bullseye

COPY html /var/www/html
COPY flag.txt /var/www/flag.txt
RUN mkdir /var/www/html/uploads
RUN chown -R root:root /var/www/html
RUN chmod -R 755 /var/www/html
RUN chown www-data:www-data /var/www/html/uploads 

