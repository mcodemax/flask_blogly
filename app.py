"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:myPassword@localhost:5433/blogly' #@ people looking at this code; you may need to change on your own computer for code to work
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True #prints in ipython the queries being run

app.config["SECRET_KEY"] = "maxcode1"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


connect_db(app)
db.create_all()

@app.route('/')
def show_title_get():

    #psql query the db and get a list of users


    return redirect("/users")



@app.route('/users')
def list_users():
    """Show all users.

    Make these links to view the detail page for the user.

    Have a link here to the add-user form.
    """
    
    users = User.query.all()

    
    
    return render_template("userlist.html", users=users)
#in ipython do db.session.execute('SELECt*from blah') and set to 
# a vars and put in a list to see the data


@app.route('/users/new')#method is get by default?
def add_user_form():
    """Show an add form for users"""


    return render_template('makeuser.html')

    

@app.route('/users/new', methods=["POST"])
def post_user():
    """Process the add form, adding a new user and going back to /users"""
    
    #get user data from post request from HTML form; ref forex project for refresher
    #user = User(name='input', first_name='see notes from above getting user data')
            #make sure to seperate logic n stuff above
    #then db.session.add(the above stuff)
    #then db.session.commit()

    #notes: you don't have to re add() a whole user once you commit it
        #you only have to commit() changes; you can call upon the user later again

    
    first_name = request.form.get("first-name")
    last_name = request.form.get("last-name")
    imglink = request.form.get("imglink")

    
    #seperate web interface from logic
    if '' in [first_name]:
        return redirect("/users/new")

    if '' in [imglink]:
        user = User(first_name=first_name, last_name=last_name)
    else:
        user = User(first_name=first_name, last_name=last_name, image_url=imglink)

    
    db.session.add(user)
    db.session.commit()

    return redirect("/users")



@app.route('/users/<int:user_num>', methods=["GET"])
def show_question(user_num):
    """Show information about the given user.

    Have a button to get to their edit page, and to delete the user.
    """
        
    user = User.query.get_or_404(user_num)
    
    return render_template('details.html',user=user)



@app.route('/users/<int:user_num>/edit', methods=["GET"])
def edit_user(user_num):
    """
    Show the edit page for a user.

    Have a cancel button that returns to the detail page for 
    a user, and a save button that updates the user.
    """
    # https://stackoverflow.com/questions/547821/two-submit-buttons-in-one-form

    user = User.query.get(user_num)

    return render_template('edit.html',user_num=user_num, user=user)


@app.route('/users/<int:user_num>/edit', methods=["POST"])
def store_edits(user_num):
    """
    Process the edit form, returning the user to the /users page.
    """
    user = User.query.get_or_404(user_num)
    
    first_name = request.form.get("first-name")
    last_name = request.form.get("last-name")
    imglink = request.form.get("imglink")

    if len(first_name) > 50 or len(last_name) > 50 or len(imglink) > 5000:
        redir_txt = '/users/' + str(user_num) + "/edit"
        return redirect(redir_txt)

    if '' not in [first_name]:
        user.first_name = first_name

    if '' not in [last_name]:
        user.last_name = last_name

    if '' not in [imglink]:
        user.image_url = imglink   
    
    db.session.commit()


    
    return redirect('/users')



@app.route('/users/<int:user_num>/delete', methods=["POST"])
def delete_user(user_num):
    """
    Process the edit form, returning the user to the /users page.
    """

    # return the user to the /users page.
    user = User.query.get_or_404(user_num)

    db.session.delete(user)
    db.session.commit()
    
    #route not yet tested
    return redirect('/users')



# @app.route()