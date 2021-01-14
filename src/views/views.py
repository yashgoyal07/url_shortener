import uuid
from flask import render_template, request, session
from application import app
# from controllers.links_controller import LinksController
# from controllers.customers_controller import CustomersController


app.secret_key = b'\xce\xdd(B\xdd\xf1\x19\x04\x8c\xf0 BV\x93e\x8c'


@app.route('/')
def slink():
    return render_template('slink.html')


@app.route('/slink_it', methods=['post'])
def slink_it():
    long_link = request.form['long_link']
    if long_link:
        session['cus_id'] = uuid.uuid4()
        return "cookie sets successfully"
    else:
        return "something went wrong"


@app.route('/panel')
def panel():
    return render_template('panel.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    # if request.method == 'POST':
    #     try:
    #         customer = request.form
    #         name = customer['name']
    #         email = customer['email']
    #         mobile = customer['mobile']
    #         password = customer['pass']
    #         error = CustomersController().create_customer(name, email, mobile, password)
    #         if error:
    #             return "Please Try Again"
    #         else:
    #             return "Registration Successful"
    #     except:
    #         return "Something Went Wrong"

    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
