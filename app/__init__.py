from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://doca_brasil:DEVroberto1979@127.0.0.1:3306/flask_test'

db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.controllers import default
