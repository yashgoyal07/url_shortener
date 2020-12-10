from application import app
from flask import render_template

@app.route('/')
def slink():
    return render_template('slink.html')

if __name__ == '__main__':
	app.run(debug=True)