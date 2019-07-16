# Django-Rest-Test
A simple REST API in Django and Python3 for employees. Supports GET, POST, PUT, DEL and more. This app is purely to understand how data can be parsed, fetched from any live website and operations can be performed.

### Basic Installation

1. Clone the git repository.
```bash
$ git clone 
```

2. Go to the directory and install the necessary libraries.
```bash
$ cd rest_api/foxtons
$ pip3 install -r requirements.txt
```

3. Track and get the dependencies.
```bash
$ sudo python manage.py migrate
```

4. Create an admin user
```bash
$ sudo python manage.py create superuser
Username (leave blank to use 'root'): admin
Email address: admin@home.local
Password:
Password (again):
Superuser created successfully.
```

5. At this point, you should have enough configured to run the app using Python's development server. Run the following command and browse to http://127.0.0.1:8000/employees
```bash
sudo python3 manage.py runserver 
```

### Some notes on usage:

We have wrapped the API https://reqres.in/ throughout this app.

* The app allows a user(admin) to login with Django Auth Token.
```bash
http://127.0.0.1:8000/admin
```

* Fetch a single user.
```bash
http://127.0.0.1:8000/employees/1
```

* Delete a single user.
```bash
http://127.0.0.1:8000/employees/1
Click on the Delete button.
```

* It can list all the users. 
```bash
http://127.0.0.1:8000/employees 
```

* It allows us to create new users.
```bash
Paste sample data and click Post button.
{
            
            "last_name": "Roy",
            "email": "roy.sita@reqres.in",
            "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/olegpogodaev/1283.jpg",
            "first_name": "Sita"
        }

This will create the new user with details.
```

* We can even update the data.
```bash
http://127.0.0.1:8000/employees/1

Paste sample data and click Put button.
{
            "id": 3,
            "last_name": "Wong C",
            "email": "emma.wong@reqres.in",
            "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/olegpogodaev/128.jpg",
            "first_name": "Emma"
        }

This will update the user with details.
```

* List all jobs (use the List Resource – this will return a list of colours)
```bash
http://127.0.0.1:8000/unknown
```

### If you had more time?
I'm not completely happy with the layer between the API and when the application ingests the data. If I had more time I 
would of built additional classes to interact better with the API response making it more robust if the API responded 
with a failure, adding exponential back-off etc, (you'll notice I did not add much in handling for what happens if the API 
responds with a non 200 code). For now, I am not saving the data retrived in the database. I have created a dummy model but haven't connected it to achieve all the tasks and save in database. For now it is just doing all the operations on live json and getting refreshed.
The code can be made faster to work on large set of data. 

### How can we improve this test?
Sometimes a real test of a programmer is compromise and looking at how they manage them while trying to conform to requirements. Either that, or I've completely missed a load of them, and I've gotten this wrong.. (hopefully not!)
