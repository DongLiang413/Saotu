# -*- encoding=UTF-8 -*-

from saotu import db
import random
#
# class Image(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     url = db.Column(db.String(512))
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     created_date = db.Column(db.DateTime)
#
#     def __int__(self, username, password):
#         self.username = username
#         self.password = password
#         self.head_url = 'C:\Users\Dong\Desktop\photos' + str(random.randint(5))



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(32))
    head_url = db.Column(db.String(256))

    def __int__(self, username, password):
        self.username = username
        self.password = password
        self.head_url = 'C:\Users\Dong\Desktop\photos'

    def __repr__(self):
        return '<User %d %s>' % (self.id, self.username)
