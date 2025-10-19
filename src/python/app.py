from flask import Flask
import python.main as main

# サーバ起動ようのスクリプト
# phpはDockerfile/CMDでコマンド指定+スクリプトの結果を動的に取得できたけど、pythonはFlask入れた方が楽そうなのでこっちにする

app = Flask(__name__)

@app.route("/")
def index():
    return main.get_users()

if __name__ == "__main__":
    # コンテナ外からアクセスできるよう host=0.0.0.0
    app.run(host="0.0.0.0", port=8001)
