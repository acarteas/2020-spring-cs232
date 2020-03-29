#import certain functions into the global
#namespace
from app import app
from flask import render_template, render_template_string, request, session

#safe global import (okay to use)
import flask

#home page
@app.route("/")
def home():
    return ""

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        
        #TODO: process request.values as necessary
        if request.values['user_name'] == 'user' and \
            request.values['password'] == 'password':
            return "success", 200
        else:
            return "error", 404
    return ""

@app.route("/favicon.ico")
def favicon():
    return ""


