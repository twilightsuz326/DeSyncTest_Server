# Pythonベースイメージを使用
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /usr/src/app

# 必要なライブラリをインストール
RUN pip install flask

# Webサーバーのスクリプトをコピー
COPY server.py .

# サーバーを起動
CMD ["python", "./server.py"]
