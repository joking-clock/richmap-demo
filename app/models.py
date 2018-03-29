from datetime import datetime
from app import db


class Retailer(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    rType = db.Column(db.String(32))
    rDescription = db.Column(db.Text)
    password_hash = db.Column(db.String(128))
    addresslist = db.relationship('RetailerAddress', backref='shopper', lazy='dynamic')
    coupons = db.relationship('Coupon', backref='shopper', lazy='dynamic')
    __tablename__ = "retailer"

    def __repr__(self):
        return '<Retailer {}>'.format(self.name)


class RetailerAddress(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    retailerID = db.Column(db.String(64), db.ForeignKey('retailer.id'))
    address = db.Column(db.String(120))
    city = db.Column(db.Text)
    contactNumber = db.Column(db.String(32))
    coupons = db.relationship('Coupon', backref='shopper_address', lazy='dynamic')
    __tablename__ = "retailer_address"

    def __repr__(self):
        return '<Address {}>'.format(self.address)


class Coupon(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    retailerID = db.Column(db.Integer, db.ForeignKey('retailer.id'))
    addressID = db.Column(db.Integer, db.ForeignKey('retailer_address.id'))
    couponTitle = db.Column(db.String(64))
    currentPrice = db.Column(db.Float)
    discountType = db.Column(db.String(32))
    offValue = db.Column(db.Float)
    percent = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    createTime = db.Column(db.DateTime, default=datetime.utcnow)
    # whenExpire = db.Column(db.DateTime, default=datetime.utcnow)
    # couponTTL = db.Column(db.Integer)
    # comment = db.Column(db.Text)
    # addresslist = db.relationship('RetailerAddress', backref='coupon', lazy='dynamic')
    __tablename__ = "coupon"

    def __repr__(self):
        return '<Coupon {}>'.format(self.couponTitle)
