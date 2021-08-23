from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/integrate')
def list_user():
    return {'data': "Интеграция с Flask прошла успешно"}


if __name__ == '__main__':
    app.run()
