#goal 1 is to make numbers game and then add increasing difficulties 

import random

import time

import sqlite3

con = sqlite3.connect('db1.db')

curs = con.cursor()

def save_score():

    con.commit()

con.execute("""CREATE TABLE IF NOT EXISTS hiscore2 (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
score INT NOT NULL)""")

def find_high_score_by_name(name):

    curs.execute('SELECT score FROM hiscore2 WHERE name=?', (name,))

    global mmr

    mmr = curs.fetchall()

    if mmr:

        mmr = int(mmr[0][0])

        print("Welcome back '{}':".format(name))

        print(f'Your last recorded score was {mmr}')
        
    else:

        mmr = int(1)

        print("Greetings,", name, "enjoy the game!")

        curs.execute("INSERT INTO hiscore2 (name, score) VALUES(?, ?)", (name, mmr))

print("Welcome to Minimalist's Math Game... Please enter your name:")

global name

name = input()

find_high_score_by_name(name)

#print("Greetings,", name, "enjoy the game!")

print('The rules are simple... just complete the math functions! Say "STOP" to quit. Otherwise the game will continue. Say anything to continue')

input()

while True:

    if mmr <= 0:
         
         mmr = 1

         
    val1 = random.randint(1,10)*int(mmr)


    val2 = random.randint(5,15)*int(mmr)


    ans = int(val1) + int(val2)


    print("What is", int(round(val1, 0)), "+", int(round(val2, 0)),"?")


    start = time.time()


    inp = input()


    if inp.upper() == "STOP":

        print(f"Your new score is saved as {mmr}!")

        print('Press any key to see high scores:')

        input()

        curs.execute("SELECT name, score FROM hiscore2 ORDER BY score DESC LIMIT 10")

        top_scores = curs.fetchall()

        print("Top 10 High Scores:")

        for rank, (name, score) in enumerate(top_scores, start=1):
            print(f"{rank}. {name}: {score}")

        save_score()

        con.close()

        break

    try:

        while True:

            user_ans = int(inp)
            
            if user_ans == ans:

                end = time.time()

                mmr = mmr + (30- round(end - start, 0))

                curs.execute("UPDATE hiscore2 SET score = ? WHERE name = ?", (int(mmr), name))

                save_score()

                rm1 = random.randint(0,9)

                wmsg = [

                    'Good work,',

                    'Nice one,',

                    'Well done,',

                    "That's right,",

                    'LETS GOOOO,',

                    'Pfft that one was easy,',

                    'Congrats,',

                    'zzz,',

                    'Well played,',

                    'yep,'

                ]

                print(wmsg[rm1-1], name)

                print('new rating:',mmr,)

                print(end-start)

                print('Say anything to continue')

                input()

                break

            else:

                mmr = mmr - 10

                curs.execute("UPDATE hiscore2 SET score = ? WHERE name = ?", (int(mmr), name))

                save_score()

                rm2 = random.randint(0,9)

                lmsg = [

                    'Try again,',

                    'Incorrect,',

                    'My lord you suck,',

                    '*sigh* Again,',

                    'Nope,',

                    'NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO,',

                    'Close one,',

                    'Wrong answer,',

                    'Wrong number,',

                    'Nice job! SIKE THATS WRONG,'

                ]

                print(lmsg[rm2], name)

                print("What is", int(round(val1,0)), "+", int(round(val2,0)),"?")

                inp = input()

        #this is the backdoor for the error of a player inputting a non integer that isnt "stop" which asks for more
                
    except ValueError:

        print("Please type an integer to answer or type 'stop' to quit.")

        


    

    
