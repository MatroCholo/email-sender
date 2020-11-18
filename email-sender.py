# Необходимые библиотеки -------------------------------------
from guizero import App, Box, MenuBar, Picture, PushButton, Text, TextBox, Window
import smtplib
import os
import mimetypes
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart
# Функции -----------------------------------------------------
def send():
    app.info('Уведомление', 'Убедитесь, что вы верно ввели данные')
    addr_from = addr_from_box.value
    password = password_box.value
    addr_to = addr_to_box.value
    subject = subject_box.value
    message = message_box.value
    if addr_from[-9:] == 'gmail.com':
        _server = 'smtp.gmail.com'
        _port = 587
    if addr_from[-7:] == 'mail.ru' or addr_from[-5:] == 'bk.ru' or addr_from[-8:] == 'inbox.ru' or addr_from[-7:] == 'list.ru':
        _server = 'smtp.mail.ru'
        _port = 25
    if addr_from[-11:] == 'hotmail.com' or addr_from[-8:] == 'live.com' or addr_from[-7:] == 'msn.com' or addr_from[-12:] == 'passport.com' or addr_from[-11:] == 'outlook.com':
        _server = 'smtp.office365.com'
        _port = 587
    #if addr_from[-10:] == 'icloud.com' or addr_from[-6:] == 'me.com' or addr_from[-7:] == 'mac.com':
        #_server = 'smtp.mail.me.com'
        #_port = 587
    msg = MIMEMultipart()
    msg['From']    = addr_from                          
    msg['To']      = addr_to                            
    msg['Subject'] = subject                       
    try:
        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP(_server, _port)
        server.starttls()
        server.login(addr_from, password)
        server.send_message(msg)
        server.quit()
        app.info('Уведомление', 'Сообщение успешно доставлено')
    except:
        app.error('Ошибка', 'Сообщение не доставлено')
def send_files():
    app.info('Уведомление', 'Убедитесь, что вы верно ввели данные')
    addr_from = addr_from_box.value
    password = password_box.value
    addr_to = addr_to_box.value
    subject = subject_box.value
    message = message_box.value
    if addr_from[-9:] == 'gmail.com':
        _server = 'smtp.gmail.com'
        _port = 587
    if addr_from[-7:] == 'mail.ru' or addr_from[-5:] == 'bk.ru' or addr_from[-8:] == 'inbox.ru' or addr_from[-7:] == 'list.ru':
        _server = 'smtp.mail.ru'
        _port = 25
    if addr_from[-11:] == 'hotmail.com' or addr_from[-8:] == 'live.com' or addr_from[-7:] == 'msn.com' or addr_from[-12:] == 'passport.com' or addr_from[-11:] == 'outlook.com':
        _server = 'smtp.office365.com'
        _port = 587
    #if addr_from[-10:] == 'icloud.com' or addr_from[-6:] == 'me.com' or addr_from[-7:] == 'mac.com':
        #_server = 'smtp.mail.me.com'
        #_port = 587
    msg = MIMEMultipart()
    msg['From']    = addr_from                          
    msg['To']      = addr_to                            
    msg['Subject'] = subject                       
    try:
        filepath = app.select_file(title="Выберите файл", folder=".", filetypes=[["All files", ".*"]], save=False)
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
        server.starttls()
        server.login(addr_from, password)
        server.send_message(msg)
        server.quit()
        app.info('Уведомление', 'Сообщение успешно доставлено')
    except:
        app.error('Уведомление', 'Сообщение не доставлено')
# Для закрытия окон -------------------------------------------------------
def close():
    app.destroy()
def docs_close():
    docs_window.hide()
def info_close():
    info_window.hide()
def thanks_close():
    thanks_window.hide()
# Для менюбара ---------------------------------------------------
def info():
    info_window.show()
def docs():
    docs_window.show()
def thanks():
    thanks_window.show()
# Основное -----------------------------------------------------
app = App('Email Sender, v1.0.4', height=300, width=337)
app.bg='#FDFDFD'
# Боксы для корректной отрисовки -------------------------------
title_box = Box(app, layout='grid', align='top', width='fill')
main_box = Box(app, align='top', width='fill')
name_box = Box(main_box, align='top', width='fill')
button_box = Box(app, align='bottom', width='fill')
# Боксы внутри уже существующих боксов, для точнейшей отрисовки-
mail_box = Box(name_box, align='top', width='fill')
pass_box = Box(name_box, align='top', width='fill')
mail_to_box = Box(name_box, align='top', width='fill')
sub_box = Box(name_box, align='top', width='fill')
msg_box = Box(name_box, align='top', width='fill')
# Картинка с логотипом -----------------------------------------
logo = Picture(title_box, image='logo.png', grid=[0,0])
# Окна из менюбара ---------------------------------------------
info_window = Window(app, 'Информация', layout='grid', height=145, width=270)
info_window.bg='#FDFDFD'
info_logo = Picture(info_window, image='info_logo.png', grid=[0,0])
info_text = Text(info_window, '', grid=[0,1])
info_window.hide()
# --------------------------------------------------------------
docs_window = Window(app, 'Документация', layout='grid', height=166, width=271)
docs_window.bg='#FDFDFD'
docs_logo = Picture(docs_window, image='docs.png', grid=[0,0])
docs_text = Text(docs_window, '', grid=[0,1])
docs_window.hide()
# --------------------------------------------------------------
thanks_window = Window(app, 'Благодарности', layout='grid', height=166, width=271)
thanks_window.bg='#FDFDFD'
thanks_logo = Picture(thanks_window, image='thanks.png', grid=[0,0])
thanks_text = Text(thanks_window, '', grid=[0,1])
thanks_window.hide()
# Текст --------------------------------------------------------
addr_from = Text(mail_box, 'Почта', align='left')
addr_from.text_size=10
addr_from.font='Open Sans'
# --------------------------------------------------------------
password = Text(pass_box, 'Пароль', align='left')
password.text_size=10
password.font='Open Sans'
# --------------------------------------------------------------
addr_to = Text(mail_to_box, 'Почта получателя', align='left')
addr_to.text_size=10
addr_to.font='Open Sans'
# --------------------------------------------------------------
subject = Text(sub_box, 'Тема сообщения', align='left')
subject.text_size=10
subject.font='Open Sans'
# --------------------------------------------------------------
message = Text(msg_box, 'Текст сообщения', align='left')
message.text_size=10
message.font='Open Sans'
# Формы для ввода текста ---------------------------------------
addr_from_box = TextBox(mail_box, align='right', width=35)
addr_from_box.bg = '#FBFBFB'
# --------------------------------------------------------------
password_box = TextBox(pass_box, align='right', width=35)
password_box.bg = '#FBFBFB'
# --------------------------------------------------------------
addr_to_box = TextBox(mail_to_box, align='right', width=35)
addr_to_box.bg = '#FBFBFB'
# --------------------------------------------------------------
subject_box = TextBox(sub_box, align='right', width=35)
subject_box.bg = '#FBFBFB'
# --------------------------------------------------------------
message_box = TextBox(msg_box, align='right', width=35)
message_box.bg='#FBFBFB'
# Отправка без файлов -------------------------------------------
send_button = PushButton(button_box, text='Отправить\nписьмо', command=send, height=2, width=10, align='left')
send_button.text_size=10
send_button.font='Open Sans'
send_button.bg='#FCFCFC'
# Отправка с файлами --------------------------------------------
send_extra_button = PushButton(button_box, text='Отправить письмо\nс файлом', command=send_files, height=2, width=13, align='right')
send_extra_button.text_size=9
send_extra_button.font='Open Sans'
send_extra_button.bg='#FCFCFC'
# Менюбар -------------------------------------------------------
menubar = MenuBar(app,
                  toplevel=['Файл', 'Помощь'],
                  options=[
                      [ ['Информация', info] ],
                      [ ['Документация', docs], ['Благодарности', thanks] ]
                  ])
# Отрисовка ------------------------------------------------------
app.display()
