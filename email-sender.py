from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Checkbutton
from tkinter.ttk import Progressbar
from tkinter.ttk import Frame
import smtplib
import webbrowser
import mimetypes
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart
def setup(event):
    webbrowser.open_new(r"https://www.google.com/settings/security/lesssecureapps")
def send():
    bar['value'] = 0
    messagebox.showinfo('Уведомление', 'Убедитесь, что вы верно ввели данные')
    addr_from = mail.get()
    addr_to = mail_to.get()
    sub = subject.get()
    passwd = password.get()
    message = message_form.get('1.0', 'end')
    bar['value'] = 25
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
    msg = MIMEMultipart()
    msg['From']    = addr_from                          
    msg['To']      = addr_to                            
    msg['Subject'] = sub                      
    try:
        bar['value'] = 50
        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP(_server, _port)
        server.starttls()
        server.login(addr_from, passwd)
        server.send_message(msg)
        bar['value'] = 75
        server.quit()
        bar['value'] = 100
        messagebox.showinfo('Уведомление', 'Сообщение успешно доставлено')
    except:
        bar['value'] = 75
        messagebox.showerror('Ошибка', 'Сообщение не доставлено')
        bar['value'] = 0
app = Tk()
app.title('Email Sender, v1.1')
app.resizable(height=False, width=False)
mail = StringVar()
password = StringVar()
mail_to = StringVar()
subject = StringVar()
message_form = StringVar()
mainframe = Frame(app, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
ttk.Label(mainframe, text="Почта: ").grid(column=0, row=1, sticky=W)
mail_form = ttk.Entry(mainframe, width=30, textvariable=mail)
mail_form.grid(column=4, row=1, sticky=(W, E))
ttk.Label(mainframe, text="Пароль: ").grid(column=0, row=2, sticky=W)
password_form = ttk.Entry(mainframe, show="*", width=30, textvariable=password)
password_form.grid(column=4, row=2, sticky=(W, E))
ttk.Label(mainframe, text="Почта получателя: ").grid(column=0, row=3, sticky=W)
mail_to_form = ttk.Entry(mainframe, width=30, textvariable=mail_to)
mail_to_form.grid(column=4, row=3, sticky=(W, E))
ttk.Label(mainframe, text="Тема сообщения: ").grid(column=0, row=6, sticky=W)
subject_form = ttk.Entry(mainframe, width=30, textvariable=subject)
subject_form.grid(column=4, row=6, sticky=(W, E))
ttk.Label(mainframe, text="Текст сообщения: ").grid(column=0, row=7, sticky=W)
message_form = Text(mainframe, width=30, height=10)
message_form.grid(column=4, row=7, sticky=(W, E))
send_button = ttk.Button(mainframe, text="Отправить", command=send)
send_button.grid(column=4,row=9,sticky=E)
chk_state = BooleanVar()  
chk_state.set(False)
send_extra = Checkbutton(mainframe, text='Добавить файл', var=chk_state)
send_extra.grid(column=4, row=8, sticky=E)  
bar = Progressbar(mainframe, length=150)
bar['value'] = 0
bar_text = ttk.Label(mainframe, text='Статус отправки: ')
bar_text.grid(column=0, row=8, sticky=W)  
bar.grid(column=0, row=9, sticky=W)  
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
app.mainloop()
