from flask import Flask, render_template, flash

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/dashboard/')
def dashboard():
    flash('TEST 1')
    flash('TEST MESSAGE 2')
    flash('TEST MESSAGE EXAMPLES 3')
    return render_template('dashboard.html', TOP_CONTENT=content())


@app.route('/slashboard/')
def slashboard():
    try:
        return render_template('dashboard.html', TOP_CONTENT=boom )
    except Exception as e:
        return render_template('500.html', error=str(e))

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


def content():
    CONTENT = {"Basics":[["Introduction to Python","/intro/"],
                            ["Print functions and Strings","/print/"],
                            ],
                  "WebDev":[]}
    return CONTENT

if __name__ == '__main__':
    app.secret_key = "secret_key_first"
    app.run(debug=1)
