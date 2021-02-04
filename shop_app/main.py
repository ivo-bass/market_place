from shop_app.authentication import render_main_enter_screen
from shop_app.canvas import app

if __name__ == '__main__':
    render_main_enter_screen()
    app.mainloop()


# Todo: stay logged in
# Todo: Clean current user if not checkbox stay logged in
# Todo: if logged in -> home screen is products page
# Todo: Details page for product
