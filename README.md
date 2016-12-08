# django-journal
A private journal web-app that can be run and maintained on a local machine

This a fork of https://github.com/DjangoGirls/tutorial

##TODO
- [ ] Sticky Posts
- [x] Better Rendering of full posts

##Installation

Make sure you have Python3.5 and django>=1.9 running.

Clone this repo by entering the following in a terminal
```
$ git clone https://github.com/kaushiksk/django-journal.git
```
Setting up the database and creating admin creedentials
```
$ cd django-journal
$ python manage.py migrate
.
.
$ python manage.py createsuperuser
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
