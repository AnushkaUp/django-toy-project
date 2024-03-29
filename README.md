# Django Toy Project

A CRUD application for learning Django.

## 1. Setting the virtualenv

**Step 1 : Create the virtual environment**
`$ virtualenv env`

**Step 2 : Activating the virtual environment**
`$ source env/bin/activate`

## 2. Clone the Repository

`$ git clone https://gitlab.com/mountblue/cohort-16-python/anushka_upadhyay/django-toy-project.git`

**cd inside the directory**

`$ cd django-toy-project`

## 3. Install the requirements.txt

`$ pip3 install -r requirements.txt`

## 4. Creating Database

**Install PostgreSQL**

`$ sudo apt install postgresql postgresql-contrib`

**Starting postgres**

`$ sudo -u postgres psql`

**Creating the database**

`postgres=# \i Path of the start.sql file`

`postgres=# \q`

## 5. Running the files

**First move inside the folder**

`$ cd src`

 **Make the migrations**

 `$ python3 manage.py makemigrations`

 `$ python3 manage.py migrate`

 **Creating the superuser**

 `$ python3 manage.py createsuperuser`

 You can provide the username, email and password and login with that later.

 **Run the server**

 `$ python3 manage.py runserver`

 Now you can use the web app and perform the operations on it.

 **Kill the server**

 `$ Ctrl^C`

 **Dropping the user and the database**

 `$ sudo -u postgres psql`

 `postgres=# \i Path of the drop.sql file`

`postgres=# \q`

**Note :** You can perform the admin operation by visiting  http://127.0.0.1:8000/admin/.
