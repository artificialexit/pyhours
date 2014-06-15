from .plugins import db, admin
from flask.ext.admin.contrib.sqla import ModelView


class Person(db.Model):
    __tablename__ = 'people'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))

admin.add_view(ModelView(Person, db.session))
