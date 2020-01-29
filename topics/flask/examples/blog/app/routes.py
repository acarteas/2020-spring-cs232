#import certain functions into the global
#namespace
from app import app
from markdown import markdown
from flask import render_template_string, request
from app.blog_helpers import render_markdown

#safe global import (okay to use)
import flask

#global import (try to avoid)
#from flask import *

#home page
@app.route("/")
def home():
    return render_markdown('index.md')

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':

        #TODO: process request.values as necessary
        pass

#generic page
@app.route("/<view_name>")

#input parameter name must match route parameter
def render_page(view_name):
    html = render_markdown(view_name + '.md')
    return render_template_string(html, view_name = view_name)


