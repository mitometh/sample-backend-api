from flask import Flask
from modules.common.db import db, get_db_uri
import logging

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = get_db_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True  # Enable debug mode

db.init_app(app)

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG if app.debug else logging.INFO)
app.logger.addHandler(handler)

# Import and register the blueprint
from modules.recipe.routes import recipe_api
app.register_blueprint(recipe_api, url_prefix='/recipes')

# Create database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()
