from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(501, 476)
        MainWindow.setMinimumSize(QtCore.QSize(501, 476))
        MainWindow.setMaximumSize(QtCore.QSize(501, 476))
        MainWindow.setMouseTracking(False)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttons = QtWidgets.QGroupBox(self.centralwidget)
        self.buttons.setGeometry(QtCore.QRect(10, 380, 481, 91))
        self.buttons.setTitle("")
        self.buttons.setObjectName("buttons")
        self.add_file_button = QtWidgets.QPushButton(self.buttons)
        self.add_file_button.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.add_file_button.setMouseTracking(False)
        self.add_file_button.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.add_file_button.setObjectName("add_file_button")
        self.send_button = QtWidgets.QPushButton(self.buttons)
        self.send_button.setGeometry(QtCore.QRect(10, 50, 101, 31))
        self.send_button.setMouseTracking(False)
        self.send_button.setStyleSheet("QPushButton {\n"
"    background-color: #272727;\n"
"    color: #fff;\n"
"    border-radius: 15px;\n"
"    font: 63 12pt \"Qanelas SemiBold\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #303030;\n"
"    color: #fff;\n"
"    border-radius: 15px;\n"
"    font: 63 12pt \"Qanelas SemiBold\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #343434;\n"
"    color: #fff;\n"
"    border-radius: 15px;\n"
"    font: 63 12pt \"Qanelas SemiBold\";\n"
"}")
        self.send_button.setObjectName("send_button")
        self.timer_form = QtWidgets.QLineEdit(self.buttons)
        self.timer_form.setGeometry(QtCore.QRect(380, 40, 91, 31))
        self.timer_form.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.timer_form.setObjectName("timer_form")
        self.timer_text = QtWidgets.QLabel(self.buttons)
        self.timer_text.setGeometry(QtCore.QRect(380, 10, 68, 16))
        self.timer_text.setObjectName("timer_text")
        self.email = QtWidgets.QGroupBox(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(10, 10, 481, 361))
        self.email.setTitle("")
        self.email.setObjectName("email")
        self.message_text_text = QtWidgets.QLabel(self.email)
        self.message_text_text.setGeometry(QtCore.QRect(10, 80, 92, 16))
        self.message_text_text.setObjectName("message_text_text")
        self.message_form = QtWidgets.QTextEdit(self.email)
        self.message_form.setGeometry(QtCore.QRect(10, 102, 461, 251))
        self.message_form.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;")
        self.message_form.setObjectName("message_form")
        self.mail_to_text = QtWidgets.QLabel(self.email)
        self.mail_to_text.setGeometry(QtCore.QRect(10, 10, 98, 16))
        self.mail_to_text.setObjectName("mail_to_text")
        self.mail_to_form = QtWidgets.QLineEdit(self.email)
        self.mail_to_form.setGeometry(QtCore.QRect(10, 40, 221, 31))
        self.mail_to_form.setMouseTracking(True)
        self.mail_to_form.setWhatsThis("")
        self.mail_to_form.setAutoFillBackground(False)
        self.mail_to_form.setStyleSheet("background-color: rgb(255,255,255);\n"
"border-radius:10px;\n"
"")
        self.mail_to_form.setObjectName("mail_to_form")
        self.subject_text_text = QtWidgets.QLabel(self.email)
        self.subject_text_text.setGeometry(QtCore.QRect(240, 10, 87, 16))
        self.subject_text_text.setObjectName("subject_text_text")
        self.subject_form = QtWidgets.QLineEdit(self.email)
        self.subject_form.setGeometry(QtCore.QRect(240, 40, 231, 31))
        self.subject_form.setMouseTracking(True)
        self.subject_form.setWhatsThis("")
        self.subject_form.setAutoFillBackground(False)
        self.subject_form.setStyleSheet("background-color: rgb(255,255,255);\n"
"border-radius:10px;\n"
"")
        self.subject_form.setObjectName("subject_form")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Email Sender, v1.5"))
        self.add_file_button.setText(_translate("MainWindow", "Файл"))
        self.send_button.setText(_translate("MainWindow", "Отправить"))
        self.timer_text.setText(_translate("MainWindow", "Таймер (сек):"))
        self.message_text_text.setText(_translate("MainWindow", "Текст сообщения:"))
        self.mail_to_text.setText(_translate("MainWindow", "Почта получателя:"))
        self.mail_to_form.setToolTip(_translate("MainWindow", "<html><head/><body><p>Введите текст</p></body></html>"))
        self.subject_text_text.setText(_translate("MainWindow", "Тема сообщения:"))
        self.subject_form.setToolTip(_translate("MainWindow", "<html><head/><body><p>Введите текст</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
