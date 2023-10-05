from app import *
from datetime import datetime

with app.app_context():
    user_data=[{
  "farm_id": 6,
  "income": 47555,
  "budget": 46940,
  "loss": 95387
}, {
  "farm_id": 21,
  "income": 51368,
  "budget": 52166,
  "loss": 80431
}, {
  "farm_id": 19,
  "income": 92056,
  "budget": 83990,
  "loss": 33772
}, {
  "farm_id": 9,
  "income": 79787,
  "budget": 85660,
  "loss": 66617
}, {
  "farm_id": 10,
  "income": 37775,
  "budget": 35626,
  "loss": 56647
}, {
  "farm_id": 9,
  "income": 85236,
  "budget": 56801,
  "loss": 40627
}, {
  "farm_id": 16,
  "income": 95929,
  "budget": 96958,
  "loss": 87421
}, {
  "farm_id": 1,
  "income": 89798,
  "budget": 82889,
  "loss": 80950
}, {
  "farm_id": 12,
  "income": 68819,
  "budget": 35067,
  "loss": 45658
}, {
  "farm_id": 10,
  "income": 91011,
  "budget": 28011,
  "loss": 53049
}, {
  "farm_id": 18,
  "income": 56731,
  "budget": 23768,
  "loss": 51489
}, {
  "farm_id": 19,
  "income": 35713,
  "budget": 26715,
  "loss": 63971
}, {
  "farm_id": 16,
  "income": 70777,
  "budget": 39990,
  "loss": 38297
}, {
  "farm_id": 4,
  "income": 59580,
  "budget": 60053,
  "loss": 54481
}, {
  "farm_id": 2,
  "income": 72297,
  "budget": 97628,
  "loss": 81912
}, {
  "farm_id": 20,
  "income": 90971,
  "budget": 73653,
  "loss": 95416
}, {
  "farm_id": 19,
  "income": 51758,
  "budget": 41655,
  "loss": 79655
}, {
  "farm_id": 10,
  "income": 84813,
  "budget": 78508,
  "loss": 58051
}, {
  "farm_id": 2,
  "income": 23085,
  "budget": 75724,
  "loss": 79549
}, {
  "farm_id": 3,
  "income": 68981,
  "budget": 50815,
  "loss": 50244
}, {
  "farm_id": 10,
  "income": 94762,
  "budget": 22747,
  "loss": 68787
}]
# Rows:

    
    

# Create a SQLAlchemy database engine
    
    for user_info in user_data:
        user = Finance(**user_info)
        db.session.add(user)

    db.session.commit()