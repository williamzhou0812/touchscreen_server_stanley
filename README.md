# README #

Django Rest Server for NAC Touchscreen Project

Utilising MySQL Database system

### How do I get set up?

* Install [MySQL](https://dev.mysql.com/downloads/mysql/) and [MySQL Workbench](https://dev.mysql.com/downloads/workbench/) 

* Install [Python 2.x](https://www.python.org/downloads/)

* Configure pip (tool for installing Python packages)
    * Securely Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py)
    * Run ```python get-pip.py``` (If error try ```sudo python get-pip.py``` instead)

* Install Django: ```pip install Django``` (Similarly, if error try ```sudo pip install Django```)

* Install Django REST Framework: ```pip install djangorestframework```

* Install Pillow ```pip install Pillow```

###How to run REST Server
* Navigate to project directory via Terminal
* Execute ```python manage.py runserver``` for local testing
* Alternatively, execute ```python manage.py runserver x.x.x.x:port```
to allow multiple device access via LAN/WLAN
    * x.x.x.x is the current device's IP Address. [Here's](http://www.wikihow.com/Find-Your-IP-Address-on-a-Mac) how to
     check your IP address on a Mac.
    * You might have to disable your firewall to allow different devices to request data from the REST Server
    * Before running the server, please add your IP address as ```'x.x.x.x'``` inside ```settings.py``` under ```ALLOWED_HOSTS``` so it will look something similar to this:
    ```ALLOWED_HOSTS = ['127.0.0.1']```

###Testing Rest Server
* Install [Postman](https://www.getpostman.com/apps)

###Sample admin account (can be changed later)
* username = root
* password = root1234