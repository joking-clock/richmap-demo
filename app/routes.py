import os
from flask import render_template, flash, redirect, url_for, session, request
from app import app
from app.forms import LoginForm, photos
from app.search import SearchForm
from app.map import MapService
import googlemaps
from werkzeug import secure_filename
from datetime import datetime
from flask_login import current_user, login_user, logout_user
from app.models import Retailer, RetailerAddress, Coupon
import sys

# gmaps = googlemaps.Client(key='AIzaSyCts7em4L-ni5Lrc1goEXae-uqyVwtIcxI')

# @app.route('/index')
# def index():
#     if current_user.is_authenticated:
#         return redirect(url_for('login'))
#     # search = SearchForm()
#
#
#     # return render_template('index.html', info=posts, search=search)
#     return render_template('index.html')

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    location_list = RetailerAddress.query.all()
    # print(location_list[0].address, location_list[1].address, file=sys.stderr)

    map = MapService()
    coordinate = []
    result = None
    for index in location_list:
        result = map.geocode(index.address)
        coordinate.append(result)
    # return render_template('map.html', coordinate=coordinate)

    # location_default = {
    #     'shop': {'shopname': 'Starbucks'},
    #     'address': '3740 Midland Ave, Toronto, ON',
    #     'coordinate': {'lat': 43.821, 'lng': -79.298}
    # }
    if request.method == 'POST':
        name_login = request.form.get('name_login')
        password_login = request.form.get('password_login')
        retailer = Retailer.query.filter_by(name=name_login).first()
        if retailer is None or not retailer.check_password(password_login):
        # if retailer is None or not retailer.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('index'))
        login_user(retailer, remember=password_login)
        # return render_template('index.html', username=name_login, info_default=location_default)
        return render_template('index.html', username=name_login, coordinate_default = coordinate)

    # form_login on the left of equal sign is the name in template, the "form_login" on the right side is form_login = LoginForm
    # return render_template('index.html', info_default=location_default)
    return render_template('index.html', coordinate_default = coordinate)


# def login():
#     form_login = LoginForm()
#     if form_login.validate_on_submit():
#         retailer = Retailer.query.filter_by(name=form_login.name.data).first()
#         if retailer is None or not retailer.check_password(form_login.password.data):
#         # if retailer is None or not retailer.check_password(form.password.data):
#             flash('Invalid username or password')
#             return redirect(url_for('login'))
#         login_user(retailer, remember=form_login.remember_me.data)
#         return redirect(url_for('index'))
#
#     location_default = {
#         'shop': {'shopname': 'Starbucks'},
#         'address': '3740 Midland Ave, Toronto, ON',
#         'coordinate': {'lat': 43.821, 'lng': -79.298}
#     }
#
#     # form_login on the left of equal sign is the name in template, the "form_login" on the right side is form_login = LoginForm
#     return render_template('index.html', info_default=location_default, form_login = form_login)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')
    # form would be used in template
'''    form = LoginForm()
    if form.validate_on_submit():
        # flash('Check-in information requested for shope {}, address={}'.format(
        #    form.shopname.data, form.address.data))
        # return redirect(url_for('index'))
        # session['address']=form.address.data
        # return redirect(url_for('map'))
        filename = photos.save(form.photo.data)
        file_url = photos.url(filename)

        map = MapService()
        result = map.geocode(form.address.data)
        coordinate = {'lat':result['lat'], 'lng':result['lng']}
        coupon = {'type':form.coupontype.data,'cdata':form.coupon.data}
        session['coordinate'] = coordinate
        session['coupon'] = coupon
        session['file_url'] = file_url
        return redirect(url_for('info'))
    return render_template('register.html', form=form)'''

@app.route('/info', methods=['GET', 'POST'])
def info():
    coordinate = session.get('coordinate', None)
    coupon = session['coupon']
    imgpath = session.get('file_url')
    return render_template('map.html', coordinate=coordinate, coupondata=coupon, img=imgpath)

@app.route('/addAddress', methods=['GET', 'POST'])
def addAddress():
    return render_template('addAddress.html')

@app.route('/couponpage', methods=['GET', 'POST'])
def couponpage():
    return render_template('couponpage.html')
