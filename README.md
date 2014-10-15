Code4SA Flask Template
======================

This is a basic [Flask](http://flask.pocoo.org/) Python application that can be used as a template for new projects.

Features:

* Sass CSS compilation, see [assets/stylesheets/app.sass](assets/stylesheets/app.sass)
* CSS and Javascript minification, put assets into `assets/stylesheets/` and `assets/javascripts/` and they will be pulled in automatically.
* Google Analytics: just fill in your tracking code in [application/templates/base.html](application/templates/base.html)
* Procfile ready for deployment to Heroku

Third-party packages:

* Twitter Bootstrap 3.1.1
* Font Awesome 4.1.0

Development
===========

* clone the repo
* virtualenv --no-site-packages env
* source env/bin/activate
* pip install -r requirements.txt
* python server.py
