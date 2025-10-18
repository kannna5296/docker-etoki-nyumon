FROM python:3.11-slim

# MySQLモジュール
RUN pip install mysql-connector-python

# メールモジュール
RUN apt-get update && apt-get install -y msmtp-mta
COPY ./msmtprc /etc/msmtprc

CMD ["/usr/local/bin/python", "-m", "http.server", "8001"]