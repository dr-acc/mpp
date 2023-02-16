"""CRUD operations (CREATE READ UPDATE DELETE)"""

from model import db, connect_to_db, User, Routine, User, Exercise, PracticeSession
###How to get db imports to show up?^^


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user


def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def create_routine(routine_id, title, description, exercises):

    """Create and return a new Routine."""

    routine = Routine(
        routine_id = routine_id,
        title = title,
        description = description,
        exercises = exercises,
    )

    return routine


def get_routines():
    """Return all routines."""

    return Routine.query.all()


def create_exercise(user, routine, exercise):
    """Allows user to create an exercise within a routine"""

    exercise = Exercise(user=user, routine=routine, exercise=exercise)

    return exercise

def last_two_sessions(user_id):
    """Return the 2 most recent PracticeSessions of the user"""

    return PracticeSession.query.filter_by(user_id=user_id).order_by(PracticeSession.session_id.desc()).limit(2).all()


# def update_routine():
#     """ 3.0 or 4.0 feature: Update a routine that was already created. """
#     routine = Routine.query.get()


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
