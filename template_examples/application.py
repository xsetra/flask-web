from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html', TOP_CONTENT=content())


def content():
    CONTENT = {"Basics":[["Introduction to Python","/intro/"],
                            ["Print functions and Strings","/print/"],
                            ],
                  "WebDev":[]}
    return CONTENT

if __name__ == '__main__':
    app.run(debug=1)
