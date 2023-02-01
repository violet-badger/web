from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')


@app.route('/blog')
def blog():
    return "WIP"


if __name__ == '__main__':
    app.run()
