# DataTube

[![Tests](https://github.com/brewinn/DataTube/actions/workflows/tests.yml/badge.svg)](https://github.com/brewinn/DataTube/actions/workflows/tests.yml)

A YouTube video search application

## Description

A web-app for searching or getting recommendations for YouTube videos. This
project is made as part of CS-5443 Database Management Systems.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)
- [License](#license)
- [Features](#features)
- [To-do](#to-do)
- [Future Work](#future-work)
- [Project Status](#project-status)

## Installation

First, pull down the repository with
```
git clone --depth 1 https://github.com/brewinn/DataTube.git
```
and `cd` into the pulled repository. The web-app and database may then be
started with 
```
docker-compose up --build
```
The web-app and database will start in separate containers -- initialization is
finished when the following line appears in the log:
```
datatube-django-1  | Watching for file changes with StatReloader
```

When the initialization finishes, the website may be accessed via a web browser
at `localhost:8000`.

### Setting up the database

The database should setup automatically. If it fails, check that the
`kaggle_data` folder is present and populated (see `database/README.md`) and
then run
```
docker exec datatube-django-1 python ../database/kaggle_import_postgres.py
```
to populate the database manually.


### Removal

To remove, run 
```
docker-compose down -v
```
and remove the containers with
```
docker-compose rm -fsv
```

## Usage

After initializing the containers, the website will be available at `localhost:8000`.

The tests can be run with 
```
docker exec datatube-django-1 python manage.py test                       # To run all tests
docker exec datatube-django-1 python manage.py test datatubeapp           # To run just the unit tests
docker exec datatube-django-1 python manage.py test functional_tests      # To run just the functional tests
```

## Credits

The original project developers include Brendan Winn, Joshua Romero, Mengke
Tian, and Nandini Kaveti. This project was made as a part of CS-5443 Database
Management Systems course of UTSA, taught by Dr. Ritu Arora. 

If we use other datasets or outside help, be sure to include a reference here.

## License

MIT: <https://mit-license.org>

## Features

Below is a list of currently implemented features:

- Web server capable of basic video searching
- URL redirection based on search query and modifiers
- Views for search, individual channels, and individual videos
- Search of multiple text fields, including full text search
- Unit testing for individual project components, and several integration tests
- URL encoding and input sanitization

## To-do

- [X] Fill out the README
- [X] Finish initial project design
- [X] Develop the back-end
- [X] Develop the web-app
- [X] Develop the front-end
- [X] Containerize the project
- [X] Deploy to live server

## Future Work

The basics, along with some useful search features and views, have been
implemented. There are numerous improvements or additions that could be made:
- Add more search options -- e.g. a regex based search
- Prettier views -- some basic styling has been added, but there's much to improve
- More videos -- more videos would make the tool more useful, but can cause throughput issues if not properly implemented
- User convenience features -- e.g. hover preview, like you see on Wikipedia
And many more potential features.

## Project Status

Project is considered finished. Addition pushes may occur to fix bugs or correct mistakes.
