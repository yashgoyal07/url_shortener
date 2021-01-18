import uuid
import logging
from flask import render_template, request, session, flash, redirect, url_for
from application import app
from helpers.utils import is_customer, short_code_generator, is_visitor
from controllers.links_controller import LinksController
from controllers.customers_controller import CustomersController


app.secret_key = b'\xce\xdd(B\xdd\xf1\x19\x04\x8c\xf0 BV\x93e\x8c'


@app.route('/<slink_id>')
def redirection(slink_id):
    try:
        result = LinksController().find_long_link(slink_id)
        if not result:
            raise ValueError
        return redirect(result[0].get("long_link"))
    except Exception as err:
        print(err)
        return "Link not exist or expired"


@app.route('/')
def slink():
    try:
        if is_customer():
            cus_id = session['cus_id']
            return render_template('slink.html', customer_id=cus_id)
        if not is_visitor():
            cus_id = uuid.uuid4().hex
            CustomersController().create_user(cus_id=cus_id)
            session['cus_id'] = cus_id
    except Exception as err:
        flash('Something Went Wrong. Try Again', 'danger')
        logging.error('error from slink occurred due to {err}')
    return render_template('slink.html')


@app.route('/slink_it', methods=['POST'])
def slink_it():
    if is_customer() or is_visitor():
        long_link = request.form.get('long_link')
        if long_link:
            try:
                short_code = short_code_generator()
                LinksController().create_slink(slink=short_code, long_link=long_link,
                                                        customer_id=session['cus_id'])
                flash('Slink Created', 'success')
                return redirect(url_for('panel'))
            except Exception as err:
                flash('Something Went Wrong. Try Again', 'danger')
                logging.error(f'error from slink_it occurred due to {err}')
    else:
        flash('Please Retry', 'danger')
    return render_template('slink.html')


@app.route('/panel')
def panel():
    if is_visitor() or is_customer():
        try:
            customer_id = session['cus_id']
            result = LinksController().show_slink(customer_id=customer_id)
            if not is_customer():
                return render_template('panel.html', slink_data=result)
            customer_status = session['Registered']
            return render_template('panel.html', cus_status=customer_status, slink_data=result)
        except Exception as err:
            flash('Something Went Wrong. Try Again', 'danger')
            logging.error(f'error from panel occurred due to {err}')
    return redirect(url_for('slink'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if is_customer():
        return redirect('panel')
    if request.method == 'POST':
        try:
            customer = request.form
            email = customer.get('email')
            password = customer.get('password')

            # email and password both are mandatory
            if not email or not password:
                raise ValueError

            result = CustomersController().find_customer(email=email.lower(), password=password)

            # if not a valid customer found
            if not result:
                raise ValueError

            session['cus_id'] = result[0].get('customer_id')
            session['Registered'] = 'Y'
            flash('You are Successfully Logged In', 'success')
            return redirect(url_for('panel'))
        except Exception as err:
            flash('Email or Password is incorrect', 'danger')
            logging.error(f'error from login occurred due to {err}')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('cus_id', None)
    session.pop('Registered', None)
    return redirect(url_for('slink'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if is_customer():
        return redirect('panel')
    if request.method == 'POST':
        if is_visitor():
            try:
                customer = request.form
                name = customer.get('name')
                email = customer.get('email')
                mobile = customer.get('mobile')
                password = customer.get('password')

                # mobile no. consists only digits
                if not mobile.isnumeric():
                    raise ValueError

                # email and password both are mandatory
                if not email or not password:
                    raise ValueError

                CustomersController().update_customer(name=name.lower(), email=email.lower(), mobile=mobile.lower(), password=password, cus_id=session['cus_id'])
                session['Registered'] = 'Y'
                flash('You are Successfully Updated', 'success')
                return redirect(url_for('panel'))
            except Exception as err:
                flash('Something Went Wrong. Try Again', 'danger')
                logging.error(f'error from signup occurred due to {err}')
        else:
            try:
                customer = request.form
                name = customer.get('name')
                email = customer.get('email')
                mobile = customer.get('mobile')
                password = customer.get('password')

                # mobile no. consists only digits
                if not mobile.isnumeric():
                    raise ValueError

                # email and password both are mandatory
                if not email or not password:
                    raise ValueError

                cus_id = uuid.uuid4().hex
                CustomersController().create_customer(cus_id=cus_id, name=name.lower(), email=email.lower(), mobile=mobile.lower(), password=password.lower())
                session['cus_id'] = cus_id
                session['Registered'] = 'Y'
                flash('You are Successfully Registered', 'success')
                return redirect(url_for('panel'))
            except Exception as err:
                flash('Something Went Wrong. Try Again', 'danger')
                logging.error(f'error from signup occurred due to {err}')

    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
