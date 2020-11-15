# Библиотеки -------------------------------------------------
from guizero import App, Text, CheckBox, PushButton, TextBox, Window, MenuBar, Picture
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Функции -----------------------------------------------------
def send():
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
        app.info('Уведомление', 'Сообщение успешно доставлено')
    except:
        app.error('Уведомление', 'Сообщение не доставлено')
def close():
    app.destroy()
def update():
    app.info('Уведомление', 'Установлена последняя версия')
def info():
    info_window.show()
def docs():
    docs_window.show()
def thanks():
    thanks_window.show()
def testinfo():
    app.info('Проверка', 'Уведомление')
def testerror():
    app.error('Проверка', 'Ошибка')
def testwarn():
    app.warn('Проверка', 'Предупреждение')
def add_file():
    app.select_file(title="Выберите файл", folder=".", filetypes=[["All files", ".*"]], save=False)
# Основное -----------------------------------------------------
app = App("Почта v0.3", layout='grid', height=205, width=325)
app.bg='#FDFDFD'
logo = Picture(app, image='logo.png', grid=[0,0])
info_window = Window(app, 'Информация', layout='grid', height=165, width=270)
info_logo = Picture(info_window, image='info_logo.png', grid=[0,0])
docs_window = Window(app, 'Документация', layout='grid', height=165, width=270)
docs_logo = Picture(docs_window, image='docs.png', grid=[0,0])
thanks_window = Window(app, 'Благодарности', layout='grid', height=165, width=270)
thanks_logo = Picture(thanks_window, image='thanks.png', grid=[0,0])
info_window.hide()
docs_window.hide()
thanks_window.hide()
# Менюбар -------------------------------------------------------
menubar = MenuBar(app,
                  toplevel=["Файл", 'Опции', "Помощь"],
                  options=[
                      [ ["Информация", info],  ['Проверка обновлений', update], ["Закрыть программу", close], ],
                      [ ['Вызвать тестовое уведомление', testinfo], ['Вызвать тестовую ошибку', testerror], ['Вызвать тестовое предупреждение',testwarn] ],
                      [ ["Документация", docs], ['Благодарности', thanks] ]
                  ])
# Адресат -------------------------------------------------------
addr_from = Text(app, 'Почта: ', grid=[0,1], align='left')
addr_from.text_size=9
addr_from_box = TextBox(app, grid=[1,1], align='left', width=25)
addr_from_box.bg = '#FBFBFB'
# Пароль --------------------------------------------------------
password = Text(app, 'Пароль: ', grid=[0,2], align='left')
password.text_size=9
password_box = TextBox(app, grid=[1,2], align='left', width=25)
password_box.bg = '#FBFBFB'
# Получатель ----------------------------------------------------
addr_to = Text(app, 'Почта получателя: ', grid=[0,3], align='left')
addr_to.text_size=9
addr_to_box = TextBox(app, grid=[1,3], align='left', width=25)
addr_to_box.bg = '#FBFBFB'
# Тема сообщения ------------------------------------------------
subject = Text(app, 'Тема сообщения: ', grid=[0,4], align='left')
subject.text_size=9
subject_box = TextBox(app, grid=[1,4], align='left', width=25)
subject_box.bg = '#FBFBFB'
# Текст сообщения -----------------------------------------------
message = Text(app, 'Текст сообщения: ', grid=[0,5], align='left')
message.text_size=9
message_box = TextBox(app, grid=[1,5], align='left', width=25)
message_box.bg='#FBFBFB'
# Кнопки----------------------------------------------------------
send_button = PushButton(app, text='Отправить\n сообщение', command=send, grid=[0,6], align='left')
send_button.text_size=9
send_button.bg='#FCFCFC'
add_file_button = PushButton(app, text='Прикрепить\n вложение', command=add_file, grid=[1,6], align='right')
add_file_button.text_size=9
add_file_button.bg='#FCFCFC'
# Отрисовка ------------------------------------------------------
app.display()
