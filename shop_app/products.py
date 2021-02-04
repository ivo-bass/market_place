import json

from shop_app.canvas import app
from shop_app.helpers import clean_screen
from tkinter import Button, Label

PRODUCTS_FILE = 'db/products.txt'


def render_products():
    clean_screen()
    with open(PRODUCTS_FILE, 'r') as file:
        products = file.readlines()
        col = 0
        for pr in products:
            product = json.loads(pr)
            Label(text=product.get('name')).grid(row=0, column=col)

            Button(app, text='Buy').grid(row=2, column=col)
            col += 1
