from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    shopname = StringField('shopname', validators=[DataRequired()])
    address = StringField('address', validators=[DataRequired()])
    shoppertype = StringField('mechant type', validators=[DataRequired()])
    coupon = StringField('coupon', validators=[DataRequired()])
    coupontype = StringField('coupontype', validators=[DataRequired()])
    submit = SubmitField('Check in')
