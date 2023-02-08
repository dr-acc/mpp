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
    routines = db.relationship("Routine", back_populates="user")
    practice_sessions = db.relationship("PracticeSession", back_populates="user")

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"


class Routine(db.Model):
    """A user-created grouping of skills and exercises to practice regularly."""

    __tablename__ = "routines"

    routine_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String) ###this will come from form
    description = db.Column(db.Text) ### form text field data
    exercises = db.Column(db.String) 
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    user = db.relationship("User", back_populates="routines")

    practice_sessions = db.relationship("PracticeSession", back_populates="routine")
    

    def __repr__(self):
        return f"<Routine routine_id={self.routine_id} title={self.title}>"


class PracticeSession(db.Model):
    """A single log entry representing a user's practice session."""

    __tablename__ = "practice_sessions"
    
    session_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date = db.Column(db.DateTime)
    exercises_this_session = db.Column(db.String, nullable=True)
    total_session_min = db.Column(db.Integer)
    on_instrument_min = db.Column(db.Integer, nullable=True)
    off_instrument_min = db.Column(db.Integer, nullable=True)
    session_challenge_level = db.Column(db.String, nullable=True)
    session_enjoyment_level = db.Column(db.String, nullable=True)
    notes_next_practice = db.Column(db.String, nullable=True)
    questions_for_teacher = db.Column(db.String, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    user = db.relationship("User", back_populates="practice_sessions")  

    routine_id = db.Column(db.Integer, db.ForeignKey("routines.routine_id"))
    routine = db.relationship("Routine", back_populates="practice_sessions")


    def __repr__(self):
        return f"<PracticeSession {self.practice_session_id} Date: {self.date} Exercises: {self.exercises_this_session}>"


# class Exercise(db.Model):
#     __tablename__ = "exercises"

#     exercise_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     ex_title = db.Column(db.String)

    # practice_date = 
    # def __repr__(self):
    #     return f"<Exercise {self.ex_title}>"
        ###simple repr for session id number and date

    # exercises_in_routine = db.relationship("Exercises", back_populates="routines")
    ###^am I doing that right and do I need one for users too?###


###can change "echo", below, to True if you want to see a much more verbose readout
def connect_to_db(flask_app, db_uri="postgresql:///mpp", echo=False): 
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
