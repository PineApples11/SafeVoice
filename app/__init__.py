from flask import Flask
from .extensions import db
from .config import Config

# Import and register blueprints here
# from .routes import user_bp
# from .routes import report_bp
# from .routes import message_bp

def create_app():
    app =  Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)


    # app.register_blueprint(user_bp, url_prefix='/users')
    # app.register_blueprint(report_bp, url_prefix='/reports')
    # app.register_blueprint(message_bp, url_prefix='/messages')
    
    return app

    

