# REST API Framework in Django


## Set up the project

Upgrade pip to the latest version:

`python -m pip install --upgrade pip`

Then we install virtualenv:

`pip install --user virtualenv`

With the next command we create a new python environment, using python version 3, so we can install the required modules without creating issues to other python applications:

`virtualenv env --python=python3`

if everything is ok you will see a new folder `env` inside the project folder.

In order to work in our new environment we need to activate it:

`source env/bin/activate`

We should see an `(env)` at the start of the command line

Now we are ready to install the required modules:

`pip install -r requirements.txt`

Before starting the application we initialize the database:

`python manage.py migrate`

We create a superuser for managing users and groups:

`python manage.py createsuperuser`

Before starting the application some configuration is required, create a new file named `local.settings.py` into the `mainapp` folder, just near the `settings.py` and add all the required variables.

Now we are ready to run the application:

    $ ./django-auto.sh

## Production

Before running the application in production, we should create a new `SECRET_KEY`, for security reason,
we can use the function `django.core.management.utils.get_random_secret_key()`.

The variable `DEBUG` should be set to `False`.

Also we need to collect the static files since django will refuse to serve static files with `DEBUG=False`; we will use the command `collectstatic` provided by django:

    $ python manage.py collectstatic --clear

A new folder `static` will be created under the project folder.

In the web server configuration we need to add the static location in order to serve those files:

    location /static/ {
        root <path>/app;
    }