"""Blogly application."""

import re
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

    return render_template("userlist.html")
#in ipython do db.session.execute('SELECt*from blah') and set to 
# a vars and put in a list to see the data


@app.route('/users/new')#method is get by default?
def add_user_form():

    return render_template('makeuser.html')

    

@app.route('/users/new', methods=["POST"])
def post_user():

    return redirect("/users")



@app.route('/users/<int:user_num>', methods=["GET"])
def show_question(user_num):
    """Show information about the given user.

    Have a button to get to their edit page, and to delete the user.
    """


    
    return render_template('details.html',user_num=user_num)



@app.route('/users/<int:user_num>/edit', methods=["GET"])
def edit_user(user_num):
    """
    Show the edit page for a user.

    Have a cancel button that returns to the detail page for 
    a user, and a save button that updates the user.
    """
    # https://stackoverflow.com/questions/547821/two-submit-buttons-in-one-form

    return render_template('edit.html',user_num=user_num)


@app.route('/users/<int:user_num>/edit', methods=["POST"])
def store_edits(user_num):
    """
    Process the edit form, returning the user to the /users page.
    """

    
    return redirect('/users')



@app.route('/users/<int:user_num>/delete', methods=["POST"])
def delete_user(user_num):
    """
    Process the edit form, returning the user to the /users page.
    """

    # return the user to the /users page.
    
    #route not yet tested
    return redirect('/users')



# @app.route()