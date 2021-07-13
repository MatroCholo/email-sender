<h1 align="center">Email Sender, v1.5.1</h1>
<h4 align="center">Email Sender - это простая программа, позволяющая отправлять электронной почту без необходимости открывать Веб-версию или запускать отдельный клиент.</h4>

## Предупреждения:
- Для работы программы необходим **доступ в Интернет**,
- Убедитесь, что вы используете последнюю версию **Email Sender**,
- Убедитесь, что вы используете **Python 3.x** (для .py),
- Убедитесь, что вы установили библиотеку PyQT5 и модуль validate email (для .py)
- Убедитесь, что вы включили **SMTP** в настройках вашей почты,
- Убедитесь, что вы открыли доступ для **незащищенных приложений (для Gmail)**,
- Программа **не собирает и не отправляет персональные данные третьим лицам!**

## Особенности:
- Поддерживаются **Google Mail, Microsoft Mail, Mail.ru и Apple iCloud**,
- Возможность отправки **любых файлов**,
- Возможность отправки **отложенного** письма.

## Использование:
**Windows:**
- Скачайте **.exe-файл** и **иконку** по **[ссылке](https://github.com/MatroCholo/email-sender/releases)**
- Запустите **email-sender.exe**

**Linux:**
- Установите **Python 3.x**, **pip3** и **git** в соответствии с вашим дистрибутивом,
- Установите модуль **validate_email** (pip3 install validate_email)
- Установите библиотеку **PyQt5** (pip3 install pyqt5)
- git clone **https://github.com/MatroCholo/email-sender**
- cd **email-sender/** && python3 **email-sender.py**

## Ручная конвертация .py в .exe:
- Установите **Python 3.x**.
- Нажмите **Windows + R**, введите **cmd** и нажмите **Enter**,
- В открывшемся окне введите **pip install pyinstaller pyqt5 pyqt5-tools**,
- После установки введите:

**pyuic5 -x C:\Directory\file.ui -o C:\Directory\file.py**, где
- **pyuic5** - **команда конвертирования .ui файла с GUI в .py**
- **C:\Directory\file.ui** - **путь к файлу с расширением .ui** 
- **C:\Directory\file.py** - **готовый файл**

**pyinstaller C:\Directory\file.py --onefile --noconsole --icon C:\Directory\file.icon**, где
- - **pyinstaller** - **команда конвертирования**,
- - **C:\Directory\file.py** - **путь к файлу с расширением .py**,
- - **--onefile** - **конвертация в один файл**,
- - **--noconsole** - **запуск сконвертированного файла без консоли (для программ с GUI)**,
- - **--icon C:\Directory\file.icon** - **добавление иконки и путь к ней (необязательно)**.

## Поддерживаемые версии:

| Версия       | Поддержка          |
| -------------| ------------------ |
| v1.5.1       | :white_check_mark: |
| v1.5         | :x:                |
| v1.4.2       | :white_check_mark: |
| <v1.4.1      | :x:                |


## Обратная связь:
- Telegram: https://t.me/MatroCholo
