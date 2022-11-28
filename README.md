# Introduction

This is a flask boilerplate for new Flask web applications created by Asiimwe Edgar. It is for developers looking to get started quickly on a new web application project using the Flask microframework.

#What's included
- User Authentication (SignUp, Login, Account verification with SMS and Email, Password Recovery)
- 
# <a name='installation-guide'>Installation Guide</a>

This project requires the following tools:

- Python - The programming language used by Flask.
- SQLite - A relational database system for Local Deployment.
- Virtualenv - A tool for creating isolated Python environments.

To get started, install Python on your local computer if you don't have them already. 

## Getting Started

**Step 1. Clone the code into a fresh folder**

```
$ git clone https://github.com/edger-asiimwe/flasky.git
$ cd 
```

**Step 2. Create a Virtual Environment and install Dependencies.**

Create a new Virtual Environment for the project and activate it. If you don't have the `virtualenv` command yet, you can find installation [instructions here](https://virtualenv.readthedocs.io/en/latest/). Learn more about [Virtual Environments](http://flask.pocoo.org/docs/1.0/installation/#virtual-environments).

```
$ virtualenv venv
$ source venv/bin/activate
```

Next, we need to install the project dependencies, which are listed in `requirements.txt`.

```
(venv) $ pip install -r requirements.txt
```

**Step 3: Update environment variables and run the Server.**

Create a new file named `.env` by duplicating `.env.example`. Update the new file with the GitHub credentials. It should look similar to this:

```
# .env file
DATABASE_URL="[INSERT_DATABASE_URL]"
```

Now we're ready to start our server which is as simple as:

```
(venv) $ flask run
```

Open http://localhost:5000 to view it in your browser.

The app will automatically reload if you make changes to the code.
You will see the build errors and warnings in the console.

# What's Included?

- [Flask](http://flask.pocoo.org/) - A microframework for Python web applications
- [Flask Blueprints](http://flask.pocoo.org/docs/1.0/blueprints/) - A Flask extension for making modular applications
- [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) - A Flask extension that adds ORM support for your data models.
- [Werkzeug](http://werkzeug.pocoo.org/) - A Flask framework that implements WSGI for handling requests.
- [Bootstrap 4](https://getbootstrap.com/) - An open source design system for HTML, CSS, and JS.
- [Jinja2](http://jinja.pocoo.org/docs/2.10/) - A templating language for Python, used by Flask.
- [Flask Login](http://flask-login.pocoo.org/docs/2.10/) - A user management framework.

