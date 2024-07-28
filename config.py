import os

class Config:
    basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'instance'))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'community_pulse.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False