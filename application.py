from flask import Flask
from flask_mongoengine import MongoEngine
from subprocess import call
from settings import MONGODB_HOST

db = MongoEngine()


def create_app(**config_overrides):
    app = Flask(__name__)

    # Load config
    app.config.from_pyfile('settings.py')

    # apply overrides for tests
    app.config.update(config_overrides)

    # setup db
    db.init_app(app)

    # import blueprints
    from home.views import home_app
    from bucketlist.views import bucketlist_app
    from app.views import app_app
    from user.views import user_app

    # register blueprints
    app.register_blueprint(home_app)
    app.register_blueprint(bucketlist_app)
    app.register_blueprint(app_app)
    app.register_blueprint(user_app)

    return app


def fixtures(test_db, collection, fixture):
    command = "mongoimport -h %s \
        -d %s \
        -c %s \
        < %s" % (MONGODB_HOST, test_db, collection, fixture)
    call(command, shell=True)
