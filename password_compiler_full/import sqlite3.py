import sqlite3
import random

con = sqlite3.connect('db1.db')

cur = con.cursor()

def get_user_input():

    print("Enter domain name")

    domain1 = input()

    print('Enter username for', domain1)

    username1 = input()

    print('Enter password for', domain1)

    password1 = input()

    print('Please reenter the password')

    password2 = input()

    if password1 == password2:

        cur.execute("INSERT INTO pass (domain, username, password) VALUES(?, ?, ?)", (domain1, username1, password1))

        con.commit()

    else:

        print("Passwords don't match")


def save_and_exit():
    
    con.commit()

    con.close()


def read_from_database():

    cur.execute('SELECT DISTINCT domain FROM pass')

    domainData = cur.fetchall()

    print('Domains in the database:')

    for row in domainData:

        print(row[0])


def password_update():

    print('Please enter a domain name:')

    read_from_database()

    user_domain_input = input()

    cur.execute("SELECT username FROM pass WHERE domain =?", (user_domain_input,))

    usernames1 = cur.fetchall()

    if usernames1:

        print(f"Usernames for domain {user_domain_input}")

        for username in usernames1:

            print(username[0])

    else:

        print("Not found")

        return

    print("Please enter a username:")

    user_username_input = input()

    print("Please enter a new password:")

    user_password_input1 = input()

    print("Please re-enter the password:")

    user_password_input2 = input()

    if user_password_input1 == user_password_input2:
        
        cur.execute(f"UPDATE pass SET password = ? WHERE domain = ? AND username = ?",(user_password_input2, user_domain_input, user_username_input))

        con.commit()

    else:

        print("Passwords don't match")


def find_usernames_by_domain(domain):

    cur.execute('SELECT username FROM pass WHERE domain=?', (domain,))

    usernames = cur.fetchall()

    if usernames:

        print("Usernames for domain '{}':".format(domain))

        for username in usernames:

            print(username[0])

    else:
        print("No usernames found for domain'{}'".format(domain))


def password_gen():
    char_list = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','r','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','!','$','%','#','@','(']
    randint = random.randint(10,15)
    x=0
    randpass = ''
    while x <= randint:
        char = random.choice(char_list) 
        randpass += char
        x += 1
    return randpass

command1 = """CREATE TABLE IF NOT EXISTS pass (
id INTEGER PRIMARY KEY,
domain text NOT NULL,
username text NOT NULL,
password text NOT NULL)"""

cur.execute(command1)

print('Please enter pin')

global pin

global pinset

pin = input()

cur.execute("""CREATE TABLE IF NOT EXISTS pin (
id INTEGER PRIMARY KEY,
setpin INTEGER NOT NULL)""")

#cur.execute("INSERT INTO pin (id, setpin) VALUES(?, ?)",(1, pin))

cur.execute("SELECT setpin FROM pin")

pinset = cur.fetchall()

if int(pin) != int(pinset[0][0]):

    print('woops')
    quit()
else:
    print('nice')

while True:
    print("Press 1 to input new data, press 2 to change a password, or press 3 to EXIT.")

    inpSelection1 = input()

    try:

        if int(inpSelection1) == 1:
        
            get_user_input()

        if int(inpSelection1) == 2:

            password_update()

        elif int(inpSelection1) == 3:

            break

    except ValueError:

            print("Please enter an integer 1, 2, or 3.")

            continue

print("Please enter a new pin:")

newpin = input()

cur.execute("UPDATE pin SET setpin = ? WHERE id = ?", (int(newpin), 1))

con.commit()

con.close()




















