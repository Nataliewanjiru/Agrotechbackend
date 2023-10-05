import re
from model import *
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, render_template, request, jsonify
import os



os.environ['FLASK_APP'] = 'app.py'


load_dotenv()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

migrate = Migrate(app, db)

db.init_app(app)

# db = SQLAlchemy(app)

email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'


@app.route('/')
def index():
    return "Welcome to our API"


# GET and POST methods for the user info
@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    user_list = []

    for user in users:
        user_data = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'role': user.role
        }
        user_list.append(user_data)

    return jsonify(user_list)


@app.route('/register', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid JSON data'}), 400

    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role')

    if not first_name or not last_name or not email or not password or not role:
        return jsonify({'error': 'Missing required fields'}), 400

    # Hash the password before storing it in the database
    password_hash = generate_password_hash(password, method='sha256')

    new_user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password_hash,  # Store the hashed password
        role=role
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password_hash, password):
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Login failed"})

################################################################
# GET AND POST methods for the farm and user information
@app.route('/farms', methods=['GET'])
def get_all_farms():
    farms = Farm.query.all()
    farm_list = []

    for farm in farms:
        farm_data = {
            'id': farm.id,
            'farmer_id': farm.farmer_id,
            'farm_name': farm.farm_name,
            'created_at': farm.created_at.strftime('%Y-%m-%d %H:%M:%S')if farm.created_at else None,
            'updated_at': farm.updated_at.strftime('%Y-%m-%d %H:%M:%S')if farm.updated_at else None
        }
        farm_list.append(farm_data)

    return jsonify(farm_list)


@app.route('/farms', methods=['POST'])
def create_farm():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid JSON data'}), 400

    farmer_id = data.get('farmer_id')
    farm_name = data.get('farm_name')

    if not farmer_id or not farm_name:
        return jsonify({'error': 'Missing required fields'}), 400

    new_farm = Farm(
        farmer_id=farmer_id,
        farm_name=farm_name
    )

    db.session.add(new_farm)
    db.session.commit()

    return jsonify({'message': 'Farm created successfully'}), 201


################################################################
# GET AND POST methods for livestock info
@app.route('/livestocks', methods=['GET'])
def get_livestock():
    livestocks = Livestock.query.all()
    livestock_list = []

    for livestock in livestocks:
        livestock_data = {
            'id': livestock.id,
            'farm_id': livestock.farm_id,
            'livestock_type': livestock.livestock_type,
            'weaning_date': livestock.weaning_date,
            'slaughter_date': livestock.slaughter_date,
            'quantity': livestock.quantity
        }

        livestock_list.append(livestock_data)
    return jsonify(livestock_list)


@app.route('/livestocks', methods=['POST'])
def create_livestock():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid Data"})

    farm_id = data.get('farm_id')
    livestock_type = data.get('livestock_type')
    weaning_date = data.get('weaning_date')
    slaughter_date = data.get('slaughter_date')
    quantity = data.get('quantity')

    if not farm_id or not livestock_type or not weaning_date or not slaughter_date or not quantity:
        return jsonify({"error": "Missing required field"})

    new_livestock = Livestock(
        farm_id=farm_id,
        livestock_type=livestock_type,
        weaning_date=weaning_date,
        slaughter_date=slaughter_date,
        quantity=quantity
    )

    db.session.add(new_livestock)
    db.session.commit()

    return jsonify({'messsage': "Livestock added successfully"})


################################################################
# GET AND PUT methods for the equipment info
@app.route('/equipments', methods=['GET'])
def get_equipment():
    equipments = Equipment.query.all()
    equipment_list = []

    for equipment in equipments:
        equipment_data = {
            'farm_id': equipment.farm_id,
            'equipment_type': equipment.equipment_type,
            'maintenance_schedule': equipment.maintenance_schedule
        }
        equipment_list.append(equipment_data)
    return jsonify(equipment_list)


@app.route('/equipments', methods=['POST'])
def create_equipment():
    data = request.get_json()
    if not data:
        return jsonify({'error': "Invalid data"})

    farm_id = data.get('farm_id')
    equipment_type = data.get('equipment_type')
    maintenance_schedule = data.get('maintenance_schedule')

    if not farm_id or not equipment_type or not maintenance_schedule:
        return jsonify({'error': "Missing fields"})

    new_equipment = Equipment(
        farm_id=farm_id,
        equipment_type=equipment_type,
        maintenance_schedule=maintenance_schedule
    )
    db.session.add(new_equipment)
    db.session.commit()

    return jsonify({'message': "Equipment added successfully"})


################################################################
# GET AND PUT methods for finance info
@app.route('/finances', methods=['GET'])
def get_all_finances():
    finances = Finance.query.all()
    finance_list = []

    for finance in finances:
        finance_data = {
            'id': finance.id,
            'farm_id': finance.farm_id,
            'income': finance.income,
            'budget': finance.budget,
            'loss': finance.loss
        }
        finance_list.append(finance_data)

    return jsonify(finance_list)


@app.route('/finances', methods=['POST'])
def create_finance():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid JSON data'}), 400

    farm_id = data.get('farm_id')
    income = data.get('income')
    budget = data.get('budget')
    loss = data.get('loss')

    if not farm_id or not income or not budget:
        return jsonify({'error': 'Missing required fields'}), 400

    new_finance = Finance(
        farm_id=farm_id,
        income=income,
        budget=budget,
        loss=loss
    )

    db.session.add(new_finance)
    db.session.commit()

    return jsonify({'message': 'Finance record created successfully'}), 201


@app.route('/crops', methods=['GET'])
def get_crops_by_farm_id(farm_id):
    crops = Crops.query.filter_by(farm_id=farm_id).all()

    crop_list = []
    for crop in crops:
        crop_data = {
            'id': crop.id,
            'farm_id': crop.farm_id,
            'crop_type': crop.crop_type,
            'planting': crop.planting.strftime("%Y-%m-%d"),  
            'weeding': crop.weeding.strftime("%Y-%m-%d"),    
            'harvest': crop.harvest.strftime("%Y-%m-%d"),    
            'acreage': crop.acreage
        }
        crop_list.append(crop_data)

    return jsonify(crop_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
