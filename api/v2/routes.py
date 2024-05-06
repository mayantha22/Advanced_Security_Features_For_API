from flask import Blueprint, request, jsonify
from models.predict import check_ip_access, enhanced_check_ip_access

v2 = Blueprint('v2', __name__)

@v2.route('/check_access', methods=['POST'])
def check_access():
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    if latitude is None or longitude is None:
        return jsonify({'error': 'Missing latitude or longitude'}), 400
    access = enhanced_check_ip_access(latitude, longitude) 
    return jsonify({'access': access})
