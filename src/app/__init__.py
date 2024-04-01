from app.views import views
from flask import Flask

app = Flask(__name__, static_folder="public")

app.register_blueprint(views)