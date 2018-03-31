from app import app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from werkzeug import secure_filename

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

class LoginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm():
    # shoppertype = StringField('mechant type', validators=[DataRequired()])
    coupon = StringField('coupon', validators=[DataRequired()])
    # coupontype = StringField('coupontype', validators=[DataRequired()])
    # submit = SubmitField('Check in')
    # photo = FileField(validators=[FileAllowed(photos, u'Image only!'), FileRequired(u'File was empty!')])
