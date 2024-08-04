# app/models.py
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy
from flask import app

db = SQLAlchemy()

class PlantInfo(db.Model):
    __tablename__ = 'plants'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    careInstructions = Column(String)
    sensorId = Column(Integer, index=True)

    def to_dict(self):
      return {
        'id': self.id,
        'name': self.name,
        'careInstructions': self.careInstructions,
        'sensorId': self.sensorId
    }