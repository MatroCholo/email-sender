# Необходимые библиотеки -------------------------------------------------
from time import sleep
from tkinter import *
from tkinter import messagebox, filedialog, ttk, Menu
from tkinter.ttk import Checkbutton, Frame, Progressbar
import os
from os import path
import smtplib
# ------------------------------------------------------------------------
import mimetypes
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart
# Функции -----------------------------------------------------------------
def mainWindow():
    # Глобализируем переменные --------------------------------------------
    global loginwindow
    global mail
    global password
    # Основное ------------------------------------------------------------
    loginwindow = Tk()
    loginwindow.title('[Авторизация]')
    loginwindow.geometry('265x100')
    loginwindow.resizable(height = False, width = False)
    # Переменные ----------------------------------------------------------
    mail = StringVar()
    password = StringVar()
    # Геометрия окна ------------------------------------------------------
    mainframe = Frame(loginwindow, padding = '3 3 12 12')
    mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
    mainframe.columnconfigure(0, weight = 1)
    mainframe.rowconfigure(0, weight = 1)
    # Текст ---------------------------------------------------------------
    ttk.Label(mainframe, text = 'Почта:').grid(column = 0, row = 0, sticky = W)
    ttk.Label(mainframe, text = 'Пароль:').grid(column = 0, row = 1, sticky = W)
    # Текстовые формы -----------------------------------------------------
    mail_form = ttk.Entry(mainframe, width = 30, textvariable = mail).grid(column = 1, row = 0, sticky = (W, E))
    # ---------------------------------------------------------------------
    password_form = ttk.Entry(mainframe, show='*', width = 30, textvariable = password).grid(column = 1, row = 1, sticky = (W, E))
    # Функции -------------------------------------------------------------
    login_button = ttk.Button(mainframe, text = 'Войти', command = secondWindow).grid(column = 1,row = 2,sticky = E)
    # Отрисовка -----------------------------------------------------------
    for child in mainframe.winfo_children():
        child.grid_configure(padx = 5, pady = 5)
    loginwindow.mainloop()
def secondWindow():
    # Предупреждение ----------------------------------------------------------
    messagebox.showinfo('[Предупреждение]', 'Убедитесь, что вы ввели верные данные')
    # Закрытие логин-окна -----------------------------------------------------
    loginwindow.destroy()
    # Глобализируем переменные ------------------------------------------------
    global mail_to
    global subject
    global message_form
    global bar
    global delay
    # Основное ----------------------------------------------------------------
    app = Tk()
    app.title('Email Sender [v1.2]')
    app.geometry('510x340')
    app.resizable(height = False, width = False)
    # Переменные -------------------------------------------------------------- 
    mail_to = StringVar()
    subject = StringVar()
    message_form = StringVar()
    delay = IntVar()
    # Геометрия окна ----------------------------------------------------------
    mainframe = Frame(app, padding = '3 3 12 12')
    mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
    mainframe.columnconfigure(0, weight = 1)
    mainframe.rowconfigure(0, weight = 1)
    # Текст -------------------------------------------------------------------
    ttk.Label(mainframe, text = 'Почта получателя: ').grid(column = 0, row = 1, sticky = W)
    ttk.Label(mainframe, text = 'Тема сообщения: ').grid(column = 0, row = 2, sticky = W)
    ttk.Label(mainframe, text = 'Текст сообщения: ').grid(column = 0, row = 3, sticky = W)
    ttk.Label(mainframe, text = 'Таймер (сек): ').grid(column = 4, row = 4, sticky = E)
    # Текстовые формы ---------------------------------------------------------
    mail_to_form = ttk.Entry(mainframe, width = 30, textvariable = mail_to).grid(column = 4, row = 1, sticky = (W, E))
    # -------------------------------------------------------------------------
    subject_form = ttk.Entry(mainframe, width = 30, textvariable = subject).grid(column = 4, row = 2, sticky = (W, E))
    # -------------------------------------------------------------------------
    message_form = Text(mainframe, width = 35, height = 10)
    message_form.grid(column = 4, row = 3, sticky = (W, E))
    # -------------------------------------------------------------------------
    timer = ttk.Entry(mainframe, width = 15, textvariable = delay).grid(column = 4, row = 5, sticky = E)
    # Кнопки ------------------------------------------------------------------
    send_button = ttk.Button(mainframe, text = 'Отправить', command = send)
    send_button.grid(column = 4,row = 6,sticky = E)
    # -------------------------------------------------------------------------
    add_file_button = ttk.Button(mainframe, text='Прикрепить', command=add_files)
    add_file_button.grid(column=0,row=6,sticky=W)
    # Прогресс-бар ------------------------------------------------------------
    bar = Progressbar(mainframe, length = 200)
    bar.grid(column = 0, row = 5, sticky = W)
    bar['value'] = 0
    bar_text = ttk.Label(mainframe, text = 'Статус отправки: ').grid(column = 0, row = 4, sticky = W)
    # Отрисовка ---------------------------------------------------------------
    for child in mainframe.winfo_children():
        child.grid_configure(padx = 5, pady = 5)
    app.mainloop()
def add_files():
    # Глобализируем переменную ------------------------------------------------- 
    global filepath
    # Создаём запрос на выбор файла --------------------------------------------
    filepath = filedialog.askopenfile('r', initialdir = path.dirname(__file__))
    # Узнаём путь файла --------------------------------------------------------
    filepath = filepath.name
def send():
    # Глобализируем переменную ------------------------------------------------- 
    global time
    # Прогресс-бар в начало ----------------------------------------------------
    bar['value'] = 0 
    # Переменные для авторизации в smtp ----------------------------------------
    addr_from = mail.get()
    addr_to = mail_to.get()
    sub = subject.get()
    passwd = password.get()
    message = message_form.get('1.0', 'end')
    time = delay.get()
    # --------------------------------------------------------------------------
    bar['value'] = 25
    # Проверка используемого провайдера ----------------------------------------
    if addr_from[-9:] == 'gmail.com':
        _server = 'smtp.gmail.com'
        _port = 587
    if addr_from[-7:] == 'mail.ru' or addr_from[-5:] == 'bk.ru' or addr_from[-8:] == 'inbox.ru' or addr_from[-7:] == 'list.ru':
        _server = 'smtp.mail.ru'
        _port = 25
    if addr_from[-11:] == 'hotmail.com' or addr_from[-8:] == 'live.com' or addr_from[-7:] == 'msn.com' or addr_from[-12:] == 'passport.com' or addr_from[-11:] == 'outlook.com':
        _server = 'smtp.office365.com'
        _port = 587
    if addr_from[-10:] == 'icloud.com' or addr_from[-6:] == 'me.com' or addr_from[-7:] == 'mac.com':
        _server = 'smtp.mail.me.com'
        _port = 587
    # Работа с smtp -------------------------------------------------------------
    msg = MIMEMultipart()
    msg['From']    = addr_from                          
    msg['To']      = addr_to                            
    msg['Subject'] = sub
    bar['value'] = 50
    # Проверка наличия таймера --------------------------------------------------
    if time == 0:
        # Проверка наличия выбора файлов ----------------------------------------
        if 'filepath' in globals():
            try:
                filename = os.path.basename(filepath)
                ctype, encoding = mimetypes.guess_type(filepath)
                if ctype is None or encoding is not None:
                    ctype = 'application/octet-stream'
                maintype, subtype = ctype.split('/', 1)
                if maintype == 'text':
                    with open(filepath) as fp:
                        file = MIMEText(fp.read(), _subtype=subtype)
                        fp.close()
                elif maintype == 'image':
                    with open(filepath, 'rb') as fp:
                        file = MIMEImage(fp.read(), _subtype=subtype)
                        fp.close()
                elif maintype == 'audio':
                    with open(filepath, 'rb') as fp:
                        file = MIMEAudio(fp.read(), _subtype=subtype)
                        fp.close()
                else:
                    with open(filepath, 'rb') as fp:
                        file = MIMEBase(maintype, subtype)
                        file.set_payload(fp.read())
                        fp.close()
                        encoders.encode_base64(file)
                file.add_header('Content-Disposition', 'attachment', filename=filename)
                msg.attach(file)
                msg.attach(MIMEText(message, 'plain'))
                server = smtplib.SMTP(_server, _port)
                bar['value'] = 75
                server.starttls()
                server.login(addr_from, passwd)
                server.send_message(msg)
                server.quit()
                bar['value'] = 100
                messagebox.showinfo('Уведомление', 'Сообщение отправлено')
            except:
                bar['value'] = 0
                messagebox.showerror('Уведомление', 'Сообщение не отправлено')
        else:
            try:
                msg.attach(MIMEText(message, 'plain'))
                server = smtplib.SMTP(_server, _port)
                server.starttls()
                server.login(addr_from, passwd)
                server.send_message(msg)
                server.quit()
                bar['value'] = 100
                messagebox.showinfo('Уведомление', 'Сообщение отправлено')
            except:
                bar['value'] = 0
                messagebox.showerror('Уведомление', 'Сообщение не отправлено')
    else:
        if 'filepath' in globals():
            try:
                filename = os.path.basename(filepath)
                ctype, encoding = mimetypes.guess_type(filepath)
                if ctype is None or encoding is not None:
                    ctype = 'application/octet-stream'
                maintype, subtype = ctype.split('/', 1)
                if maintype == 'text':
                    with open(filepath) as fp:
                        file = MIMEText(fp.read(), _subtype=subtype)
                        fp.close()
                elif maintype == 'image':
                    with open(filepath, 'rb') as fp:
                        file = MIMEImage(fp.read(), _subtype=subtype)
                        fp.close()
                elif maintype == 'audio':
                    with open(filepath, 'rb') as fp:
                        file = MIMEAudio(fp.read(), _subtype=subtype)
                        fp.close()
                else:
                    with open(filepath, 'rb') as fp:
                        file = MIMEBase(maintype, subtype)
                        file.set_payload(fp.read())
                        fp.close()
                        encoders.encode_base64(file)
                file.add_header('Content-Disposition', 'attachment', filename=filename)
                msg.attach(file)
                msg.attach(MIMEText(message, 'plain'))
                server = smtplib.SMTP(_server, _port)
                bar['value'] = 75
                server.starttls()
                server.login(addr_from, passwd)
                messagebox.showinfo('Уведомление', 'Сообщение будет отправлено')
                sleep(time)
                server.send_message(msg)
                server.quit()
                bar['value'] = 100
            except:
                bar['value'] = 0
                messagebox.showerror('Уведомление', 'Сообщение не отправлено')
        else:
            try:
                msg.attach(MIMEText(message, 'plain'))
                server = smtplib.SMTP(_server, _port)
                server.starttls()
                server.login(addr_from, passwd)
                messagebox.showinfo('Уведомление', 'Сообщение будет отправлено')
                sleep(time)
                server.send_message(msg)
                server.quit()
                bar['value'] = 100
            except:
                bar['value'] = 0
                messagebox.showerror('Уведомление', 'Сообщение не отправлено')
# Запуск ------------------------------------------------------------------------
if __name__ == '__main__':
    mainWindow()
