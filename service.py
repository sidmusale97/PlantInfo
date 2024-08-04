from db import get_plants, get_plant, create_plant, delete_plants, update_plant

class Service:

    def get_plants_info(self):
        return get_plants()
    
    def update(self, updatedPlant):
        return update_plant(updatedPlant)

    def create(self, name, care, sensor_id):
        print("here")
        return create_plant(name=name, care=care, sensor_id=sensor_id)
    
    def get(self, id):
        return get_plant(id)
    
    def delete(self):
        return delete_plants()