# django-journal
A private journal web-app that can be run and maintained on a local machine

## Requirements
This app require Python3, django>=1.9 and django-tinymce to run.

## Installation

```
(myenv)$ cd django-journal
(myenv)$ pip install django django-tinymce
(myenv)$ python manage.py migrate
.
.
(myenv)$ python manage.py createsuperuser
```

Choose your preferred username, supple any dummy email, and choose your password.

Make sure you remember the username and password.

To start the server run
`python manage.py runserver [port]`

If the port is not specified the server runs at port 8000 by default.

*Make sure you're in the project root directory every time you run these commands*

Your blog should now be up and running at `http://127.0.0.1:8000/`.

To add posts and categories go to `http://127.0.0.1:8000/admin`, login with your credentials and you should be good to go!

Also, make sure you `git pull` every once in a while to stay updated with new changes!
