import os
from model import connect_to_db, db, User, Exercise, Routine, PracticeSession
from server import app



os.system("dropdb mpp")
os.system("createdb mpp")

connect_to_db(app)
app.app_context().push()

db.create_all()

user = User(email="pwrchords2@yahoo.com", password="p")
db.session.add(user)
db.session.commit()

db.session.refresh(user)

routine1 = Routine(title="Patterns", description="A Routine to track progress in Pattern System", user=user)
routine2 = Routine(title="Finger Exercises", description="Drills to play at 120bpm one day", user=user)
routine3 = Routine(title="Harmonium Jams", description="Songs to play with Ann & friends", user=user)

db.session.add_all([routine1, routine2, routine3])
db.session.commit()

db.session.refresh(routine1)
db.session.refresh(routine2)
db.session.refresh(routine3)

exercise1 = Exercise(ex_title="Charting Open Area", routine=routine1, bpm=100, user_id=1)
exercise2 = Exercise(ex_title="Workbook", routine=routine1,  user_id=1)
exercise3 = Exercise(ex_title="Play Along", routine = routine1, bpm=106, user_id=1)
exercise4 = Exercise(ex_title="Broken Thirds", routine=routine2, bpm=60, user_id=1)
exercise5 = Exercise(ex_title="Broken Sixths", routine=routine2, bpm=89, user_id=1)
exercise6 = Exercise(ex_title="Subtraction", routine=routine2, user_id=1)
exercise7 = Exercise(ex_title="Major Scales All Strings", routine=routine2, user_id=1)
exercise8 = Exercise(ex_title="Six Variations", routine=routine2, user_id=1) 
exercise9 = Exercise(ex_title="Shh", routine=routine3, user_id=1)
exercise10 = Exercise(ex_title="Broken Sixths", routine=routine2, bpm=100, user_id=1)

db.session.add_all([exercise1, exercise2, exercise3, exercise4, exercise5, exercise6, exercise7, exercise8, exercise9, exercise10])
db.session.commit()

practice_session = PracticeSession(date="01-01-2023", total_session_min=60, user=user, routine=routine1)

db.session.add(practice_session)
db.session.commit()

