<h1 align="center">Email Sender, v1.5</h1>
<h4 align="center">Email Sender - это простая программа, позволяющая отправлять электронной почту без необходимости открывать Веб-версию или запускать отдельный клиент.</h4>

## Предупреждения:
- Для работы программы необходим **доступ в Интернет**,
- Убедитесь, что вы используете последнюю версию **Email Sender**,
- Убедитесь, что вы используете **Python 3.x** (если скачали .py),
- Убедитесь, что вы включили **SMTP** в настройках вашей почты,
- Убедитесь, что вы открыли доступ для **незащищенных приложений (для Gmail)**,
- Программа **не собирает и не отправляет персональные данные третьим лицам!**

## Особенности:
- Поддерживаются **Google Mail, Microsoft Mail, Mail.ru и Apple iCloud**,
- Возможность отправки **любых файлов**,
- Возможность отправки **отложенного** письма.

## Использование:
**Windows:**
- Скачайте **.exe-файл** по **[ссылке](https://github.com/MatroCholo/email-sender/releases)**
- Запустите **email-sender.exe**

**Linux:**
- Корректная работа **не гарантируется**. Возможны неправильная отрисовка и неработоспособность функций.
- Установите **Python 3.x** и **git** в соответствии с вашим дистрибутивом,
- Установите модуль **validate_email** (pip install validate_email)
- Установите библиотеку **PyQt5** (pip install pyqt5)
- git clone **https://github.com/MatroCholo/email-sender**
- cd **email-sender/**
- python **email-sender.py**

## Ручная конвертация .py в .exe:
- Установите **Python 3.x**.
- Нажмите **Windows + R**, введите **cmd** и нажмите **Enter**,
- В открывшемся окне введите **pip install pyinstaller**,
- После установки введите:
**pyinstaller C:\Directory\file.py --onefile --noconsole --icon C:\Directory\file.icon**, где
- - **pyinstaller** - **команда конвертирования**,
- - **C:\Directory\file.py** - **путь к файлу с расширением .py**,
- - **--onefile** - **конвертация в один файл**,
- - **--noconsole** - **запуск сконвертированного файла без консоли (для программ с GUI)**,
- - **--icon C:\Directory\file.icon** - **добавление иконки и путь к ней (необязательно)**.

## Поддерживаемые версии:

| Версия       | Поддержка          |
| -------------| ------------------ |
| v1.5         | :white_check_mark: |
| <v1.4.2      | :x:                |

## Обратная связь:
- Telegram: https://t.me/MatroCholo
