import json
from tkinter import Button, Entry
from canvas import app
from shop_app.helpers import clean_screen


USERS_FILE = './db/users.txt'
CREDENTIALS_FILE = './db/user_credentials_db.txt'


def login(username, password):
    pass


def register(**user):
    user.update({'products': []})
    with open(USERS_FILE, 'a') as file:
        file.write(json.dumps(user))
        file.write('\n')
    with open(CREDENTIALS_FILE, 'a') as file:
        file.write(f'{user.get("username")} | {user.get("password")}')
        file.write('\n')


def render_login():
    clean_screen()
    username = Entry(app)
    username.grid(row=0, column=0)
    password = Entry(app, show='*')
    password.grid(row=1, column=0)
    Button(app, text='Submit', bg='green', fg='white',
           command=lambda: login(
               username=username.get(),
               password=password.get())).grid(row=3, column=0)


def render_register():
    # Todo: retype password
    # Todo: Label for fields left of field
    clean_screen()
    username = Entry(app)
    username.grid(row=0, column=0)
    password = Entry(app, show='*')
    password.grid(row=1, column=0)
    first_name = Entry(app)
    first_name.grid(row=2, column=0)
    last_name = Entry(app)
    last_name.grid(row=3, column=0)
    Button(app, text='Submit', bg='green', fg='white',
           command=lambda: register(
               username=username.get(),
               password=password.get(),
               first_name=first_name.get(),
               last_name=last_name.get())).grid(row=4, column=0)


def render_main_enter_screen():
    Button(app, text='LogIn', bg='green', fg='white', command=render_login).grid(row=0, column=0)
    Button(app, text='Register', bg='yellow', fg='black', command=render_register).grid(row=0, column=1)
