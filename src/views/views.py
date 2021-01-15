import uuid
from flask import render_template, request, session
from application import app
from helpers.utils import is_customer, short_link_generator
# from controllers.links_controller import LinksController
from controllers.customers_controller import CustomersController


app.secret_key = b'\xce\xdd(B\xdd\xf1\x19\x04\x8c\xf0 BV\x93e\x8c'


@app.route('/')
def slink():
    if not is_customer():
        cus_id = uuid.uuid4().int
        result = CustomersController().create_customer(cus_id=cus_id)
        if result:
            session['cus_id'] = cus_id
            return "you become guest user"
        else:
            return "Another User Existed"
    return render_template('slink.html')


# @app.route('/slink_it', methods=['post'])
# def slink_it():
#     if is_customer():
#         long_link = request.form['long_link']
#         if long_link:
#             slink = short_link_generator()
#
#
#


@app.route('/panel')
def panel():
    return render_template('panel.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        if is_customer():
            try:
                customer = request.form
                name = customer['name']
                email = customer['email']
                mobile = customer['mobile']
                password = customer['password']
                result = CustomersController().create_customer(cus_id=session['cus_id'], name=name, email=email, mobile=mobile, password=password)
                if result == "No Response":
                    return "Update Successful"
                else:
                    return "Something Wrong"
            except:
                return "Something Went Wrong"
        else:
            return "you are not a customer"
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
