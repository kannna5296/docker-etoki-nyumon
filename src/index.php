<?php

$users = [];

$dsn = "mysql:host=db;port=3306;dbname=sample";
$username = "root";
$password = "secret";

try {
  $pdo = new PDO($dsn, $username, $password);
  
  $statement = $pdo->query("SELECT * FROM user");
  $statement->execute();
  while ($row = $statement->fetch()) {
    $users[] = $row;
  };
  // 切断
  $pdo = null;
} catch (PDOException $e) {
  echo "データベース接続失敗: " . $e->getMessage();
}

foreach ($users as $user) {
  echo "<p>id: " . "" . $user['id'] . ", name: " . $user['name'] . "</p>";
}

$subject = "Test Email";
$body = "DockerHubはこちら→ https://hub.docker.com/";
foreach ($users as $user) {
  #mb_send_mailはPHPのマルチバイト対応メール送信関数
  $success = mb_send_mail($user['email'], $subject, $body);
  if ($success) {
    echo "<p>メール送信成功: " . $user['email'] . "</p>";
  } else {
    echo "<p>メール送信失敗: " . $user['email'] . "</p>";
  }
}
?>