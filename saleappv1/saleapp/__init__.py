from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_login import LoginManager
import cloudinary
from flask_babelex import Babel


app = Flask(__name__)
app.secret_key = '$%^*&())(*&%^%4678675446&#%$%^&&*^$&%&*^&^'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/it01saledbv1?charset=utf8mb4' % quote('Admin@123')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
cloudinary.config(cloud_name='dtlqyvkvu', api_key='654129736974748', api_secret='CPi-rz8Bl-s9WY9fV-39VhOxRAQ')

db = SQLAlchemy(app=app)

login = LoginManager(app=app)


babel = Babel(app=app)

@babel.localeselector
def load_locale():
    return 'vi'