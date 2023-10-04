from faker import Faker
from datetime import datetime
from random import choice, randint
from app.modelodel import User, Farm, Livestock, Crops, Equipment, Finance, Labourers, Advisor
from app.app import app, db

fake = Faker()

# Function to generate random user data


def generate_random_user():
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    password = fake.password()
    role = 'user'

    user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
        role=role
    )

    return user

# Function to generate random farm data


def generate_random_farm(user):
    farm_name = fake.company()

    farm = Farm(
        farmer_id=user.id,
        farm_name=farm_name,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    return farm


# Function to generate random livestock data


def generate_random_livestock(farm):
    livestock_types = ['Cattle', 'Sheep', 'Pig', 'Chicken']
    livestock_type = choice(livestock_types)
    weaning_date = fake.date_between(start_date='-2y', end_date='today')
    slaughter_date = fake.date_between(start_date='-1y', end_date='today')
    quantity = randint(1, 100)

    livestock = Livestock(
        farm_id=farm.id,
        livestock_type=livestock_type,
        weaning_date=weaning_date,
        slaughter_date=slaughter_date,
        quantity=quantity
    )

    return livestock


# Function to generate random crops data


# def generate_random_crops(farm):
#     crop_types = ['Wheat', 'Corn', 'Rice', 'Soybeans']
#     crop_type = choice(crop_types)
#     planting = fake.date_between(start_date='-1y', end_date='today')
#     weeding = fake.date_between(start_date='-6m', end_date='today')
#     harvest = fake.date_between(start_date='-3m', end_date='today')
#     acreage = randint(1, 100)

#     crops = Crops(
#         farm_id=farm.id,
#         crop_type=crop_type,
#         planting=planting,
#         weeding=weeding,
#         harvest=harvest,
#         acreage=acreage
#     )

#     return crops



# Function to generate random equipment data


def generate_random_equipment(farm):
    equipment_types = ['Tractor', 'Plow', 'Harvester', 'Irrigation System']
    equipment_type = choice(equipment_types)
    maintenance_schedule = choice(['Monthly', 'Quarterly', 'Annually'])

    equipment = Equipment(
        farm_id=farm.id,
        equipment_type=equipment_type,
        maintenance_schedule=maintenance_schedule
    )

    return equipment

# # Function to generate random finance data


def generate_random_finance(farm):
    income = randint(1000, 100000)
    budget = randint(800, 90000)
    loss = randint(0, 5000)

    finance = Finance(
        farm_id=farm.id,
        income=income,
        budget=budget,
        loss=loss
    )

    return finance

# # Function to generate random labourers data


# def generate_random_labourers(farm):
#     labour_allocations = ['Harvesting', 'Weeding', 'Planting', 'Fertilizing']
#     work_schedule = choice(['Full-time', 'Part-time'])

#     labourer = Labourers(
#         farm_id=farm.id,
#         labour_allocation=choice(labour_allocations),
#         work_schedule=work_schedule
#     )

#     return labourer

# # Function to generate random advisor data


# def generate_random_advisor(user):
#     advisor = Advisor(
#         advisor_id=user.id,
#         username=fake.user_name(),
#         specialization=choice(['Agriculture', 'Livestock', 'Crop Management']),
#         phonenumber=fake.random_int(min=1000000000, max=9999999999),
#         location=fake.city()
#     )
#     return advisor


if __name__ == '__main__':
    with app.app_context():
        for _ in range(10):
            user = generate_random_user()
            db.session.add(user)
            farm = generate_random_farm(user)
            db.session.add(farm)
            livestock = generate_random_livestock(farm)
            db.session.add(livestock)
            # crops = generate_random_crops(farm)
            # db.session.add(crops)
            equipment = generate_random_equipment(farm)
            db.session.add(equipment)
            finance = generate_random_finance(farm)
            db.session.add(finance)
            # labourer = generate_random_labourers(farm)
            # db.session.add(labourer)
            # advisor = generate_random_advisor(user)
            # db.session.add(advisor)

        db.session.commit()
        print('Random data generation complete.')
