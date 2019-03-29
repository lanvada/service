from app import db
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI

import os.path

db.create_all()