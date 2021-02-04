import json
import os
from PIL import Image, ImageTk
from shop_app.canvas import app
from shop_app.helpers import clean_screen
from tkinter import Button, Label

BASE_DIR = os.path.dirname(__file__)
DB_DIR = os.path.join(BASE_DIR, 'db')
IMAGE_DIR = os.path.join(BASE_DIR, 'images')
PRODUCTS_FILE = os.path.join(DB_DIR, 'products.txt')
USERS_FILE = os.path.join(DB_DIR, 'users.txt')
CURRENT_USER_FILE = os.path.join(DB_DIR, 'current_user.txt')


def update_products(pr_id):
    with open(PRODUCTS_FILE, 'r+') as file:
        products = file.readlines()
        file.seek(0)
        for pr in products:
            product = json.loads(pr)
            if product.get('id') == pr_id:
                product['count'] -= 1
            # TODO: if product count == 0 logic
            file.write(json.dumps(product))
            file.write('\n')


def update_users(logged_user, pr_id):
    with open(USERS_FILE, 'r+') as file:
        users = file.readlines()
        file.seek(0)
        for us in users:
            user = json.loads(us)
            if user.get('username') == logged_user:
                user['products'].append(pr_id)
            file.write(json.dumps(user))
            file.write('\n')


def buy_product(btn):
    pr_id = int(btn.cget('text').split()[-1])
    with open(CURRENT_USER_FILE, 'r') as file:
        logged_user = file.read()
    update_users(logged_user, pr_id)
    update_products(pr_id)
    render_products()


def render_products():
    clean_screen()
    with open(PRODUCTS_FILE, 'r') as file:
        products = file.readlines()
        col = 0
        for pr in products:
            product = json.loads(pr)

            label = Label(text=product.get('name'))
            label.grid(row=0, column=col)

            image = Image.open(os.path.join(IMAGE_DIR, product.get('img_path')))
            image = image.resize((200, 200))
            photo = ImageTk.PhotoImage(image)
            img_label = Label(image=photo)
            img_label.image = photo
            img_label.grid(row=1, column=col)

            label = Label(text=f'In Stock: {product.get("count")}')
            label.grid(row=3, column=col)

            button = Button(app, text=f'Buy {product.get("id")}')
            button.configure(command=lambda b=button: buy_product(b))
            button.grid(row=4, column=col)

            col += 1
