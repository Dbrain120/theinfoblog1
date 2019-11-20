from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail

from config import Config


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
mail = Mail(app)

from myproject import routes



# def create_app(config_class=Config):
#     app = Flask(__name__)
#     app.config.from_object(Config)

#     db.init_app(app)
#     migrate.init_app(app)
#     bcrypt.init_app(app)
#     login_manager.init_app(app)
#     mail.init_app(app)

#     from myproject.users.routes import users
#     from myproject.posts.routes import posts
#     from myproject.main.routes import main
#     app.register_blueprint(users)
#     app.register_blueprint(posts)
#     app.register_blueprint(main)


#     return app

