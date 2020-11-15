# Библиотеки -------------------------------------------------
from guizero import App, Text, PushButton, TextBox, Window, MenuBar, Picture, ListBox
from time import sleep
import datetime
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Функции -----------------------------------------------------
def are_you_sure():
    addr_from = addr_from_box.value
    password = password_box.value
    addr_to = addr_to_box.value
    subject = subject_box.value
    message = message_box.value
    # Данные для корректной работы почтовых сервисов ----------
    if addr_from[-9:] == 'gmail.com':
        _server = 'smtp.gmail.com'
        _port = 587
    if addr_from[-9:] == 'yandex.ru' or addr_from[-5:] == 'ya.ru':
        _server = 'smtp.yandex.ru'
        _port = 465
    if addr_from[-7:] == 'mail.ru' or addr_from[-5:] == 'bk.ru' or addr_from[-8:] == 'inbox.ru' or addr_from[-7:] == 'list.ru':
        _server = 'smtp.mail.ru'
        _port = 25
    # Значения для корректной работы почты ---------------------
    msg = MIMEMultipart()
    msg['From']    = addr_from                          
    msg['To']      = addr_to                            
    msg['Subject'] = subject
    # Выполнение ------------------------------------------------
    try:
        time = datetime.datetime.now()
        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP(_server, _port)
        server.starttls()
        server.login(addr_from, password)
        server.send_message(msg)
        server.quit()
        app.info('Уведомление', 'Сообщение успешно доставлено')
    except:
        app.info('Уведомление', 'Сообщение не доставлено')
def settings():
    settings_window.show()
def info():
    info_window.show()
def docs():
    docs_window.show()
# Основное -----------------------------------------------------
app = App("Почта v0.2", layout='grid', height=165, width=270)
app.bg='#FDFDFD'
# Менюбар -------------------------------------------------------
settings_window = Window(app, 'Настройки', layout='grid', height=170, width=277)
settings_window.hide()
info_window = Window(app, 'Информация', layout='grid', height=170, width=277)
info_window.hide()
docs_window = Window(app, 'Документация', layout='grid', height=170, width=277)
docs_window.hide()
menubar = MenuBar(app,
                  toplevel=["Файл", "Помощь"],
                  options=[
                      [ ["Настройки", settings] ],
                      [ ["Информация", info], ["Документация", docs] ]
                  ])
# Адресат -------------------------------------------------------
addr_from = Text(app, 'Почта: ', grid=[0,0], align='left')
addr_from.text_size=9
addr_from_box = TextBox(app, grid=[1,0], align='left', width=25)
addr_from_box.bg = '#FBFBFB'
# Пароль --------------------------------------------------------
password = Text(app, 'Пароль: ', grid=[0,1], align='left')
password.text_size=9
password_box = TextBox(app, grid=[1,1], align='left', width=25)
password_box.bg = '#FBFBFB'
# Получатель ----------------------------------------------------
addr_to = Text(app, 'Почта получателя: ', grid=[0,2], align='left')
addr_to.text_size=9
addr_to_box = TextBox(app, grid=[1,2], align='left', width=25)
addr_to_box.bg = '#FBFBFB'
# Тема сообщения ------------------------------------------------
subject = Text(app, 'Тема сообщения: ', grid=[0,3], align='left')
subject.text_size=9
subject_box = TextBox(app, grid=[1,3], align='left', width=25)
subject_box.bg = '#FBFBFB'
# Текст сообщения -----------------------------------------------
message = Text(app, 'Текст сообщения: ', grid=[0,4], align='left')
message.text_size=9
message_box = TextBox(app, grid=[1,4], align='left', width=25)
message_box.bg='#FBFBFB'
# Кнопки----------------------------------------------------------
send_button = PushButton(app, text='Отправить\n сообщение', command=are_you_sure, grid=[0,6], align='left')
send_button.text_size=9
send_button.bg='#FCFCFC'
add_file_button = PushButton(app, text='Прикрепить\n вложение', grid=[1,6], align='right')
add_file_button.text_size=9
add_file_button.bg='#FCFCFC'
# Отрисовка ------------------------------------------------------
app.info('Уведомление', 'Это бета версия. Стабильность не обещается!')
app.display()
