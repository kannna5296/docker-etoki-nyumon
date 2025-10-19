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

    return html_output
  except Exception as e:
     traceback.print_exc()
     return "接続失敗！！！！"
  finally:
    if conn:
        conn.close()