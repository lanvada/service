from app import db
import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True, unique = True, nullable = False)
    email = db.Column(db.String(120), index = True, unique = True, nullable = False)
    psw = db.Column(db.String(120), nullable = False)
    photos = db.relationship('Photo', backref = 'author', lazy = 'dynamic')

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)  # python 3
    
    def __repr__(self):
        return '<User %r>' % (self.name)

class Photo(db.Model):
    __tablename__ = 'photos'
    id = db.Column(db.Integer, primary_key = True)
    update_time = db.Column(db.DateTime, default = '0')
    photo_path = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), index = True, nullable = False)

    def __repr__(self):
        return '<Photo %r>' % (self.photo_path)