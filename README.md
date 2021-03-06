# TaskTracker
A Simple To Do List Application

# A To Do List Application built using Django with MySQL as the backend database

### Requirements as per tested upon
1. Python 3.6+
2. Django 2.0.2 (Tested)
3. Xampp (for MySQL running on port 3306)
4. MySQL 5.0 or above

Note: In case of a different port being used for MySQL, change the settings accordingly in the settings.py file in the main folder

### Steps for Running the project
1. Start Apache and MySQL from the Xampp Control Panel
2. Import the database file `tasktracker.sql` under the schema name tasktracker
3. Run the code using `command prompt` or pycharm ide preferably

### To run the project from command prompt
1. Locate and open the project folder in cmd
2. Type in `python manage.py runserver` to start the server for project.

### To run the project from Pycharm
1. setup configuration as Django Server and click on apply.
2. click on the run icon and the project is up and ready to be used.

### There are two users that have been already setup for use
- `username: admin      password: admin123456`
- `username: demouser   password: demouser123`

Django admin panel can be accessed using the admin credentials and link `127.0.0.1:8000/admin`

Note: This is the default localhost which is used by the server for django
