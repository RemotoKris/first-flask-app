import os
basedir = os.path.abspath(os.path.dirname(_file_))


class config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really needs-to-be-changed'


class ProductionConfig(Config):
    DEBUG = False 



class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG: False



class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
