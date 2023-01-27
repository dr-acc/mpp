"""My practice pal logginig functions"""


###--Static--Libraries--###
###--Will build out a section to distinguish between library and log functions===###
key_library = {
    "C": ["C", "D", "E", "F", "G", "A", "B"],
    "G": ["G", "A", "B", "C", "D", "E", "F#"],
    "D": ["D", "E", "F#", "G", "A", "B", "C#"],
    "A": ["A", "B", "C#", "D", "E", "F#", "G#"],
    "E": ["E", "F#", "G#", "A", "B", "C#", "D#"],
    "B": ["B", "C#", "D#", "E", "F#", "G#", "A#"],
    "F#": ["F#", "G#", "A#", "B", "C#", "D#", "E#"],
    "C#": ["C#", "D#", "E#", "F#", "G#", "A#", "B#"],
    "F":['F','G', 'A','B♭','C','D','E'],
    "B♭": ["B♭", "C", "D", "E♭", "F", "G", "A"],
    "E♭": ["E♭", "F", "G", "A♭", "B♭", "C", "D"],
    "A♭": ["A♭", "B♭", "C", "D♭", "E♭", "F", "G"],
    "D♭": ["D♭", "E♭", "F", "G♭", "A♭", "B♭", "C"],
    "G♭": ["G♭", "A♭", "B♭", "C♭", "D♭", "E♭", "F"],
    "C♭": ["C♭", "D♭", "E♭", "F♭", "G♭", "A♭", "B♭"],
}
mode_library = ["I Ionian", "II Dorian", "III Phrygian", "IV Lydian", "V Mixolydian", "VI Aeolean", "VII Locrian"]

six_variations = ["1 2 3", "1 3 2", "2 1 3", "2 3 1", "3 1 2", "3 2 1"]
for variation in six_variations:
    print(variation)
###I also put the variables below inside the play_bq function ###
# entry_num = 0
# total_min = 0
# noodle_min = 0
# theory_min = 0
# instrument_min = 0
# logged_noodle_min = 0
# logged_theory_min = 0
# logged_instrument_min = 0
# drill_library = ["broken thirds", "broken sixths", "6 variations", "subtraction"]
# list_of_maj_keys = ["C", "G", "D", "A", "E", "B", "F#", "C#", "F", "Bb", "Eb", "Ab", "Db", "Gb", "Cb"]
# entry_date = datetime.datetime.now() #should make timestamp each day(?)
# todays_drill = " "

# def welcome_player():
#   first_choice = input("Hi there! Type a number to start:\n 1 = log a practice session\n 2 = add new drill to library\n 3 = print out all major keys\n 4 = check out my stats\n 5 = log a music lesson\n 6 = log a jam session: ")
#     while True:
#         if first_choice == "1":
#             play_bq()
#         if first_choice == "2":
#             add_new_drill(drill_library)
#         if first_choice == "3":
#             for k, v in key_library:
#                 print(k, v)
# welcome_player()

# def add_new_drill(drill_library):
#     """If user chooses '2' in welcome_player, this function allows them to use a new drill. """
#     while True:
#         print("Drill library:")
#         for drill in drill_library:
#             print(drill)
#     new_drill = input("Type the name of a drill to save it in your library or '0' to exit: ")
#     if new_drill == "0":
#         welcome_player()
#     elif new_drill in drill_library:
#         print("That drill is already in your library.")
#         continue
#     else:
#         drill_library.append(new_drill)
#         print (f"{new_drill} added to your drill library.")
#         continue
#     return drill_library
# add_new_drill(drill_library)

def log():
    """First function is to run all the sub-functions for whole 'game'."""
# variables with empty counters ready to begin summing entries
    entry_num = 0
    total_min_today = 0
    noodle_min = 0
    theory_min = 0
    instrument_min = 0
    logged_noodle_min = 0
    logged_theory_min = 0
    logged_instrument_min = 0
    drill_library = ["broken thirds", "broken sixths", "6 variations", "subtraction"]
    list_of_maj_keys = ["C", "G", "D", "A", "E", "B", "F#", "C#", "F", "Bb", "Eb", "Ab", "Db", "Gb", "Cb"]
    entry_date = datetime.datetime.now() #should make timestamp each day(?)
    todays_drill = " "

### Intro instructions to daily logging ###
    print("\nLog your hard work to track your progress! Estimate how long you spent noodling, working on theory, or drilling on your instrument.\n")
    print("Only type numbers to save your info correctly.\n")
    print("Use '0' if your answer is none.\n")

    def add_total_min_today (total_min_today, noodle_min, theory_min, instrument_min, logged_noodle_min, logged_theory_min, logged_instrument_min):
        """This function totals the 3 categories of practice (noodle, theory, instrument)"""
        def ask_noodle_min():
            """Asks if user noodled around and for how long"""
            # logged_noodle_min = 0
            while True:
                print("A little bit of practice time can be 'noodling', just having fun.")
                noodle_min = int(input("How many minutes did you spend noodling? "))
                if noodle_min == 0:
                    print("\nSounds like you got straight down to business!")
                    break
                if noodle_min > 0 and noodle_min < 1440:
                    print(f"\nYou logged {noodle_min} minutes of noodling. Rock on!\n")
                    # logged_noodle_min += noodle_min
                    return noodle_min, logged_noodle_min
                elif noodle_min > 1440:
                    print("\nHmm... that number is more than the minutes available in a day.\nTry again.")
            return noodle_min, logged_noodle_min
        ask_noodle_min()

        def ask_theory_min():
            """Asks how long user spent on theory and off-instrument"""
            logged_theory_min = 0
            while True:
                print("\nPracticing theory is mental exercise, often  without your instrument.\n")
                theory_min = int(input("How many minutes of your practice focused on music theory? "))
                if theory_min == 0:
                    print("\nYou didn't log any theory minutes for this practice.")
                    break
                elif theory_min > 0 and theory_min < 1440:
                    logged_theory_min += theory_min
                    print(f"\nHooray, you logged {theory_min} minutes of theory practice!")
                    return theory_min, logged_theory_min
                elif theory_min > 1440:
                    print("\nHmm... that number is more than the minutes available in a day.\nTry again.")
                else:
                    print("\nYou can only log a number, like '60'. Type '0' if none.")
            return theory_min, logged_theory_min
        ask_theory_min()

        def ask_instrument_min():
            """Asks user for practice time on instrument"""
            logged_instrument_min = 0
            while True:
                print("\nInstrument practice means focused exercises, such as drills assigned by your teacher.\n")
                instrument_min = int(input("How many minutes did you practice on your instrument? "))
                if instrument_min == 0:
                    print("Not all practices require your instrument. Visualization works wonders!\n")
                    break
                if instrument_min > 0 and instrument_min < 1440:
                    logged_instrument_min += instrument_min
                    print(f"\nNice shredding! You logged {instrument_min} minutes of instrument practice!\n")
                    return instrument_min, logged_instrument_min
                elif instrument_min > 1440:
                    print("\nHmm... that number is more than the minutes available in a day.\nTry again.")
            return instrument_min, logged_instrument_min
        ask_instrument_min()
        
    total_min_today = noodle_min + theory_min + instrument_min
    #will also want all-time total in here, maybe
    print(f"You logged {total_min_today} minutes total. Funky!")
    return total_min_today, noodle_min, theory_min, instrument_min, logged_noodle_min, logged_theory_min, logged_instrument_min
    add_total_min_today(total_min_today, noodle_min, theory_min, instrument_min, logged_noodle_min, logged_theory_min, logged_instrument_min)









#     def log_drill_today():
#         """Adds a specific drill to the user's log, update the count of practices"""
#         todays_drill = " " #I guess this needs to be defined before the function(?)
#         while True:
#             todays_drill = input("\nAdd drill practice to your log today. Type the name of a drill in your library or 'no' to exit: ")
#             for drill in drill_library:
#                 print(drill)
#             todays_drill = todays_drill.lower()
#             if todays_drill == "no":
#                 print("\nNo drill added today.")
#             else:
#                 todays_drill = input("Type the name of a drill in your library: ")
#                 todays_drill = todays_drill.lower()
#                 if todays_drill not in drill_library:
#                     print("\nThat drill is not in your library.")
#                     continue
#                 if todays_drill in drill_library:
#                     print(f"You practiced {todays_drill}")
#             return todays_drill
#     log_drill_today()

#     def add_drill_key(todays_drill):
#         """Specifies key in which drill was practiced"""
#         if todays_drill == "no":
#             pass
#         elif todays_drill == "all": #leaving this here, but fyi, it isn't updating here yet
#             pass
#         else:
#             while True:
#                 print("\nWhich key did you practice this drill in?")
#                 for key in list_of_maj_keys:
#                     print(key)
#                 drill_key = input("\nType a major key, using 'b' or '#' for flat or sharp.\nType 'all' if you practiced in every key, or 'no' to skip.\n ")
#                 drill_key = drill_key.title()
#                 if drill_key == "No":
#                     break
#                 if drill_key == "All":
#                     print("\nNice work getting every key in!!!")
#                     ###will need to update all counts
#                     break
#                 if drill_key not in list_of_maj_keys:
#                     print("\nCheck that you typed the key in correctly. Example: 'Ab' for 'A♭'")
#                     continue
#                 if drill_key in list_of_maj_keys:
#                     print(f"You practiced {todays_drill} in {drill_key}. Woo hoo!")
#         return drill_key
#     add_drill_key()

#     def add_drill_mode(todays_drill):
#         if todays_drill == "no":
#             pass
#         elif todays_drill == "all":
#             pass
#         else:
#             while True:
#                 for mode in mode_library:
#                     print(mode)
#                     print("Did this drill focus on a particular mode?")
#                 mode_choice = input("Type the name of a mode, 'all' for all modes, 'no' to skip. ")
#                 mode_choice = mode_choice.lower()
#                 if mode_choice == "no":
#                     break
#                 if mode_choice == "all":
#                     print("You practiced all modes -- that's some top-shelf practicing!")
#                     #will need to append each mode if htey selected all
#                 if mode_choice not in mode_library:
#                     print("Mode not found in library. Try again.")
#                     continue
#                 if mode_choice in mode_library:
#                     print(f"You entered {mode_choice} -- right on!\n")
#                     break
#         return mode_choice
#     add_drill_mode(todays_drill)

#     def summarize_log(entry_num, noodle_min, theory_min, instrument_min, total_min):
#         print("Awesome job logging your practice session!! Check out your stats:")
#         print(f"Today's Entry: ({entry_num} + 1)\n")
#         print(f"Minutes noodled: {noodle_min}\n")
#         print(f"Minutes theorized: {theory_min}")
#         print(f"Minutes drilled: {instrument_min}")
#         print(f"You've logged a total of {total_min} on your journey to mastery!!!")
#     summarize_log(entry_num, entry_date, todays_drill, noodle_min, theory_min, instrument_min, total_min)
#     return summarize_log
log()

#         # log_entry = {0: (entry_date, drill_key, drill_mode)}
#         # print(f"Today you practiced: ")
#         # print(entry_date)

# # # #ok, now I'm thinking that there is so much more information to input that I need to pause and think if maybe this should all be a function -- like maybe logging time is separate and this is just a big ol' function
# # #         elif drill_entry == "key":
# # #             print("This part will be built out more later.")
# # #             pass
# # #         # Here is one spot where I'll use all kays global variable
# # #         # For now I'm going to build out the drill name
# # #         # I have some of these saved as js arrays already in my html file
# # #         elif drill_entry == "mode":
# # #             print("This part will be built out more later.")
# # #             pass 
# # # print("Jamming is often thought of as creative and casual playing with others.")

# # #now there's going to be another layer of nested loop to select which exercises the user did
# # #this is where things start to get complex but also really interesting
# # #I'm using my own practice and curriculum for now
# # # the goal is that it could be adapted for a particular teacher or curriculum
# # # def report_practice_breakdown(theory_min, instrument_min, jamming_min, total_min):
# # # percent_theory = (theory_min/total_min) * 100
# # # return percent_theory
# # #use .isdigit or .isnumeric built-in python methods to test if string, especially input(), is a number


# # #Here is a pile of ideas outside of scope for now:
# # # This should be a playing-with-others seperate section.
# # # Also things like gigs, rehearsals, workshops, camp.
# # # jamming_min = int(input("How many minutes was your jam session? "))
