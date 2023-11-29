from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin

#Initiates the admin side
admin = Admin()

Base = declarative_base()
metadata = Base.metadata

#Initiates the database
db = SQLAlchemy(metadata=metadata)


class Advisor(db.Model):
    __tablename__ = 'advisors'

    id = db.Column(db.Integer, primary_key=True)
    advisor_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    username = db.Column(db.String, nullable=False)
    specialization = db.Column(db.String, nullable=False)
    phonenumber = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String, nullable=False)

admin.add_view(ModelView(Advisor,db.session))


class Livestock(db.Model):
    __tablename__ = 'livestocks'

    id = db.Column(db.Integer, primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey('farms.id'))
    livestock_type = db.Column(db.String, nullable=False)
    weaning_date = db.Column(db.Date, nullable=False)
    slaughter_date = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    image=db.Column(db.String,nullable=True)
    information = db.Column(db.String, nullable=True, default='Default Information')

    
    

admin.add_view(ModelView(Livestock,db.session))

class Crops (db.Model):
    __tablename__ = 'crops'

    id = db.Column(db.Integer, primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey('farms.id'))
    crop_type = db.Column(db.String, nullable=False)
    planting = db.Column(db.Date, nullable=False)
    weeding = db.Column(db.Date, nullable=False)
    harvest = db.Column(db.Date, nullable=False)
    acreage = db.Column(db.Integer, nullable=False)

admin.add_view(ModelView(Crops,db.session))



class Equipment(db.Model):
    __tablename__ = 'equipments'

    id = db.Column(db.Integer, primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey('farms.id'))
    equipment_type = db.Column(db.String, nullable=False)
    maintenance_schedule = db.Column(db.String, nullable=True)

admin.add_view(ModelView(Equipment,db.session))

class Finance(db.Model):
    __tablename__ = 'finances'

    id = db.Column(db.Integer, primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey('farms.id'))
    income = db.Column(db.Integer, nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    loss = db.Column(db.Integer, nullable=True)

admin.add_view(ModelView(Finance,db.session))

class Labourers(db.Model):
    __tablename__ = 'labours'

    id = db.Column(db.Integer, primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey('farms.id'))
    labourerName = db.Column(db.String, nullable=False)
    work_schedule = db.Column(db.String, nullable=False)

admin.add_view(ModelView(Labourers,db.session)) 

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

admin.add_view(ModelView(Farm,db.session))

class Users(db.Model,UserMixin,Base):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(8),nullable=False)

    advisors = db.relationship("Advisor", backref='users')
    farms = db.relationship("Farm", backref='users')

    def get_id(self):
        return str(self.id)
    
    @property
    def is_active(self):
        return True
    

admin.add_view(ModelView(Users,db.session))


