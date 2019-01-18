# intive_project_2

This is a simple Django web app prepared in the second round of Intive Patronage 2019 recruitment process. It displays data from the first round in a dynamic table. This time I had very little time to prepare it, so I didn't go for any extra functionality.

## Installation

The installation process is very much standard. Just clone the repo, go into the project directory and create and activate a virtual environment:

```
$ python3 -m venv env
$ source env/bin/activate
```

Then install dependencies:

```
$ pip install -r requirements.txt
```

As a project requirement the repo includes a prepared SQLite database, but if you started from scratch at this point you'd have to initialize the database with:

```
$ python manage.py makemigrations
$ python manage.py migrate
```

Then to load data from a CSV file you could use a custom management command:

```
$ python manage.py populate_db <file_name>
```

Where `<file_name>` is the name of your input file, in our case `salary.csv`.

### Usage

To run the app just activate your virtual environment and type:

```
$ python manage.py runserver
```

The website should be available at ```http://127.0.0.1:8000/```

There are two pages:

* home page with a link to the list of salaries
* table of salaries