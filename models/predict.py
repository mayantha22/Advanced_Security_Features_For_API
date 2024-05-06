import pickle
import numpy as np
import os

import os
import pickle

def load_model(model_filename):
    dir_path = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(dir_path, model_filename)
    print("Attempting to load model from:", model_path)

    if not os.path.exists(model_path):
        print("Error: Model file not found at:", model_path)
        return None 

    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model


primary_model = load_model('security_model.pkl')
secondary_model = load_model('secondary_model.pkl')

def check_ip_access(lat, lon):
    prediction = primary_model.predict([[lat, lon]])
    return 'Granted' if prediction == 1 else 'Denied'

def enhanced_check_ip_access(lat, lon):
    primary_prediction = primary_model.predict([[lat, lon]])
    secondary_prediction = secondary_model.predict([[lat, lon]])

    if lat < -90 or lat > 90 or lon < -180 or lon > 180:
        return 'Denied' 

    if primary_prediction == 1 and secondary_prediction == 1:
        return 'Granted'
    else:
        return 'Denied'

def load_geofence():
    return (40.712776, -74.005974, 50) 

def check_geofence(lat, lon, geofence):
    center_lat, center_lon, radius = geofence
    distance = np.sqrt((lat - center_lat)**2 + (lon - center_lon)**2)
    return distance <= radius

def super_enhanced_check_ip_access(lat, lon):
    if check_geofence(lat, lon, load_geofence()):
        return 'Denied' 
    return enhanced_check_ip_access(lat, lon)
