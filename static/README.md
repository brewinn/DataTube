## DataTube Static

The webserver (Nginx) will look for static files (Javascript, CSS, etc.) here.
Do not place files here directly, but in `datatube/datatubeapp/static`. Django
will collect these static files with `python manage.py collectstatic`. 

_Note_: To avoid unintentionally deleting this file from the remote, run `git
update-index --assume-unchanged static/README.md`.

### Attribution

The original favicon for this project (the bug emoji) was generated using the
following graphics from Twitter Twemoji:

- Graphics Title: 1f41b.svg
- Graphics Author: Copyright 2020 Twitter, Inc and other contributors (https://github.com/twitter/twemoji)
- Graphics Source: https://github.com/twitter/twemoji/blob/master/assets/svg/1f41b.svg
- Graphics License: CC-BY 4.0 (https://creativecommons.org/licenses/by/4.0/)
