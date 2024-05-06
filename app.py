from flask import Flask
from api.v1.routes import v1 as v1_blueprint
from api.v2.routes import v2 as v2_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(v1_blueprint, url_prefix='/api/v1')
    app.register_blueprint(v2_blueprint, url_prefix='/api/v2')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
