FROM php:8.4

RUN docker-php-ext-install pdo_mysql

RUN apt-get update && apt-get install -y msmtp-mta

COPY ./msmtprc /etc/msmtprc

CMD ["/user/local/bin/php", "--server", "0.0.0.0:8000", "--docroot", "/my-work"]