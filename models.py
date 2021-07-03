"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model): # usually only run this once after deployment otherwise you'll constantly be recreating data
    """User."""
    __tablename__ = "users"

    def __repr__(self):
        return f"<User id={self.id} first_name={self.first_name} last_name={self.last_name} image_url={self.image_url}>"

    id = db.Column(db.Integer, # int not the same as SQL Integer, the ORM translates etween python and postgreSQL
                    primary_key=True,
                    autoincrement=True)
    
    first_name = db.Column(db.String(50),
                            nullable=False)

    last_name = db.Column(db.String(50)) #maybe null as default?

    image_url = db.Column(db.String(5000),
                            default='https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Question_mark_%28black%29.svg/200px-Question_mark_%28black%29.svg.png')
                            #maybe add a default image