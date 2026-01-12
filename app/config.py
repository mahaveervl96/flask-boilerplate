import os

class BaseConfig:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_LEVEL = os.getenv('LOG_LEVEL')

class DevConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False

def get_config():
    env = (os.getenv("FLASK_ENV")).lower()
    if env == "production":
        return ProductionConfig
    
    return DevConfig