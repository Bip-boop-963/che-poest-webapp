from flask import Flask, send_from_directory
from pyngrok import ngrok

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory('.', 'index.html')

if __name__ == "__main__":
    # Подключение ngrok
    public_url = ngrok.connect(5000)
    print("Веб-приложение доступно по:", public_url)

    # Запуск локального сервера
    app.run(port=5000)
