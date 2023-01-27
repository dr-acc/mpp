"""Models for music practice logger app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A musician & app user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    routines = db.relationship("Routines", back_populates="user")

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"


class Routine(db.Model):
    """A user-created grouping of skills and exercises to practice regularly."""

    __tablename__ = "routines"

    routine_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String) ###this will come from form
    description = db.Column(db.Text) ### form text field data
    
    user_routines = db.relationship("Routines", back_populates="users")
    ####^what am I doing here?####

    def __repr__(self):
        return f"<Routine routine_id={self.routine_id} title={self.title}>"


class PracticeSession(db.Model):
    """A single log entry representing a user's practice session."""

    __tablename__ = "practice_sessions"
    
    practice_session_id = db.Column(db.Integer, autoincrement=True, primary_key=True) ###a unique identifier
    practice_date = db.Column(db.DateTime) #this is automatic
    exercises_this_session = db.Column(db.#####) ### 
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id")) # each session created by a logged-in user


    user_session = db.relationship("User", back_populates="user")  ##<<I'm not confident on this
    #should it be "pratice session"? What else am I missing?

    def __repr__(self):
        return f"<PracticeSession practice_session_id={self.practice_session_id} practice_date={self.practice_date}>"
        ###simple repr for session id number and date

class Exercise(db.Model):
    __tablename__ = "exercises"

    exercise_id = db.Column(db.Integer, autoincrement=True, primary_key=True) ###a unique identifier
    ####haven't really finished this yet; may need help to think through

    def __repr__(self):
        return f"<PracticeSession practice_session_id={self.practice_session_id} practice_date={self.practice_date}>"
        ###simple repr for session id number and date

    exercises_in_routine = db.relationship("Exercises", back_populates="routines")
    ###^am I doing that right and do I need one for users too?###


###this, below, is not something I feel confident about###

def connect_to_db(flask_app, db_uri="postgresql:///mpp", echo=True): 
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets  annoying
    # this will tell SQLAlchemy not to print out every query it executes.

    connect_to_db(app)
