import os

from inspira.config import Config

config = Config()

config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "my-dummy-secret-key")

uri = os.environ.get("DATABASE_URL", "no-db")

if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

config['SQLALCHEMY_DATABASE_URI'] = uri
