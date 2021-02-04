from tkinter import Tk


def create_app():
    tk = Tk()
    tk.geometry('800x600+0+0')
    tk.title('Shop')
    return tk


app = create_app()