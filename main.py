from flask import Flask, request, jsonify
from service import Service
from flask_cors import CORS
import argparse
from flask import request
from models import db, PlantInfo
from config import DevConfig, ProdConfig

def create_app(env):
    app = Flask(__name__)
    CORS(app)
   
    app.config.from_object(DevConfig)

    service = Service()

    db.init_app(app)

    with app.app_context():
        db.create_all()


    @app.route("/plants", methods=['GET', 'DELETE'])
    def plants():
        if (request.method == "GET"):
            plants = service.get_plants_info()
            if (plants):
                return jsonify([p.to_dict() for p in plants]), 200
            else:
                return "No plants found", 404
        else:
            service.delete()
            return "", 200

    @app.route("/plant/<id>", methods=['GET'])
    def plant(id):
        plant = service.get(id)
        if plant:
            return jsonify(plant.to_dict()), 200
        else:
            return f"No plant found with id: {id}", 404

    @app.route("/plant", methods=['PUT', 'POST'])
    def create_plant():
        data = request.get_json()
        if (request.method == "PUT"):
            plant = service.create(data['name'], data['care'], data['sensor_id'])
            return jsonify(plant.to_dict(), 200)
        else:
            plant = service.update(data)
            return jsonify(plant.to_dict(), 200)
    
    return app

parser = argparse.ArgumentParser()

parser.add_argument('--debug', default=False, type=bool)
parser.add_argument('--port', default=5000, type=int)
parser.add_argument('--env', default="prod", type=str)
args = parser.parse_args()

app = create_app(args.env)

if __name__ == '__main__':  
    app.run(debug=args.debug, port=args.port)

    