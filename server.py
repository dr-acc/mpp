from flask import Flask, render_template, redirect, flash
import jinja2

app = Flask(__name__)

###SO... do I need all this section?#####
# A secret key is needed to use Flask sessioning features
app.secret_key = 's0m3TH!ng'

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.
app.jinja_env.undefined = jinja2.StrictUndefined

# This configuration option makes the Flask interactive debugger
# more useful (you should remove this line in production though)
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True
###############################################


@app.route("/")
def index():
    """Return homepage."""

    return render_template("mpp.html")

@app.route("/signup")
def signup():
###add new user to database###
###here is where to use redirect so flask sends user to routines(/routine)###
    return redirect("/routine")

@app.route("/routine")
def create_routine():
    """Create a Routine, a grouping of drills to practice.

    Users signing up will be (re)directed here first.

    Existing users will be able to add new routines to distinguish groupings of their drills & exercises"""

    return render_template("logger.html")
    ### I think going straight to the logging function makes sense here but will want to check-in about it again over time
    ### So, this would be a "template" because it is getting some info about this individual user and their saved data (I think)

@app.route("/logger")
def log_practice_session():
    """Allow user to log a practice session
    Form data is partially pre-filled based on their Routine(s)"""
    return render_template("dashboard.html")
    ##maybe some kind of flashed message congratulating the user for logging a new session

@app.route("/dashboard")
##from dash there will be navigation home or log
def show_dash():
    return render_template("dashboard.html")
    ###user-specific with <user..>^?

    