import os


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # disable modification tracking feature
    JWT_SECRET_KEY = os.environ.get("SECRET_KEY")
    JSON_SORT_KEYS = False
    ##prevent sorting JSON responses by their keys

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        # the variable name can be any but needs to match
        value = os.environ.get("DATABASE_URI")
        # Raise an error if the database URI is not set
        if not value:
            raise ValueError("DATABASE_URI is not set")
        return value


# Different configurations using class inheritance
class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    TESTING = True


environment = os.environ.get("FLASK_ENV")

# Set the configuration depending on the environment
if environment == "production":
    app_config = ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()