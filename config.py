class Config(object):
    pass
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI= 'sqlite:///database.db'
    UPLOAD_FOLDER = './static/csvfile'
    SECRET_KEY = '880ce5bcb46bce4e6a264499a754d684'
    UPLOADS_DEFAULT_DEST = './static/xlsfile'