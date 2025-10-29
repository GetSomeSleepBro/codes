import os


class Config:
    def __call__(self):
        return self

    def __init__(self):
        # Base defaults; DB URI finalized in create_app to use app.instance_path
        self.SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
