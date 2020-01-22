from app import app

#home page
@app.route("/")
def home():
    return "<h1>My Blog</h1>"

@app.route("/about")
def about():
    return "<h1>About Me</h1>"