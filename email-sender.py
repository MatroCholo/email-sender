#!/usr/bin/python3
#-*- coding: utf-8 -*-
# Необходимые библиотеки -------------------------------------------------
import sys
try:
    import mimetypes
    import os
    import smtplib
    import webbrowser
    from os import path
    from time import sleep
    from email import encoders
    from email.mime.audio import MIMEAudio
    from email.mime.base import MIMEBase
    from email.mime.image import MIMEImage
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
except ImportError:
    print('Критическая ошибка! Убедитесь, что Python 3.x верно установлен.')
    sys.exit(1)
try:
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget, QFileDialog
    from gui import Ui_MainWindow
    from login import Ui_loginWindow
except ImportError:
    print('Критическая ошибка! Убедитесь, что библиотека PyQT5 установлена и все файлы были скачаны полностью.')
    sys.exit(1)
# Окно авторизации -----------------------------------------------------------
def loginwindow():
    # Построение окна --------------------------------------------------------
    login_app = QtWidgets.QApplication(sys.argv)
    loginWindow = QtWidgets.QMainWindow()
    login_ui = Ui_loginWindow()
    login_ui.setupUi(loginWindow)
    loginWindow.show()
    # Функция для закрытия окна авторизации ----------------------------------
    def close_():
        # Глобализируем переменные -------------------------------------------
        global mail_from
        global password
        # Извлекаем данные ---------------------------------------------------
        mail_from = login_ui.mail_from_form.text()
        password = login_ui.password_form.text()
        # Закрываем окно -----------------------------------------------------
        loginWindow.close()
    # Функция для открытия сайта проета --------------------------------------
    def open_site():
        webbrowser.open_new('https://github.com/MatroCholo/email-sender')
    # Применяем функции выше для кнопок --------------------------------------
    login_ui.login_button.clicked.connect(close_)
    login_ui.site_button.clicked.connect(open_site)
    # Отрисовка окна ---------------------------------------------------------
    login_app.exec_()
    # Нужно, чтобы при закрытии окна авторизации не было ошибок --------------
    try:
        main(mail_from, password)
    except:
        pass
# Главное окно ---------------------------------------------------------------
def main(mail_from, password):
    # Построение окна --------------------------------------------------------
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # Функция для объявления ошибок ------------------------------------------
    def error():
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText('Что-то пошло не так. Проверьте введённые данные!')
        msg.setWindowTitle("Ошибка!")
        msg.exec_()
    # Функция для объявления успешно выполненных задач -----------------------
    def success():
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText('Письмо отправлено')
        msg.setWindowTitle("Успех")
        msg.exec_()
    # Функция выбора файла ---------------------------------------------------
    def add_files():
        # Глобализируем переменную -------------------------------------------
        global filepath
        # Создаём запрос на выбор файла --------------------------------------
        filepath = QFileDialog.getOpenFileName()[0]
    # Функция отправки почты -------------------------------------------------
    def send():
        # Извлекаем данные из переменных -------------------------------------
        addr_from = mail_from
        passwd = password
        addr_to = ui.mail_to_form.text()
        sub = ui.subject_form.text()
        message = ui.message_form.toPlainText()
        time = int(ui.timer_form.text())
        # Проверка используемого провайдера ----------------------------------
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
        # Проверка наличия выбора файлов ----------------------------------------
        if 'filepath' in globals():
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
            try:
                file.add_header('Content-Disposition', 'attachment', filename=filename)
                msg.attach(file)
                msg.attach(MIMEText(message, 'plain'))
                server = smtplib.SMTP(_server, _port)
                server.starttls()
                server.login(addr_from, passwd)
                sleep(time)
                server.send_message(msg)
                server.quit()
                success()
            except:
                error()
        else:
            try:
                msg.attach(MIMEText(message, 'plain'))
                server = smtplib.SMTP(_server, _port)
                server.starttls()
                server.login(addr_from, passwd)
                sleep(time)
                server.send_message(msg)
                server.quit()
                success()
            except:
               error()
    # Применяем функции выше для кнопок --------------------------------------
    ui.send_button.clicked.connect(send)
    ui.add_file_button.clicked.connect(add_files)
    # Отрисовка окна ---------------------------------------------------------
    sys.exit(app.exec_())

# Если программа запущена как программа то -----------------------------------
if __name__ == '__main__':
    try:
        loginwindow()
    except:
        print('Ошибка!')
