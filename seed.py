from app import *
from datetime import datetime

with app.app_context():
    user_data=[{
  "advisor_id": 2,
  "username": "Dr Skipp",
  "specialization": "Fertilizer specialist",
  "phonenumber": "9578579829",
  "location": "Lakipia"
}, {
  "advisor_id": 3,
  "username": "Dr Esme",
  "specialization": "General specialist",
  "phonenumber": "0586803076",
  "location": "RiftValley"
}, {
  "advisor_id": 7,
  "username": "Basiley Tiley",
  "specialization": "Soil specialist",
  "phonenumber": "5906596801",
  "location": "Nyahururu"
}, {
  "advisor_id": 8,
  "username": "Dr Carl",
  "specialization": "Veterinary",
  "phonenumber": "2204315389",
  "location": "Turkana"
}, {
  "advisor_id": 9,
  "username": "Silvia",
  "specialization": "General specialist",
  "phonenumber": "1009097091",
  "location": "Muranga"
}, {
  "advisor_id": 11,
  "username": "Dr Kathy",
  "specialization": "Fertilizer specialist",
  "phonenumber": "0099914727",
  "location": "Turkana"
}, {
  "advisor_id": 13,
  "username": "Gibbie",
  "specialization": "Veterinary",
  "phonenumber": "1839227737",
  "location": "Narok"
}, {
  "advisor_id": 15,
  "username": "Dr Nata",
  "specialization": "Soil specialist",
  "phonenumber": "1698911033",
  "location": "Mombasa"
}, {
  "advisor_id": 16,
  "username": "Hobard",
  "specialization": "Soil specialist",
  "phonenumber": "5434215117",
  "location": "Muranga"
}, {
  "advisor_id": 17,
  "username": "Zeb",
  "specialization": "Veterinary",
  "phonenumber": "4951093871",
  "location": "Turkana"
}]
# Rows:

# Rows:

# Rows:

    
    

# Create a SQLAlchemy database engine
    
    for user_info in user_data:
        user = Advisor(**user_info)
        db.session.add(user)

    db.session.commit()