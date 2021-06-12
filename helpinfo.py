from tkinter import *
from tkinter import ttk
from tkinter.ttk import Frame
import webbrowser
global infobanner
def infobanner():
    infowindow = Tk()
    infowindow.title('Информация')
    infowindow.geometry('334x185') #Измените размеры, если у вас НЕ Windows
    infowindow.resizable(height = False, width = False)
    # Геометрия окна ------------------------------------------------------
    mainframe = Frame(infowindow, padding = '3 3 12 12')
    mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
    mainframe.columnconfigure(0, weight = 1)
    mainframe.rowconfigure(0, weight = 1)
    banner = """
 Email Sender - это простая программа, позволяющая
  отправлять электронной почту без необходимости
открывать web-версию или запускать отдельный клиент.
    """
    # Текст ---------------------------------------------------------------
    ttk.Label(mainframe, text = 'Email Sender, v1.4').grid(column = 0, row = 0, sticky = N)
    ttk.Label(mainframe, text = banner).grid(column = 0, row = 1, sticky = W)
    ttk.Label(mainframe, text = '\n\nMatroCholo' ).grid(column = 0, row = 2, sticky = S)
    # Отрисовка -----------------------------------------------------------
    for child in mainframe.winfo_children():
        child.grid_configure(padx = 5, pady = 5)
    infowindow.mainloop()
