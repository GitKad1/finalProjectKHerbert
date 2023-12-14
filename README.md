# FinalProjectKHerbert

This project is a topic survey app. It allows users to log in and supply topics that they are interested in.
These topics can be added or deleted. With these the user can search a curated list verified media houses to gain a quick survey of the up-to-date news concerning their topics.
This can help them avoid advertisements and unwanted posts by less respected entities.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)


## Features
The app allows:
- Adding and deleting topics.
- Searching among curated sources for up-to-date information.
- User privacy and protection.
- Admin creation and management


## Installation
To install:
```
pip install -r requirements.txt
```

## Configuration
```
//This creates the schema that sets up the database.
python manage.py makemigrations

//This applies the migrations.
python manage.py migrate

//This creates the administrator profile for the admin side of the website.
python manage.py createsuperuser
```
