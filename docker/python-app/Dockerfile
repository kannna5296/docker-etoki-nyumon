FROM python:3.11-slim

# MySQLモジュール
RUN pip install mysql-connector-python flask

# メールモジュール
RUN apt-get update && apt-get install -y msmtp-mta 
COPY ./msmtprc /etc/msmtprc

# Flaskアプリ起動
CMD ["/usr/local/bin/python", "/my-work/app.py"]