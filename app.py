# app.pys
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello level 400 FET, Quality Assurance!"


if __name__ == '__main__':
    app.run(debug=True)
