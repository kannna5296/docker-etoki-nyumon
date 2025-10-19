import subprocess
import mysql.connector as connector
import traceback
import html

def get_users():
  users = []
  html_output = ""

  try:
    conn = connector.connect(
      host="db",          # Docker ComposeでMySQLを立てる場合はサービス名
      user="app",
      password="pass1234",
      port='3306',
      database="sample"
    )
    cursor = conn.cursor(buffered=True, dictionary=True)

    cursor.execute("SELECT * FROM user;")
  
    # 結果をすべて取得
    for row in cursor.fetchall():
      users.append(row)
    # HTML作成
    for user in users:
        html_output += f"<p>id: {html.escape(str(user['id']))}, name: {html.escape(user['name'])}</p>\n"

    subject = "Test Email From Python"
    body = "DockerHubはこちら→ https://hub.docker.com/"
    for user in users:
      recipient = user.get("email", "")
      try:
        msg = f"Subject: {subject}\nFrom: service@example.com\nTo: {recipient}\n\n{body}"
        result = subprocess.run(["msmtp", "-t"], input=msg.encode("utf-8"),stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
          html_output += f"<p>メール送信成功. {html.escape(str(user['name']))} </p>\n"
        else:
          html_output += f"<p>メール送信失敗. {html.escape(str(user['name']))} {str(result.stderr)}</p>\n"
      except Exception as e:
        html_output += f"<p>メール送信失敗. {html.escape(str(user['name']))} {str(e)}</p>\n"
    return html_output
  except Exception as e:
     traceback.print_exc()
     return "接続失敗！！！！"
  finally:
    if conn:
        conn.close()