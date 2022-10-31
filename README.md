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

Once pulled, you'll want to use a python virtual environment; the rest of this
guide will use `venv`. Initialize a virtual environment with 
```
cd virtualenv
python3 -m venv datatube
```
If the environment is not already active, it may be activated with `source
datatube/bin/activate`. The required python packages may then be installed with 
```
pip -r ../datatube/requirements.txt
```

### Setting up the database

The current version utilizes sqlite3, and assumes an empty `db.sqlite3`
database in the `datatube` directory. From the `datatube` directory, run 
```
python manage.py makemigrations
python manage.py migrate
```
To populate this database, `cd` into the `database` folder and run `python
kaggle_import.py`.

### Functional tests setup

The functional tests rely on the Selenium testing framework, and assume that
you have [Firefox](https://www.mozilla.org/en-US/firefox/new/) and
[geckodriver](https://github.com/mozilla/geckodriver) installed. Installation
may vary for each system, consult the [Selenium documentation](https://www.selenium.dev/documentation/) 
for more information.

### Removal

To remove, simply delete the repository. If you created the virtual environment
separately, or installed the packages with a base python install, you'll have
to remove those separately.

## Usage

To run the server locally, run `python manage.py runserver` from the `datatube`
directory. This will start a server and provide an address to view it --
usually `localhost:8000`.

The tests can be run with `python manage.py test`. The unit tests will run
without additional setup. To run just the unit tests, use `python manage.py
test datatubeapp`, and use `python manage.py test functional_tests` to run just
the functional tests.

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
- [ ] Develop the web-app
  - [X] Initial design
  - [X] Basic functionality
  - [ ] Advanced search capabilities
  - [ ] More search catagories
  - [ ] Individual video and channel views
- [ ] Develop the front-end
- [ ] Containerize the project
- [ ] Deploy to live server

## Future Work

This section is more for when the project is considered complete. What could be
done to build upon or improve the project?

## Project Status

The project is currently being designed and developed.
