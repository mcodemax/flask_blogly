"""Seed file for Users"""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add Users
user1 = User(first_name='Fname1', last_name="Lname1", image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Two_red_dice_01.svg/1200px-Two_red_dice_01.svg.png')
user2 = User(first_name='Fname2', last_name="Lname2")
user3 = User(first_name='Fname3', last_name="Lname3", image_url='https://i.ytimg.com/vi/MPV2METPeJU/maxresdefault.jpg')

# Add new objects to session, so they'll persist
db.session.add(user1)
db.session.add(user2)
db.session.add(user3)

# Commit--otherwise, this never gets saved!
db.session.commit()