from flask import Flask, render_template, redirect, request, flash, session
import jinja2
from model import Routine, User, Exercise, PracticeSession, db
from crud import last_two_sessions

app = Flask(__name__)
app.secret_key = 's0m3TH!ng'

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.
app.jinja_env.undefined = jinja2.StrictUndefined

# This configuration option makes the Flask interactive debugger
# more useful (you should remove this line in production though)
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True

list_of_maj_keys = ["C", "G", "D", "A", "E", "B", "F#", "C#", "F", "Bb", "Eb", "Ab", "Db", "Gb", "Cb"]
mode_library = ["I Ionian", "II Dorian", "III Phrygian", "IV Lydian", "V Mixolydian", "VI Aeolean", "VII Locrian"]
direction_variations = ["Forwards", "Backwards", "Forwards & Back", "Backwards & Forward", "Ascending", "Descending"]




@app.route("/")
def landing():
    """Return homepage."""

    return render_template("landing.html")


@app.route("/signup", methods=['POST'])
def signup():
    user_email = request.form.get("signup_email")
    user_password = request.form.get("signup_password")

    if User.query.filter(User.email == user_email).first():
        flash("Email already in use")
        return redirect("/")

    new_user = User(email=user_email, password=user_password)
    db.session.add(new_user)
    db.session.commit()

    flash("New user created; enter email and password to sign in")
    return redirect("/")


@app.route("/login", methods=['POST'])
def login():
    email_input = request.form.get("email_input") 
    password_input = request.form.get("password_input")

    user = User.query.filter(User.email == email_input).first()
    practice_sessions = last_two_sessions(user.user_id)

    if user:
        if user.password == password_input:
            session["user_id"] = user.user_id
            flash("Successfully logged in")
            return render_template("log.html", user=user, practice_sessions=practice_sessions, list_of_maj_keys=list_of_maj_keys, mode_library=mode_library)
        else:
            flash("Password does not match email")
            return redirect("/")
    
    else: 
        flash("Email not found")
        return redirect("/") 


@app.route("/routine", methods=["GET", "POST"])
def create_routine():
    """Create a Routine, a grouping of exercises to practice.

    Users signing up will be (re)directed here first.

    Existing users will be able to add new routines to distinguish groupings of their drills & exercises"""
    if request.method == "POST":

        new_title = request.form.get("title")
        new_description = request.form.get("description")
        new_exercises = request.form.getlist("exercise")

        user = User.query.filter(User.user_id == session["user_id"]).first()
        print(user)

        new_routine = Routine(title=new_title, description=new_description, user=user)
        print(new_routine)

        db.session.add(new_routine)
        db.session.commit()

        ###
        db.session.refresh(new_routine)

        for exercise in new_exercises:
            new_exercise = Exercise(ex_title=exercise, routine=new_routine)
            db.session.add(new_exercise)

        db.session.commit()

        ###

        return redirect("/routine")

    return render_template("routines.html")


@app.route("/log", methods=["POST"])
def log_practice_session():
    """Allow user to log a practice session, saving to db.

    Form data is partially pre-filled based on their Routine(s)"""

    date = request.form.get("date")

    session_min = int(request.form.get("session_minutes"))
    on_instrument_min = int(request.form.get("on_instrument_min"))
    off_instrument_min = int(request.form.get("off_instrument_min"))
    
    routine_id = request.form.get("select_routine")
    routine = Routine.query.filter(Routine.routine_id == routine_id).first()

    exercises_this_session = request.form.getlist("exercise")

    session_difficulty = request.form.get("session_difficulty")
    session_enjoyment = request.form.get("session_enjoyment")
    notes_next_practice = request.form.get("notes_for_practice")
    questions_for_teacher = request.form.get("questions_teacher")

    print(f"Routine: {routine.title}")
    print(f"Exercises: {exercises_this_session}")

    user = User.query.filter(User.user_id == session["user_id"]).first()

    new_practice_session = PracticeSession(date=date, 
                                           total_session_min=session_min, 
                                           on_instrument_min=on_instrument_min, 
                                           off_instrument_min=off_instrument_min,
                                           session_challenge_level=session_difficulty,
                                           session_enjoyment_level=session_enjoyment,
                                           notes_next_practice=notes_next_practice,
                                           questions_for_teacher=questions_for_teacher,
                                           exercises_this_session="|".join(exercises_this_session),
                                           user=user,
                                           routine=routine
                                           )

    print(new_practice_session)

    db.session.add(new_practice_session)
    db.session.commit()
    # return redirect("/  ")

    practice_sessions = last_two_sessions(user.user_id)
    

    return render_template("log.html", user=user, practice_sessions=practice_sessions, list_of_maj_keys=list_of_maj_keys, mode_library = mode_library)


@app.route("/dashboard")
def show_dash():
    
    """Display data on page with stats & cool visualizations """

    user = User.query.filter_by(user_id=session["user_id"]).first()

    return render_template("dashboard.html", user=user)


if __name__ == "__main__":
    from model import connect_to_db
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
