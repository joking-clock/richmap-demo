import os
from flask import render_template, flash, redirect, url_for, session, request
from app import app
from app.forms import LoginForm, photos
from app.map import MapService
import googlemaps
from werkzeug import secure_filename

# gmaps = googlemaps.Client(key='AIzaSyCts7em4L-ni5Lrc1goEXae-uqyVwtIcxI')

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
        return redirect(url_for('info', para1=coordinate, para2=coupon, para3=file_url))
    return render_template('login.html', form=form)

@app.route('/info', methods=['GET', 'POST'])
def info():
    coordinate = request.args['para1']
    coupon = request.args['para2']
    imgpath = request.args['para3']
    return render_template('map.html', coordinate=coordinate, coupondata=coupon, img=imgpath)