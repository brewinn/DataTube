# DataTube
A YouTube video search application

## Description

A web-app for searching or getting recommendations for YouTube videos. This
project is made as part of CS-5443 Database Management Systems.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
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
docker exec -it datatube-django-1 python ../database/kaggle_import_postgres.py
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
docker exec -it datatube-django-1 python manage.py test                       # To run all tests
docker exec -it datatube-django-1 python manage.py test datatubeapp           # To run just the unit tests
docker exec -it datatube-django-1 python manage.py test functional_tests      # To run just the functional tests
```

## Development

This section describes agreed upon practices/conventions. We may not need it.

Todo

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
- More to come

## To-do

- [X] Fill out the README
- [X] Finish initial project design
- [ ] Develop the back-end
  - [X] Move to PostgreSQL
  - [ ] Develop final database schema
- [ ] Develop the web-app
  - [X] Initial design
  - [X] Basic functionality
  - [ ] Advanced search capabilities
  - [ ] More search catagories
  - [ ] Individual video and channel views
- [ ] Develop the front-end
- [X] Containerize the project
- [ ] Deploy to live server

## Future Work

This section is more for when the project is considered complete. What could be
done to build upon or improve the project?

## Project Status

The project is currently being designed and developed. With everything
containerized, it should be simple to pull down and run.
