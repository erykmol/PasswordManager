# PasswordManager
This application is a simple web-based Password manager written in python programming language in Django framework, that stores website information such as its name and url and users login and password associated with that website as a single entry which the user can edit and delete.

# Design
All design choices I've made for this application are based on the skill/knowledge level I currently have with the framework and recommended solutions suggested by the creators of the Django framework in the documentation such as:

Hashing users passwords with a built-in PBKDF2 algorithm with a SHA256 hash which a password stretching mechanism used by default and is recommended by NIST.

Using SQLite as a database which is easier to use during the development of the application.

Using the MVC design pattern to easily separate database, controller functions, and html templates.

# Instructions

Python is already installed on mac, but I was using Python3 so it would be good to install it also from https://www.python.org/downloads/.

Also, Django will be required. To install it using pip, just type in `pip install django`.

After that, download the entire application into some folder, then open the terminal and navigate to the directory where manage.py file resides. After that, run command `python3 manage.py runserver` which will create a localhost address that will be displayed in the terminal, it's usually http://127.0.0.1:8000/. The last thing to do is to copy the url from terminal and paste it to the browser which should be showing the login page.


