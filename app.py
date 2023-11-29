from model import *
from dotenv import load_dotenv
from flask_cors import CORS
from flask import Flask,  render_template, request, jsonify
from sqlalchemy import or_
import datetime,os
from flask_jwt_extended import JWTManager, create_access_token, jwt_required,get_jwt_identity
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from datetime import timedelta


app = Flask(__name__)


# Configure your Flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key_here'
# Other app configurations...

# Initialize extensions
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)
jwt = JWTManager(app)
CORS(app)

admin.init_app(app)
db.init_app(app)




# db = SQLAlchemy(app)#main page route
@app.route('/')
def index():
    return "Welcome to our API"

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


#Route for register
@app.route('/usersignup', methods=['POST'])
def register_user():
  try:
       data = request.get_json() 
       if not data:
           return jsonify({'error': 'Invalid JSON data'}), 400
       
       username = data.get('username')
       first_name = data.get('first_name')
       last_name = data.get('last_name')
       email = data.get('email')
       password = data.get('password')
   
       # Check if the username is already taken
       existing_user = Users.query.filter_by(username=username).first()
       if existing_user:
           response = {'message': 'Username is already taken. Please choose another one.'}
           return jsonify(response), 400
       # Create a new user
       hashed_password = generate_password_hash(password, method='sha256')
       new_user = Users(first_name=first_name,last_name=last_name,username=username,email=email, password=hashed_password, role="User")
   
       # Add the new user to the database
       db.session.add(new_user)
       db.session.commit()
   
       response = {'message': 'Registration successful!'}
       return jsonify(response)
  except Exception as e:
    print(e)
    response = {"status": False,"msg": str(e)}
    return jsonify(response), 500
  


#Routes for login
@app.route('/userlogin', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not ((username or email) and password):
      return jsonify({'error': 'Invalid JSON data'}), 400  

    user = Users.query.filter(or_(Users.username == username, Users.email == email)).first()

    if user and check_password_hash(user.password, password):
        login_user(user)
        access_token = create_access_token(identity=user.id, expires_delta=timedelta(hours=24))
        return jsonify({'access_token': access_token,
                        "userid":current_user.id}), 200
    else:
        return jsonify({'message': 'Invalid username,email or password'}), 401



# Route for profile
@app.route('/userprofile', methods=['GET'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()  
    user = Users.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    fullname = user.first_name + user.last_name

    return jsonify({
        "name": fullname,
        "username": user.username,
        "email": user.email
    })



# Route for logout
@app.route('/userlogout', methods=['GET'])
@jwt_required()
def logout():
    logout_user()
    return 'Logged out successfully'

@app.route('/deleteaccount', methods=['GET'])
@jwt_required()
def delete_account():
    user_id = get_jwt_identity() 

    if user_id:
        # Query the database to find the user
        user = Users.query.get(user_id)

        if user:
            try:
                # Delete the user from the database
                db.session.delete(user)
                db.session.commit()

                return 'Your account has been deleted.'
            except Exception as e:
                db.session.rollback()  
                return jsonify({'error': 'An error occurred while deleting the user.'}), 500
        else:
            return 'User not found.'
    else:
        return 'Invalid or expired token.'



################################################################
# GET AND POST methods for the farm and user information
@app.route('/farms')
def get_all_farms():
    farms = Farm.query.all()
    farm_list = []
    for farm in farms:
        farm_data = {
            'id': farm.id,
            'farmer_id': farm.farmer_id,
            'farm_name': farm.farm_name
        }
        farm_list.append(farm_data)

    return jsonify(farm_list)



@app.route('/farm', methods=['POST'])
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
            'quantity': livestock.quantity,
            "image":livestock.image,
            "details":livestock.information
        }

        livestock_list.append(livestock_data)
    return jsonify(livestock_list)

from flask import jsonify, request
from datetime import datetime

@app.route('/livestock', methods=['POST'])
def create_livestock():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid Data"}), 400
    
    farm_id = data.get('farm_id')
    livestock_type = data.get('livestock_type')
    weaning_date_str = data.get('weaning_date')
    slaughter_date_str = data.get('slaughter_date')
    quantity = data.get('quantity')
    image = data.get("image")
    information = data.get("information")

    if not farm_id or not livestock_type or not weaning_date_str or not slaughter_date_str or not quantity:
        return jsonify({"error": "Missing required field"}), 40
    
    weaning_object = datetime.strptime(weaning_date_str, '%Y-%m-%d').date()
    slaughter_object = datetime.strptime(slaughter_date_str, '%Y-%m-%d').date()

    new_livestock = Livestock(
        farm_id=farm_id,
        livestock_type=livestock_type,
        weaning_date=weaning_object,
        slaughter_date= slaughter_object,
        quantity=quantity,
        image=image,
        information=information
    )

    db.session.add(new_livestock)
    db.session.commit()

    return jsonify({'message': "Livestock added successfully"}), 201

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
def get_crops_by_farm_id():
    crops = Crops.query.filter_by().all()

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


@app.route('/advisors')
def get_advisors():
    advisors = Advisor.query.all()
    advisor_list = []

    for advisor in advisors:
        advisor_data = {
            'id': advisor.id,
            'name': advisor.username,
            'field': advisor.specialization,
            'phone': advisor.phonenumber,
            'location':advisor.location
        }
        advisor_list.append(advisor_data)

    return jsonify(advisor_list)



if __name__ == '__main__':
    app.run(debug=True, port=5910)
