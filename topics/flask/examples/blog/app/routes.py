from app import app
from markdown import markdown
from flask import render_template_string

#home page
@app.route("/")
def home():
    return "<h1>My Blog</h1>"

@app.route("/<view_name>")
def about(view_name):
    about_markdown = ""
    with open('app/views/'+ view_name +'.md') as contents:
        about_markdown = contents.read()
    about_html = markdown(about_markdown)
    return render_template_string(about_html, view_name=view_name)
    