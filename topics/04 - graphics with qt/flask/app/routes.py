from app import app
from flask import render_template, render_template_string, request, session
import flask


#home page
@app.route("/")
def home():
    "Welcome to my flask app."

@app.route('/login', methods=['POST'])
def login():

    if request.method == 'POST':
        
        #TODO: process request.values as necessary
        if(request.values['user_name'] == "user" and request.values["password"] == "password"):
            return "success"
        return "error", 404
