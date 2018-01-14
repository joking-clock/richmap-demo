from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    owner = {'shopname': 'Richmap'}
    posts = [
        {
            'shop': {'shopname': 'Starbucks'},
            'address': '3740 Midland Ave, Toronto, ON'
        },
        {
            'shop': {'shopname': 'Origination Noodle House'},
            'address': '633 Silver Star Blvd, Scarborough, ON'
        }
    ]
    return render_template('index.html', title='Home', shop=owner, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # form would be used in template
    form = LoginForm()
    if form.validate_on_submit():
        flash('Check-in information requested for shope {}, address={}'.format(
            form.shopname.data, form.address.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Check In', form=form)
