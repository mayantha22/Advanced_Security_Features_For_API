from flask import Blueprint, request, jsonify
from models.predict import check_ip_access

from flask import Blueprint

v1 = Blueprint('v1', __name__)

@v1.route('/')
def index():
    return "API Version 1 Home"

@v1.route('/check_access', methods=['POST'])
def check_access():
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    if latitude is None or longitude is None:
        return jsonify({'error': 'Missing latitude or longitude'}), 400
    access = check_ip_access(latitude, longitude)
    return jsonify({'access': access})
