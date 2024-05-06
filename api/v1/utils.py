from flask import jsonify

def validate_coordinates(data):
    """ Validates if the provided data dictionary has latitude and longitude keys with valid float values.
    Returns True if valid, False otherwise.
    """
    try:
        lat = float(data['latitude'])
        lon = float(data['longitude'])
        return -90 <= lat <= 90 and -180 <= lon <= 180
    except (ValueError, KeyError, TypeError):
        return False

def validate_ip_address(data):
    """ Validates if the provided data dictionary has a valid IP address in the 'ip' key.
    Returns True if valid, False otherwise.
    """
    import ipaddress
    try:
        ipaddress.ip_address(data['ip'])
        return True
    except ValueError:
        return False

def error_response(message, status_code):
    """ Constructs a JSON error response with a given message and status code.
    """
    response = jsonify({'error': message})
    response.status_code = status_code
    return response

def log_error(message):
    """ Logs an error message to the server's log.
    You might want to integrate with more sophisticated logging infrastructure.
    """
    import logging
    logging.error(message)

def log_info(message):
    """ Logs an informational message to the server's log.
    """
    import logging
    logging.info(message)

