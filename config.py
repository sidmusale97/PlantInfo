from sqlalchemy.ext.declarative import declarative_base


# Create a base class for declarative models
Base = declarative_base()

class Config(object):
    SQLALCHEMY_ENGINE_OPTIONS = {'pool_recycle' : 280}
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    host = "sidm97.mysql.pythonanywhere-services.com"
    password = "jywmed-2wyjso-pyjZyn"
    username = "sidm97"
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqldb://{username}:{password}@{host}/default'


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///plants.db'
