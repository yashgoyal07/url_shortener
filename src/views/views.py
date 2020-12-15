from flask import render_template, request
from application import app


@app.route('/')
def slink():
    return render_template('slink.html')


@app.route('/slinkit', methods=['post'])
def slinkit():
    longlink = request.form['longlink']
    return render_template('panel.html', lolink=longlink)


@app.route('/panel')
def panel():
    return render_template('panel.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
