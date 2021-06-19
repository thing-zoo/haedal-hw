from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return '2019113772 컴퓨터학부 정명주'


@app.route('/me/')
def me():
    return render_template('index.html', cat_img='cat.jpeg')


if __name__ == "__main__":
    app.run(debug=True)