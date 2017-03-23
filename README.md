# README #

Django RESTful Server for NAC Touchscreen Project

Utilising MySQL Database System

### How do I get set up?

* Install [MySQL](https://dev.mysql.com/downloads/mysql/) and [MySQL Workbench](https://dev.mysql.com/downloads/workbench/)

* MySQL Workbench is a GUI tool to view and alter the tables and data in the database

* Install [Python 2.x](https://www.python.org/downloads/)

* Configure pip (tool for installing Python packages)
    * Securely Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py)
    * Navigate via Terminal to the location of the downloaded `get-pip.py`
    * Run (via terminal) ```python get-pip.py``` (If error try ```sudo python get-pip.py``` instead)

* Install Django via Terminal: ```pip install Django``` (Similarly, if error try ```sudo pip install Django```)

* Install Django REST Framework via Terminal: ```pip install djangorestframework```

* Install Pillow via Terminal: ```pip install Pillow```

* Install Django-Cors-Header (to enable cross-origin resource sharing) via Terminal: `pip install django-cors-headers`

* Configure MySQL (Database System)
    * Start MySQL Server via Systems Preferences
    * Create a [MySQL Administrator User](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
    * Find out [MySQL Server host and port](http://stackoverflow.com/questions/4093603/how-do-i-find-out-my-mysql-url-host-port-and-username)
    * Create a new connection in MySQL Workbench
    * Create a new schema with MySQL Workbench
    * Open `settings.py` modify variable `DATABASES` with parameters:
        
        'default': {

             'ENGINE': 'django.db.backends.mysql',

             'NAME': '<SchemaName>',

             'USER': '<Administrator account>',

             'PASSWORD': '<Administrator password>',

             'HOST': '<MySQL Server Host>',

             'PORT': '<MySQL Server Port>',
        }

###How to run REST Server
* Navigate to project directory via Terminal
* Execute ```python manage.py runserver``` for local testing
* Alternatively, execute ```python manage.py runserver x.x.x.x:port```
to allow multiple device access via LAN/WLAN
    * x.x.x.x is the current device's IP Address. [Here's](http://www.wikihow.com/Find-Your-IP-Address-on-a-Mac) how to
     check your IP address on a Mac.
    * You might have to modify your firewall settings to allow different devices to request data from the REST Server
    * Before running the server, please add your IP address as ```'x.x.x.x'``` inside ```settings.py``` under ```ALLOWED_HOSTS``` so it will look something similar to this:
    ```ALLOWED_HOSTS = ['127.0.0.1']```

###Testing Rest Server
* Install [Postman](https://www.getpostman.com/apps)

###Sample admin account (can be changed later)
* username = root
* password = root1234