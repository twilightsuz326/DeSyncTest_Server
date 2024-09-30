# Pythonベースイメージを使用
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /usr/src/app

# 必要なライブラリをインストール
RUN pip install flask==1.1.2 gunicorn==20.0.4 Jinja2==2.11.3 MarkupSafe==1.1.1 itsdangerous==1.1.0 Werkzeug==1.0.1

# Webサーバーのスクリプトをコピー
COPY server.py .

# サーバーを起動
CMD ["gunicorn", "-b", "0.0.0.0:8080", "server:app"]
