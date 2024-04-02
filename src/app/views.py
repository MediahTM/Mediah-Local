from flask import Blueprint, render_template, request, jsonify
from app.cache import cache
import requests

views = Blueprint("views", __name__)

@views.context_processor
def globals():
    return {
        "tmdb_apikey": "bfe60268dcb9f6352a6ff6ce40312265" # This can be left public!
    }

@views.route("/")
def index():
    return render_template("pages/index.html")

@views.route("/view")
def view():
    return render_template("pages/view.html")

@views.route("/search")
def search():
    return render_template("pages/search.html")

@views.route("/api/json")
@cache.cached(timeout=500)
def get_json():
    url = request.args.get("url")
    response = requests.get(url)
    if response.status_code in [200, 201]:
        return jsonify(response.json()), 200
    else:
        return jsonify({"error": "Could not resolve the JSON!"})