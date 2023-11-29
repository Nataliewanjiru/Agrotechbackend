from app import app  # Assuming 'app' is your Flask application instance
from datetime import datetime
from model import * # Assuming 'Farm' is the SQLAlchemy model for farms
from app import db  # Assuming 'db' is your SQLAlchemy instance

with app.app_context():
    user_data=[{
         "farm_id": 1,
        "livestock_type": "Cow",
        "weaning_date": datetime.strptime("2023-11-10", "%Y-%m-%d").date(),  # Convert string to datetime object
        "slaughter_date": datetime.strptime("2024-11-10", "%Y-%m-%d").date(),  # Convert string to datetime object
        "quantity": 30,
        "image":"https://images.unsplash.com/photo-1570042225831-d98fa7577f1e?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "information":"Animals were brought in on 10th November from Kinangop bt Mr James Juma. Currently placed in Shed number 23 From row 27. The cows are Freshian with each producing an average of five litres"
    
}]
# Rows:

    
    

# Create a SQLAlchemy database engine
    
    for user_info in user_data:
        user = Livestock(**user_info)
        db.session.add(user)

    db.session.commit()