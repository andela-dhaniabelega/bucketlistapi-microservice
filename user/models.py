from mongoengine import signals
from application import db


class User(db.Document):
    external_id = db.StringField(db_field="ei")
    first_name = db.StringField(db_field="fn")
    last_name = db.StringField(db_field="ln")
    email = db.StringField(db_field="e")
    password = db.StringField(db_field="p")
    live = db.Boolean(db_field="l", default=True)

    meta = {
        'indexes': [('external_id', 'live')]
    }
