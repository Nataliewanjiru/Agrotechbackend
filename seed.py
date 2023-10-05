from app import *
from datetime import datetime

with app.app_context():
    user_data=[{
  "farm_id": 11,
  "labourerName": "Sanford Edwicke",
  "work_schedule": "7/1/2023"
}, {
  "farm_id": 16,
  "labourerName": "Rosalind Greves",
  "work_schedule": "10/15/2023"
}, {
  "farm_id": 7,
  "labourerName": "Dani Southerden",
  "work_schedule": "5/28/2024"
}, {
  "farm_id": 18,
  "labourerName": "Vite Swenson",
  "work_schedule": "12/31/2023"
}, {
  "farm_id": 9,
  "labourerName": "Sandor Gerbi",
  "work_schedule": "1/17/2023"
}, {
  "farm_id": 1,
  "labourerName": "Van Watmough",
  "work_schedule": "9/22/2023"
}, {
  "farm_id": 20,
  "labourerName": "Yevette Creese",
  "work_schedule": "4/5/2023"
}, {
  "farm_id": 14,
  "labourerName": "Merrill Mogie",
  "work_schedule": "2/13/2024"
}, {
  "farm_id": 16,
  "labourerName": "Ethelind Gymlett",
  "work_schedule": "5/11/2023"
}, {
  "farm_id": 5,
  "labourerName": "Kamila Walduck",
  "work_schedule": "2/6/2024"
}, {
  "farm_id": 19,
  "labourerName": "Ardis Reynolds",
  "work_schedule": "11/22/2023"
}, {
  "farm_id": 18,
  "labourerName": "Lanna Sinnett",
  "work_schedule": "5/31/2024"
}, {
  "farm_id": 12,
  "labourerName": "Ange Whiteway",
  "work_schedule": "10/13/2023"
}, {
  "farm_id": 7,
  "labourerName": "Hesther Hedman",
  "work_schedule": "8/8/2023"
}, {
  "farm_id": 21,
  "labourerName": "Mahmud Papierz",
  "work_schedule": "2/14/2024"
}, {
  "farm_id": 2,
  "labourerName": "Taite Fochs",
  "work_schedule": "8/10/2023"
}, {
  "farm_id": 6,
  "labourerName": "Marie-ann Linster",
  "work_schedule": "4/30/2023"
}, {
  "farm_id": 9,
  "labourerName": "Welbie Bullen",
  "work_schedule": "6/3/2024"
}, {
  "farm_id": 2,
  "labourerName": "Pren Wedgwood",
  "work_schedule": "12/24/2023"
}, {
  "farm_id": 3,
  "labourerName": "Leif Pillman",
  "work_schedule": "12/14/2023"
}, {
  "farm_id": 19,
  "labourerName": "Leo Mulroy",
  "work_schedule": "10/30/2023"
}, {
  "farm_id": 10,
  "labourerName": "Giusto Hubner",
  "work_schedule": "5/13/2024"
}, {
  "farm_id": 19,
  "labourerName": "Vivi Damrel",
  "work_schedule": "1/9/2024"
}, {
  "farm_id": 3,
  "labourerName": "Palm Stoneham",
  "work_schedule": "1/20/2023"
}, {
  "farm_id": 19,
  "labourerName": "Reeta Torald",
  "work_schedule": "5/28/2023"
}, {
  "farm_id": 2,
  "labourerName": "Blinny Hartfleet",
  "work_schedule": "1/15/2023"
}, {
  "farm_id": 18,
  "labourerName": "Melicent O'Finan",
  "work_schedule": "2/27/2024"
}, {
  "farm_id": 5,
  "labourerName": "Sax Gilstin",
  "work_schedule": "4/14/2023"
}, {
  "farm_id": 11,
  "labourerName": "Almeria Eassom",
  "work_schedule": "12/2/2023"
}, {
  "farm_id": 17,
  "labourerName": "Leighton Kristof",
  "work_schedule": "4/19/2024"
}, {
  "farm_id": 3,
  "labourerName": "Hilarius Hymor",
  "work_schedule": "3/3/2024"
}, {
  "farm_id": 3,
  "labourerName": "Yale Yedy",
  "work_schedule": "12/25/2022"
}, {
  "farm_id": 13,
  "labourerName": "Candide Alenichev",
  "work_schedule": "12/24/2022"
}, {
  "farm_id": 11,
  "labourerName": "Cooper Dalley",
  "work_schedule": "12/5/2023"
}, {
  "farm_id": 4,
  "labourerName": "Prudy Maclaine",
  "work_schedule": "6/26/2023"
}, {
  "farm_id": 20,
  "labourerName": "Eb Mellody",
  "work_schedule": "4/4/2023"
}, {
  "farm_id": 17,
  "labourerName": "Janet Kubiczek",
  "work_schedule": "8/13/2023"
}, {
  "farm_id": 9,
  "labourerName": "Romonda Searston",
  "work_schedule": "3/16/2023"
}, {
  "farm_id": 9,
  "labourerName": "Nanci Wardroper",
  "work_schedule": "10/11/2022"
}, {
  "farm_id": 5,
  "labourerName": "Gaven O'Flaverty",
  "work_schedule": "4/8/2023"
}, {
  "farm_id": 15,
  "labourerName": "Ilario Attewill",
  "work_schedule": "9/1/2023"
}, {
  "farm_id": 7,
  "labourerName": "Dennie Millins",
  "work_schedule": "4/22/2023"
}, {
  "farm_id": 4,
  "labourerName": "Evelina Damp",
  "work_schedule": "1/14/2023"
}, {
  "farm_id": 6,
  "labourerName": "Waylen Rollings",
  "work_schedule": "12/28/2022"
}, {
  "farm_id": 13,
  "labourerName": "Harmony Tassell",
  "work_schedule": "4/20/2024"
}, {
  "farm_id": 8,
  "labourerName": "Elfrieda Jandak",
  "work_schedule": "10/29/2022"
}, {
  "farm_id": 19,
  "labourerName": "Rebeka Cullotey",
  "work_schedule": "12/29/2023"
}, {
  "farm_id": 6,
  "labourerName": "Dunc Warner",
  "work_schedule": "2/13/2024"
}, {
  "farm_id": 10,
  "labourerName": "Sara-ann Stiebler",
  "work_schedule": "3/7/2024"
}, {
  "farm_id": 4,
  "labourerName": "Augustus Leslie",
  "work_schedule": "1/16/2023"
}, {
  "farm_id": 6,
  "labourerName": "Elsy Partrick",
  "work_schedule": "2/17/2023"
}, {
  "farm_id": 10,
  "labourerName": "Farra Monan",
  "work_schedule": "7/26/2023"
}, {
  "farm_id": 3,
  "labourerName": "Madelle Thomassen",
  "work_schedule": "11/11/2023"
}, {
  "farm_id": 12,
  "labourerName": "Dannie Ruilton",
  "work_schedule": "10/31/2023"
}, {
  "farm_id": 19,
  "labourerName": "Farlee Sneden",
  "work_schedule": "3/6/2024"
}, {
  "farm_id": 11,
  "labourerName": "Nicola Drinkale",
  "work_schedule": "3/25/2024"
}, {
  "farm_id": 15,
  "labourerName": "Doyle Hames",
  "work_schedule": "11/23/2022"
}, {
  "farm_id": 17,
  "labourerName": "Delcine Mager",
  "work_schedule": "1/10/2024"
}, {
  "farm_id": 18,
  "labourerName": "Lucille Grigore",
  "work_schedule": "2/28/2023"
}, {
  "farm_id": 2,
  "labourerName": "Sybilla Blethin",
  "work_schedule": "4/3/2024"
}, {
  "farm_id": 18,
  "labourerName": "Renae Semered",
  "work_schedule": "3/19/2023"
}, {
  "farm_id": 15,
  "labourerName": "Jodi Obin",
  "work_schedule": "2/12/2023"
}, {
  "farm_id": 5,
  "labourerName": "Hendrika Bruyns",
  "work_schedule": "3/13/2023"
}, {
  "farm_id": 19,
  "labourerName": "Gene Temprell",
  "work_schedule": "11/10/2023"
}, {
  "farm_id": 18,
  "labourerName": "Perry Seaman",
  "work_schedule": "5/31/2024"
}, {
  "farm_id": 9,
  "labourerName": "Darby Hatherley",
  "work_schedule": "10/2/2023"
}, {
  "farm_id": 8,
  "labourerName": "Cherice Gravell",
  "work_schedule": "6/3/2023"
}, {
  "farm_id": 20,
  "labourerName": "Idalia Nathon",
  "work_schedule": "4/26/2024"
}, {
  "farm_id": 3,
  "labourerName": "Tani Hanhard",
  "work_schedule": "1/11/2023"
}, {
  "farm_id": 13,
  "labourerName": "Regan Ambrosoli",
  "work_schedule": "11/25/2022"
}, {
  "farm_id": 3,
  "labourerName": "Kaja Fewell",
  "work_schedule": "6/30/2023"
}, {
  "farm_id": 4,
  "labourerName": "Sabina Walkington",
  "work_schedule": "11/9/2023"
}, {
  "farm_id": 6,
  "labourerName": "Gibb Rogez",
  "work_schedule": "3/31/2023"
}, {
  "farm_id": 9,
  "labourerName": "Kaye Ralph",
  "work_schedule": "10/5/2023"
}, {
  "farm_id": 5,
  "labourerName": "Selle Clemont",
  "work_schedule": "12/18/2022"
}, {
  "farm_id": 5,
  "labourerName": "Ermina Makey",
  "work_schedule": "5/29/2023"
}, {
  "farm_id": 5,
  "labourerName": "Ab Furst",
  "work_schedule": "1/6/2024"
}, {
  "farm_id": 16,
  "labourerName": "Drusilla MacNamee",
  "work_schedule": "9/2/2023"
}, {
  "farm_id": 14,
  "labourerName": "Mitch Biffen",
  "work_schedule": "8/3/2023"
}, {
  "farm_id": 18,
  "labourerName": "Cletus Sankey",
  "work_schedule": "5/6/2024"
}, {
  "farm_id": 3,
  "labourerName": "Florentia Tal",
  "work_schedule": "2/26/2023"
}, {
  "farm_id": 19,
  "labourerName": "Hyacinth Skill",
  "work_schedule": "10/19/2023"
}, {
  "farm_id": 7,
  "labourerName": "Ronnie Hatliffe",
  "work_schedule": "3/12/2024"
}, {
  "farm_id": 10,
  "labourerName": "Rosalia Saltwell",
  "work_schedule": "4/30/2024"
}, {
  "farm_id": 4,
  "labourerName": "Sharon Carette",
  "work_schedule": "3/15/2024"
}, {
  "farm_id": 21,
  "labourerName": "Delainey Crowth",
  "work_schedule": "11/6/2023"
}, {
  "farm_id": 18,
  "labourerName": "Moselle Johns",
  "work_schedule": "2/25/2024"
}, {
  "farm_id": 10,
  "labourerName": "Dionysus Peile",
  "work_schedule": "3/31/2024"
}, {
  "farm_id": 17,
  "labourerName": "Carmine Warkup",
  "work_schedule": "11/4/2022"
}, {
  "farm_id": 18,
  "labourerName": "Noach Coney",
  "work_schedule": "5/26/2023"
}, {
  "farm_id": 14,
  "labourerName": "Aloisia D'Hooge",
  "work_schedule": "11/8/2023"
}, {
  "farm_id": 11,
  "labourerName": "Herschel Keeney",
  "work_schedule": "7/12/2023"
}, {
  "farm_id": 15,
  "labourerName": "Edyth Smallman",
  "work_schedule": "1/13/2023"
}, {
  "farm_id": 11,
  "labourerName": "Fernando Stoney",
  "work_schedule": "11/12/2023"
}, {
  "farm_id": 6,
  "labourerName": "Beatriz Moehler",
  "work_schedule": "11/27/2022"
}, {
  "farm_id": 14,
  "labourerName": "Brant Seggie",
  "work_schedule": "2/16/2024"
}, {
  "farm_id": 19,
  "labourerName": "Arnold Burgin",
  "work_schedule": "6/2/2023"
}, {
  "farm_id": 6,
  "labourerName": "Nevins Smee",
  "work_schedule": "9/30/2023"
}, {
  "farm_id": 9,
  "labourerName": "Gabie Copestake",
  "work_schedule": "9/19/2023"
}, {
  "farm_id": 9,
  "labourerName": "Danyelle Eburne",
  "work_schedule": "10/25/2023"
}]

# Rows:

# Rows:

    for item in user_data:
        item["work_schedule"] = datetime.strptime(item["work_schedule"], "%m/%d/%Y")

# Create a SQLAlchemy database engine
    
    for user_info in user_data:
        user = Labourers(**user_info)
        db.session.add(user)

    db.session.commit()