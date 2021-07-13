from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(352, 200)
        loginWindow.setMinimumSize(QtCore.QSize(352, 200))
        loginWindow.setMaximumSize(QtCore.QSize(352, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        loginWindow.setWindowIcon(icon)
        loginWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(loginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.password_form = QtWidgets.QLineEdit(self.centralwidget)
        self.password_form.setGeometry(QtCore.QRect(180, 31, 161, 31))
        self.password_form.setMouseTracking(True)
        self.password_form.setWhatsThis("")
        self.password_form.setAutoFillBackground(False)
        self.password_form.setStyleSheet("background-color: #ffffff;\n"
"border-radius: 10px;\n"
"")
        self.password_form.setObjectName("password_form")
        self.mail_from_form = QtWidgets.QLineEdit(self.centralwidget)
        self.mail_from_form.setGeometry(QtCore.QRect(10, 31, 161, 31))
        self.mail_from_form.setMouseTracking(True)
        self.mail_from_form.setWhatsThis("")
        self.mail_from_form.setAutoFillBackground(False)
        self.mail_from_form.setStyleSheet("background-color: rgb(255,255,255);\n"
"border-radius:10px;\n"
"")
        self.mail_from_form.setObjectName("mail_from_form")
        self.mail_text = QtWidgets.QLabel(self.centralwidget)
        self.mail_text.setGeometry(QtCore.QRect(10, 10, 35, 16))
        self.mail_text.setObjectName("mail_text")
        self.mail_to_text = QtWidgets.QLabel(self.centralwidget)
        self.mail_to_text.setGeometry(QtCore.QRect(180, 10, 41, 16))
        self.mail_to_text.setObjectName("mail_to_text")
        self.site_button = QtWidgets.QPushButton(self.centralwidget)
        self.site_button.setGeometry(QtCore.QRect(10, 160, 101, 31))
        self.site_button.setMouseTracking(False)
        self.site_button.setStyleSheet("QPushButton {\n"
"    background-color: #ffffff;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f7f7f7;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e7e7e7;\n"
"    border-radius: 10px;\n"
"}")
        self.site_button.setObjectName("site_button")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(240, 160, 101, 31))
        self.login_button.setMouseTracking(False)
        self.login_button.setStyleSheet("QPushButton {\n"
"    background-color: #ffffff;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f7f7f7;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e7e7e7;\n"
"    border-radius: 10px;\n"
"}")
        self.login_button.setObjectName("login_button")
        loginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)
        loginWindow.setTabOrder(self.mail_from_form, self.password_form)
        loginWindow.setTabOrder(self.password_form, self.login_button)
        loginWindow.setTabOrder(self.login_button, self.site_button)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "Авторизация"))
        self.password_form.setToolTip(_translate("loginWindow", "<html><head/><body><p>Введите текст</p></body></html>"))
        self.mail_from_form.setToolTip(_translate("loginWindow", "<html><head/><body><p>Введите текст</p></body></html>"))
        self.mail_text.setText(_translate("loginWindow", "Почта:"))
        self.mail_to_text.setText(_translate("loginWindow", "Пароль:"))
        self.site_button.setText(_translate("loginWindow", "Сайт проекта"))
        self.login_button.setText(_translate("loginWindow", "Авторизация"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = QtWidgets.QMainWindow()
    ui = Ui_loginWindow()
    ui.setupUi(loginWindow)
    loginWindow.show()
    sys.exit(app.exec_())
