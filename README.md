## これは何
https://www.shuwasystem.co.jp/book/9784798071503.html　
この書籍をやってみたTRYログ

プラスアルファで、python用のコンテナもdocker composeで作ってみた


## コマンドで作るときのやつメモ

### app
```
docker container run --name app --rm --detach --publish 8000:8000 --mount type=bind,source="$(pwd)"/src,dst=/my-work --network work-network work-app:0.1.0 /usr/local/bin/php --server 0.0.0.0:8000 --docroot /my-work
```
※work-app:0.1.0は自前で作ったやつ

### db
```
docker container run --name db --rm --detach --publish 3306:3306 --mount type=bind,source=$(pwd)/docker/db/init,dst=/docker-entrypoint-initdb.d --mount type=volume,source=work-db-volume,dst=/var/lib/mysql --network work-network
--env MYSQL_ROOT_PASSWORD=secret --env MYSQL_USER=app --env MYSQL_PASSWORD=pass1234 --env MYSQL_DATABASE=sample --env TZ=Asia/Tokyo mysql:8.4.0 
```
※--envの後にイメージ指定が来ないといけないっぽい

### mail
```
docker container run --name mail --rm --detach --publish 8025:8025 --env TZ=Asia/Tokyo --mount type=volume,source=work-mail-volume,dst=/data --network work-network axllent/mailpit:v1.10.1
```