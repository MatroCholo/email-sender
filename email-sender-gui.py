# Библиотеки -------------------------------------------------
from guizero import App, Text, PushButton, TextBox, Window, MenuBar, Picture
from time import sleep
import datetime                                                  
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Функции -----------------------------------------------------
def are_you_sure():
    app.info('Предупреждение', 'Убедитесь,\n1) что вы верно ввели почту и пароль!\n \
2) что есть доступ к ненадежным приложениям для Gmail!\n \
(myaccount.google.com/lesssecureapps)')
    addr_from = addr_from_box.value
    password = password_box.value
    addr_to = addr_to_box.value
    subject = subject_box.value
    message = message_box.value
    if addr_from[-9:] == 'gmail.com':
        _server = 'smtp.gmail.com'
        _port = 587
    if addr_from[-9:] == 'yandex.ru' or addr_from[-5:] == 'ya.ru':
        _server = 'smtp.yandex.ru'
        _port = 465
    if addr_from[-7:] == 'mail.ru' or addr_from[-5:] == 'bk.ru' or addr_from[-8:] == 'inbox.ru' or addr_from[-7:] == 'list.ru':
        _server = 'smtp.mail.ru'
        _port = 25
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
        print(datetime.datetime.now().strftime("%H:%M:%S"), '- Успешно')
    except:
        print(datetime.datetime.now().strftime("%H:%M:%S"), '- Провалено (скорее всего, сервер закрыл порт)')
    
def logs():
    logs_window.show()
def settings():
    settings_window.show()
def info():
    info_window.show()
def docs():
    docs_window.show()
# Основное -----------------------------------------------------
app = App("Почта v0.1", layout='grid', height=300, width=280)
app.bg='#FFFFFF'
# Картинки -----------------------------------------------------
picture = Picture(app, image="mail.png", grid=[0,0], align='left')
# Менюбар -------------------------------------------------------
logs_window = Window(app, 'Логи', layout='grid', height=300, width=300)
logs_window.visible=0
settings_window = Window(app, 'Настройки', layout='grid', height=300, width=300)
settings_window.visible=0
info_window = Window(app, 'Информация', layout='grid', height=300, width=300)
info_window.visible=0
docs_window = Window(app, 'Документация', layout='grid', height=300, width=300)
docs_window.visible=0
menubar = MenuBar(app,
                  toplevel=["Файл", "Помощь"],
                  options=[
                      [ ["Логи", logs], ["Настройки", settings] ],
                      [ ["Информация", info], ["Документация", docs] ]
                  ])
# Банеры -------------------------------------------------------
logo = Text(app, text="MatroCholo", grid=[0,0], align='left')
logo.text_size=9
name = Text(app, 'Версия v0.1', grid=[1,10], align='right')
name.text_size=5
# Адресат -------------------------------------------------------
addr_from = Text(app, 'Почта: ', grid=[0,1], align='left')
addr_from.text_size=10
addr_from_box = TextBox(app, grid=[1,1], align='left', width=25)
# Пароль --------------------------------------------------------
password = Text(app, 'Пароль: ', grid=[0,2], align='left')
password.text_size=10
password_box = TextBox(app, grid=[1,2], align='left', width=25)
# Получатель ----------------------------------------------------
addr_to = Text(app, 'Почта получателя: ', grid=[0,3], align='left')
addr_to.text_size=10
addr_to_box = TextBox(app, grid=[1,3], align='left', width=25)
# Тема сообщения ------------------------------------------------
subject = Text(app, 'Тема сообщения: ', grid=[0,4], align='left')
subject.text_size=10
subject_box = TextBox(app, grid=[1,4], align='left', width=25)
# Текст сообщения -----------------------------------------------
message = Text(app, 'Текст сообщения: ', grid=[0,5], align='left')
message.text_size=10
message_box = TextBox(app, grid=[1,5], align='left', width=25)
#Кнопки----------------------------------------------------------
send_button = PushButton(app, text='Отправить \nСообщение', command=are_you_sure, grid=[0,9], align='left')
send_button.text_size=9
add_file_button = PushButton(app, text='Прикрепить \nФайл', grid=[1,9], align='right')
add_file_button.text_size=9
# Отрисовка ---------------
app.info('Уведомление', 'Спасибо за использование!')
app.display()
