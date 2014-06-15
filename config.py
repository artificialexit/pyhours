class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/pyhours.db'


class ProductionConfig(Config):
    SECRET_KEY = "<change me>"


class DevelopmentConfig(Config):
    SECRET_KEY = "dev_key"
    DEBUG = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    TESTING = True

config_map = {
    'dev': DevelopmentConfig,
    'test': TestingConfig
}

default_config = ProductionConfig
