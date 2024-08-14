# django-mysite

## Introduction

This is a simple website. It contains a questionary with several choice options. Question and Choices are stroed in the MySQL database **mysite**. It is needed to be configured in advance before starting the server. The official [documentation](https://docs.djangoproject.com/en/5.0/) helped me a lot in learning how to build a webpage with django.

## Configuration of the database

Set-up MySQL Server on Ubuntu and configure database and users. User and password must match the database configurations in **settings.py**.

```
create database mysite;
CREATE USER <user>@'localhost' IDENTIFIED BY <passwd>;
GRANT PRIVILEGE ...
FLUSH PRIVILEGES
```

Then define an admin-user for the webpage: `python manage.py createsuperuser`

## Migrations

The app configuration of _polls_ are migrated to the database. <br>
`python manage.py migrate` <br>
`python manage.py sqlmigrate polls 0001`

## fill database with data - questions and choices

The MySQL database can be filled with questions and choices in several ways. One way is to enter the interactive python shell provided by django with `python manage.py shell` and fill in the tables with data as described in the documentation. <br>
For doing the process of population the tables with data fast just execute `python fill_db_with_data.py`. The script fills the tables polls_choice and polls_question with a set of predefned questions and choice opportunities for each question. <br>
Questions and Choices can also be set in the admin mode of the website (see below).

## running the server

python manage.py runserver 4000 <br>

- For viewing and interacting as a user <br>
  http://localhost:4000/polls
- For administrative actions like setting new questions and choices <br>
  http://localhost:4000/admin

## Technical configurations

- ubuntu 22.04
- mysql 14.14
- python 3.11
- conda 24.5.0
- django 5.1
- django-debug-toolbar 4.4.6
- mysqlclient 2.2.4
