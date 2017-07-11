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

* Install Python MySQLclient via Terminal: ```pip install mysqlclient```

* Install Pillow via Terminal: ```pip install Pillow```

* Install PhoneNumbers via Terminal: ```pip install phonenumbers```

* Install Django-Cors-Header (to enable cross-origin resource sharing) via Terminal: `pip install django-cors-headers`

* Install django-nested-admin via Terminal: ```pip install django-nested-admin```

* Clone the project via [SourceTree](https://www.sourcetreeapp.com/)

* Configure MySQL (Database System)
    * Start MySQL Server via Systems Preferences
    * Create a [MySQL Administrator User](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
    * If error in creating user, please see these links: [1](https://www.youtube.com/watch?v=90TGTG_4CQ0) [2](http://stackoverflow.com/questions/30692812/mysql-user-db-does-not-have-password-columns-installing-mysql-on-osx)
    * Find out [MySQL Server host and port](http://stackoverflow.com/questions/4093603/how-do-i-find-out-my-mysql-url-host-port-and-username)
    * Create a new connection in MySQL Workbench
    * Create a new schema with MySQL Workbench
    * Open `settings.py` inside <project directory/touchscreen> and modify variable `DATABASES` with parameters:
        
        'default': {

             'ENGINE': 'django.db.backends.mysql',

             'NAME': '<SchemaName>',

             'USER': '<Administrator account>',

             'PASSWORD': '<Administrator password>',

             'HOST': '<MySQL Server Host>',

             'PORT': '<MySQL Server Port>',
        }

    * Open Terminal, navigate to project directory, and execute: `python manage.py makemigrations` and `python manage.py migrate`
    * To create a new administrator user execute `python manage.py createsuperuser`

###How to run REST Server
* Navigate to project directory via Terminal
* Execute ```sudo python manage.py runserver``` for local testing
* Alternatively, execute ```sudo python manage.py runserver x.x.x.x:port```
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

###Automate MySQL Backup Instructions
* Download [AutoMySQLbackup from Sourceforge](https://sourceforge.net/p/automysqlbackup/)
* Open the install.sh script in your favorite text editor and search for md5sum --check, replace with md5 -r (OS X does not have md5sum installed by default)
* Follow instructions on the AutoMySQLBackup README
* Run `sudo ./install.sh` in the Terminal 
* [Reference](http://soarhevn.blogspot.com.au/2014/10/using-automysqlbackup-on-os-x-1010.html)
* Configure the configuration file (`myserver.conf`)
* To run the backup: `sudo /usr/local/bin/automysqlbackup /etc/automysqlbackup/myserver.conf`
* TO-DO: Figure out how to automate backup 

###Deploying Production Version Instructions (doesn't work for now)
 * Set `Debug = False` in `settings.py`
 * Turn off logging with: `LOGGING_CONFIG = None` in `settings.py`
 * Launch python with: `sudo python manage.py runserver 0.0.0.0:8000 --insecure`
 