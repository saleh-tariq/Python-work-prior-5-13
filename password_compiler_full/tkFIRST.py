import tkinter as tk
import ttkbootstrap as ttk
import random
from pyperclip import copy
import sqlite3


root = ttk.Window(themename= 'darkly')
root.geometry('800x600')
root.minsize(800,600)
root.maxsize(800,600)
frame = ttk.Frame(root)
# root.bind('<Escape>', lambda event: main_window_setup(frame))

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

def main_window_setup(frame):
    frame.pack_forget()

    frame = ttk.Frame(root)
    frame.rowconfigure((0,1),weight=1, uniform='a')
    frame.columnconfigure((0,1),weight=1, uniform='a')
    frame.pack(expand=True,fill='both')

    #main widgets
    back_drop = ttk.Label(frame, text='',background='gold4')

    button1 = ttk.Button(frame, text= 'New login',style= 'dark', command= lambda: new_login(frame))
    button2 = ttk.Button(frame, text= 'Change login',style= 'dark', command= lambda: change_login(frame))
    button3 = ttk.Button(frame, text= 'Make password',style= 'dark', command= lambda: make_password(frame))
    button4 = ttk.Button(frame, text= 'Exit',style= 'light', command= lambda: root.quit())

    button1.grid(row=0,column=0,sticky='enws',padx=10, pady=10)
    button2.grid(row=0,column=1,sticky='enws',padx=10, pady=10)
    button3.grid(row=1,column=0,sticky='enws',padx=10, pady=10)
    button4.grid(row=1,column=1,sticky='enws',padx=10, pady=10)

    back_drop.grid(column=0,row=0,columnspan=2,rowspan=2,sticky='news')

def side_menu_setup(frame):
    frame.pack_forget()
    frame = ttk.Frame(root)
    frame.rowconfigure(0,weight=1, uniform='an')
    frame.columnconfigure((0,1,2,3),weight=1, uniform='an')
    
    menu_frame = ttk.Frame(frame)
    menu_frame.rowconfigure((0,1,2,3), weight=1,uniform='v')
    menu_frame.columnconfigure(0,weight=1,uniform='a')

    back_drop = ttk.Label(menu_frame, text='',background='gold4')

    button1 = ttk.Button(menu_frame, text= 'New Login',style= 'dark', command=lambda:new_login(frame))
    button2 = ttk.Button(menu_frame, text= 'Change login',style= 'dark', command= lambda: change_login(frame))
    button3 = ttk.Button(menu_frame, text= 'Make password',style= 'dark', command= lambda: make_password(frame))
    button4 = ttk.Button(menu_frame, text= 'Main',style= 'dark', command= lambda: main_window_setup(frame))

    back_drop.grid(row=0,column=0,rowspan=4,sticky='news')

    button1.grid(row=0,column=0,sticky='enws', pady=5,padx=5)
    button2.grid(row=1,column=0,sticky='enws', pady=5,padx=5)
    button3.grid(row=2,column=0,sticky='enws', pady=5,padx=5)
    button4.grid(row=3,column=0,sticky='enws', pady=5,padx=5)

    frame.pack(expand=True,fill='both')
    menu_frame.grid(row=0,column=0,sticky='news')
    return frame

def new_login(frame):
    frame = side_menu_setup(frame)
    frame.grid_forget()
    login_frame = ttk.Frame(frame)
    login_frame.rowconfigure((0,1,2,3,4),weight=1, uniform='a')
    login_frame.columnconfigure((0,1,2,3),weight=1, uniform='a')

    label1 = ttk.Label(login_frame, text='Enter domain:', font= 'Terminal 14 bold')
    label2 = ttk.Label(login_frame, text='Enter username:', font= 'Terminal 14 bold')
    label3 = ttk.Label(login_frame, text='Enter password:', font= 'Terminal 14 bold')
    label4 = ttk.Label(login_frame, text='Re-enter password:', font= 'Terminal 14 bold')

    domain_entry = ttk.StringVar()
    user_entry = ttk.StringVar()
    pass1_entry = ttk.StringVar()
    pass2_entry = ttk.StringVar()

    entry1 = ttk.Entry(login_frame, textvariable= domain_entry)
    entry2 = ttk.Entry(login_frame, textvariable= user_entry)
    entry3 = ttk.Entry(login_frame, textvariable= pass1_entry,show='*')
    entry4 = ttk.Entry(login_frame, textvariable= pass2_entry,show='*')

    button1 = ttk.Button(login_frame, text='Save', style= 'light',command= lambda: save_new_login(domain_entry,user_entry,pass1_entry,pass2_entry,frame))

    label1.grid(row=0,column=0,columnspan=2,sticky='news',padx=5,pady=5)
    entry1.grid(row=0, column=2, columnspan=2,sticky='ew',padx=5,pady=5)

    label2.grid(row=1,column=0,columnspan=2,sticky='news',padx=5,pady=5)
    entry2.grid(row=1, column=2, columnspan=2,sticky='ew',padx=5,pady=5)

    label3.grid(row=2,column=0,columnspan=2,sticky='news',padx=5,pady=5)
    entry3.grid(row=2, column=2, columnspan=2,sticky='ew',padx=5,pady=5)

    label4.grid(row=3,column=0,columnspan=2,sticky='news',padx=5,pady=5)
    entry4.grid(row=3, column=2, columnspan=2,sticky='ew',padx=5,pady=5)

    button1.grid(row=4,column=0,columnspan=4,sticky='news',padx=5,pady=5)

    login_frame.place(relx=.25, rely=0, relheight=1,relwidth=.75)

    frame.pack(expand=True,fill='both')

def change_login(frame):
    global table
    frame = side_menu_setup(frame)
    frame.grid_forget()

    frame1 = ttk.Frame(frame)

    # treeview
    table = ttk.Treeview(frame1, columns = ('Index', 'Domain', 'User'), show= 'headings')
    table.heading('Index',text='ID Number')
    table.heading('Domain',text = 'Domain')
    table.heading('User',text = 'Username')

    con = sqlite3.connect('db1.db')
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS pass (
    id INTEGER PRIMARY KEY,
    domain text NOT NULL,
    username text NOT NULL,
    password text NOT NULL)""")   

    cur.execute("SELECT * FROM pass")
    
    for list in cur.fetchall():
        table.insert(parent= '', index=0, values= list)



    table.bind('<<TreeviewSelect>>', lambda event: change_login_screen2(frame,table))

    table.pack(fill = 'both', expand= True)
    frame1.place(relx=.25, rely=0, relheight=1,relwidth=.75)
    frame.pack(expand=True,fill='both')


def change_login_screen2(frame,table):
    user_pass1= ttk.StringVar
    user_pass2= ttk.StringVar

    frame = side_menu_setup(frame)
    frame.grid_forget()

    new_password_frame = ttk.Frame(frame)
    new_password_frame.columnconfigure((0,1,2), weight=1,uniform='a')
    new_password_frame.rowconfigure((0,1,2),weight=1,uniform='a')

    pass_label1 = ttk.Label(new_password_frame,text=f'New password:')
    pass_label2 = ttk.Label(new_password_frame,text=f'Repeat password:')

    pass_entry1 = ttk.Entry(new_password_frame,textvariable=user_pass1)
    pass_entry2 = ttk.Entry(new_password_frame,textvariable=user_pass2)

    pass_label1.grid(row=1, column=0, sticky='news')
    pass_label2.grid(row=2, column=0, sticky='news')
    pass_entry1.grid(row=1, column=1, sticky='ew',columnspan=2)
    pass_entry2.grid(row=2, column=1, sticky='ew',columnspan=2)

    new_password_frame.place(relx=.25, rely=0, relheight=1,relwidth=.75)

def make_password(frame):
    frame = side_menu_setup(frame)
    frame.grid_forget()

    make_frame = ttk.Frame(frame)

    string_to_copy = password_gen()

    label = ttk.Label(make_frame, text=string_to_copy,font= 'Terminal 14 bold')

    button = ttk.Button(make_frame, text= 'Copy',style='light', command= lambda: copy(string_to_copy))

    make_frame.place(relx=.25, rely=0, relheight=1,relwidth=.75)

    label.place(relx=.5,rely=.5,anchor='center')
    button.place(relx=.5, rely=.7,relheight=.15,relwidth=.3,anchor='center')


def save_new_login(domain_entry,user_entry,pass1_entry,pass2_entry,frame):
    con = sqlite3.connect('db1.db')
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS pass (
    id INTEGER PRIMARY KEY,
    domain text NOT NULL,
    username text NOT NULL,
    password text NOT NULL)""")

    domain1 = domain_entry.get()
    username1 = user_entry.get()
    password1 = pass1_entry.get()
    password2 = pass2_entry.get()

    if password1 == password2:
        cur.execute("INSERT INTO pass (domain, username, password) VALUES(?, ?, ?)", (domain1, username1, password1))
        con.commit()
        con.close()
        main_window_setup(frame)

        return True

    else:
        con.close()

        return False
    

main_window_setup(frame)
root.mainloop()