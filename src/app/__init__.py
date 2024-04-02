from app.views import views
from app.cache import cache
from flask import Flask
import requests

app = Flask(__name__, static_folder="public")
cache.init_app(app)

with open("version") as version:
    version = version.read()

web_version = requests.get("https://raw.githubusercontent.com/MediahTM/Mediah-Local/main/src/version").text

if float(version) >= float(web_version):
    app.register_blueprint(views)
else:
    print("Please update your version of Mediah-Local\nVisit 'https://github.com/MediahTM/Mediah-Local' and follow the install instructions")
    exit()