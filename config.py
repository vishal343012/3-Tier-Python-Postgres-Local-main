import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://apppppwedd-server:Password123##@localhost/apppppwedd-database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

