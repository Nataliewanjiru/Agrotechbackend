from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password=db.Column(db.String, nullable=False)
    role= db.Column(db.String, nullable=False)

    advisors = db.relationship("Advisor", backref='users')
    farms = db.relationship("Farm", backref='users')


class Farm(db.Model):
    __tablename__ = 'farms'

    id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    farm_name = db.Column(db.String, nullable=False)

    livestocks = db.relationship("Livestock", backref='farms')
    crops = db.relationship("Crops", backref='farms')
    equipments = db.relationship("Equipment", backref='farms')
    finances = db.relationship("Finance", backref='farms')
    labourers = db.relationship("Labourers", backref='farms')



class Livestock(db.Model):
    __tablename__ = 'livestocks'

    id = db.Column(db.Integer, primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey('farms.id'))
    livestock_type = db.Column(db.String, nullable= False)
    weaning_date = db.Column(db.Date, nullable=False)
    slaughter_date = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
   
   


class Crops (db.Model):
    __tablename__ = 'crops'

    id = db.Column(db.Integer, primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey('farms.id'))
    crop_type = db.Column(db.String, nullable=False)
    planting = db.Column(db.Date, nullable=False)
    weeding = db.Column(db.Date, nullable=False)
    harvest = db.Column(db.Date, nullable=False)
    acreage = db.Column(db.Date, nullable=False)
   
   


class Equipment(db.Model):
    __tablename__ = 'equipments'

    id = db.Column(db.Integer, primary_key = True)
    farm_id = db.Column(db.Integer, db.ForeignKey('farms.id'))
    equipment_type = db.Column(db.String, nullable=False)
    maintenance_schedule = db.Column(db.Date, nullable=True)
   
   

class Finance(db.Model):
    __tablename__ = 'finances'

    id = db.Column(db.Integer, primary_key = True)
    farm_id = db.Column(db.Integer, db.ForeignKey('farms.id'))
    income = db.Column(db.Integer, nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    loss = db.Column(db.Integer, nullable=True)
   
   

class Labourers(db.Model):
    __tablename__ = 'labours'

    id = db.Column(db.Integer,primary_key=True )
    farm_id = db.Column(db.Integer, db.ForeignKey('farms.id'))
    labour_allocation = db.Column(db.String, nullable=False)
    work_schedule = db.Column(db.String, nullable=False)
   
   
   

class Advisor(db.Model):
    __tablename__ = 'advisors'

    id = db.Column(db.Integer, primary_key=True)
    advisor_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    username = db.Column(db.String, nullable=False)
    specialization = db.Column(db.String, nullable=False)
    phonenumber = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String, nullable = False)
  
  