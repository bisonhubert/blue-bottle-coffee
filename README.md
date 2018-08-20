# Blue Bottle Coffee 
Item management system for a global coffee supplier.

## Prerequisites
* postgresql
* python3
* virtualenv

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
```
# Clone the repo 
$ git clone https://github.com/bisonhubert/blue-bottle-coffee.git
$ cd blue-bottle-coffee

# Create and activate a virtual environment
$ mkdir venv && cd venv && python3 -m venv blue-bottle-coffee
$ source venv/blue-bottle-coffee/bin/activate
$ echo $VIRTUAL_ENV
# the virtual environment is ready if 'echo' returns the correct file path
# ie: /Users/_bison__/venv/blue-bottle-coffee

# Install dependencies
$ pip3 install -r requirements.txt

# Initialize and seed database
$ make db-init

# Start server
$ python3 manage.py runserver
```
You should now be able to visit the admin dashboard at [localhost:8000/admin](localhost:8000/admin).


## Access the  Admin Dashboard
We're using a Postgresql database with this project to make deployment to Heroku possible. To gain access to the admin dashboard, we'll need to start a local Postgresql db instance and create a superuser.
```
# Boot psql
$ psql

# In a new tab, run this command and follow the steps for email and password
$ python3 manage.py createsuperuser --username bison

# You should now be able to log into the admin dashboard
```

## Running the tests
Run the test suite with `py.test`. The tests cover:
* database models
* third-party API client
* seed importer and factories

## Deployment
As instructed, this project has not been deployed to a cloud service. The following steps outline what is required in order to deploy this project to production. We will be using [Heroku](https://devcenter.heroku.com/articles/deploying-python) as our host service.
