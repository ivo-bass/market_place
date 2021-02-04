import json
import os
from shop_app.canvas import app
from shop_app.helpers import clean_screen
from shop_app.products import render_products
from tkinter import Button, Entry, Label, Frame

BASE_DIR = os.path.dirname(__file__)
IMAGE_DIR = os.path.join(BASE_DIR, 'images')
DB_DIR = os.path.join(BASE_DIR, 'db')
PRODUCTS_FILE = os.path.join(DB_DIR, 'products.txt')
USERS_FILE = os.path.join(DB_DIR, 'users.txt')
CURRENT_USER_FILE = os.path.join(DB_DIR, 'current_user.txt')
CREDENTIALS_FILE = os.path.join(DB_DIR, 'user_credentials_db.txt')
ERROR_CREDENTIALS = 'Invalid username or password'


def login(username, password):
    with open(CREDENTIALS_FILE, 'r') as file:
        lines = file.readlines()
        for line in lines:
            u, p = line[:-1].split(' | ')
            if u == username and p == password:
                with open(CURRENT_USER_FILE, 'w') as f:
                    f.write(username)
                    render_products()
                return
        render_login(err=ERROR_CREDENTIALS)


def register(**user):
    user.update({'products': []})
    with open(USERS_FILE, 'a') as file:
        file.write(json.dumps(user))
        file.write('\n')
    with open(CREDENTIALS_FILE, 'a') as file:
        file.write(f'{user.get("username")} | {user.get("password")}')
        file.write('\n')
    render_login()


def render_login(err=None):
    clean_screen()
    frame = Frame(app, width=400, height=400)
    frame.grid(row=0, column=0, padx=220, pady=100)

    label = Label(frame, text='Username: ')
    label.grid(row=0, column=0)
    username = Entry(frame)
    username.grid(row=0, column=1)

    label = Label(frame, text='Password: ')
    label.grid(row=1, column=0)
    password = Entry(frame, show='*')
    password.grid(row=1, column=1)
    Button(frame, text='Submit', bg='green', fg='white',
           command=lambda: login(
               username=username.get(),
               password=password.get())).grid(row=4, column=1, pady=30)
    if err:
        Label(frame, text=err).grid(row=3, column=1)


def render_register():
    # Todo: retype password
    clean_screen()
    frame = Frame(app, width=400, height=400)
    frame.grid(row=0, column=0, padx=220, pady=100)

    label = Label(frame, text='Username: ')
    label.grid(row=0, column=0)
    username = Entry(frame)
    username.grid(row=0, column=1)

    label = Label(frame, text='Password: ')
    label.grid(row=1, column=0)
    password = Entry(frame, show='*')
    password.grid(row=1, column=1)

    label = Label(frame, text='First Name: ')
    label.grid(row=2, column=0)
    first_name = Entry(frame)
    first_name.grid(row=2, column=1)

    label = Label(frame, text='Last Name: ')
    label.grid(row=3, column=0)
    last_name = Entry(frame)
    last_name.grid(row=3, column=1)

    button = Button(frame, text='Submit', bg='green', fg='white',
                    command=lambda: register(
                        username=username.get(),
                        password=password.get(),
                        first_name=first_name.get(),
                        last_name=last_name.get()))
    button.grid(row=4, column=1)


def render_main_enter_screen():
    frame = Frame(app, width=200, height=400)
    frame.grid(row=0, column=0, padx=300, pady=30)
    label = Label(text='Welcome to the shop!')
    label.grid(row=1, column=0, pady=30)

    l_btn = Button(frame, text='LogIn', bg='green', fg='white', command=render_login)
    l_btn.grid(row=0, column=0)
    r_btn = Button(frame, text='Register', bg='yellow', fg='black', command=render_register)
    r_btn.grid(row=0, column=1, sticky="e")
