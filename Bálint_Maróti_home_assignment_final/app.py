from flask import Flask, request, jsonify, abort, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
from model import db, URL
import os
from urlshortener import URLShortener

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///url_shortener.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'  

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "URL Shortener API"
    },
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

url_shortener = URLShortener()



@app.route('/shorten', methods=['POST'])
def api_shorten_url():
    return url_shortener.shorten_url(request)


@app.route('/<shortcode>', methods=['GET'])
def api_redirect_url(shortcode):
   return url_shortener.redirect_url(shortcode)


@app.route('/<shortcode>/stats', methods=['GET'])
def api_get_stats(shortcode):
    return url_shortener.get_stats(shortcode)


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)