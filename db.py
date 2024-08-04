# app/crud.py
from models import PlantInfo, db
import json

image_bucket_url = "https://storage.googleapis.com/sid-plants/plant%d.jpg"

def create_plant(name: str, care: str, sensor_id: int):
    try:
        plant = PlantInfo(name=name, careInstructions=care, sensorId=sensor_id)
        db.session.add(plant)
        db.session.commit()
        return plant
    except Exception as e:
        print(f"An error occurred while creating the plant: {e}")

def get_plant(id: int):
    try:
        return db.session.query(PlantInfo).filter(PlantInfo.id == id).first()
    except Exception as e:
        print(f"An error occurred while retrieving the plant: {e}")

def get_plants():
    try:
        print('here')
        return db.session.query(PlantInfo).all()
    except Exception as e:
        print(f"An error occurred while retrieving plants: {e}")

def update_plant(updatedPlant: dict):
    try:
        plant = get_plant(updatedPlant["id"])
        if plant is not None:
            plant.sensorId = updatedPlant["sensorId"]
            plant.careInstructions = updatedPlant["careInstructions"]
            plant.name = updatedPlant["name"]
            db.session.commit()
            print(plant.to_dict())
            return plant
        else:
            print(f"Plant with id {id} not found.")
    except Exception as e:
        print(f"An error occurred while updating the plant: {e}")

def delete_plants():
    try:
        db.session.query(PlantInfo).delete()
        db.session.commit()
    except Exception as e:
        print(f"An error occurred while deleting plants: {e}")

def delete_plant(id):
    try:
        db.session.query(PlantInfo).filter(PlantInfo.id == id).delete()
        db.session.commit()
    except Exception as e:
        print(f"An error occurred while deleting plants: {e}")