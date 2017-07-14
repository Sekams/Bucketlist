# BucketList Application
[![Build Status](https://travis-ci.org/Sekams/Bucketlist.svg?branch=master)](https://travis-ci.org/Sekams/Bucketlist)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/11fc4593f01d42d9af9fd30b8670ebcc)](https://www.codacy.com/app/Sekams/Bucketlist?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Sekams/Bucketlist&amp;utm_campaign=Badge_Grade)
[![Coverage Status](https://coveralls.io/repos/github/Sekams/Bucketlist/badge.svg?branch=master)](https://coveralls.io/github/Sekams/Bucketlist?branch=master)
[![Code Climate](https://codeclimate.com/github/Sekams/Bucketlist/badges/gpa.svg)](https://codeclimate.com/github/Sekams/Bucketlist)


**The BucketList Application** is a web-based application that whose purpose is to help its users to create, manage, share and delete their bucket lists for the things they would like to do before a given age.


## Technologies
1. Python 2.7
2. click==6.7
3. coverage==4.4.1
4. Flask==0.12.2
5. Flask-Login==0.4.0
6. itsdangerous==0.24
7. Jinja2==2.9.6
8. MarkupSafe==1.0
9. nose==1.3.7
10. pbr==3.1.1
11. six==1.10.0
12. stevedore==1.24.0
13. virtualenv==15.1.0
14. virtualenv-clone==0.2.6
15. virtualenvwrapper==4.7.2
16. Werkzeug==0.12.2


## Getting Started
To be able to use the application locally, one should follow the guidelines highlighted below.

1. Clone/download the application Github repository by running the command below in a git shell 
```
git clone https://github.com/Sekams/Bucketlist.git
```
2. Set up a virtual environment (follow instructions at: http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/)

3. Install the application requirements by running the code below in the virtual environment:
```
pip install -r requirements.txt
```
4. After all the requirements are installed on the local virtual environment, run the application by running the following code in the virtual environment:

5. After successfully running the application, one can explore the features of the BucketList app by navigation to the address: http://127.0.0.1:5000 in any web browser of choice
```
python run.py 
```

## Features 
* Account creation
* User session manegement (Login and Logout)
* Bucketlist creation and management
* Activity creation and tracking
* Bucketlist sharing

## Testing
The application's test coverage can be reviewed by running the code below within the virtual environment:
```
nosetests --with-coverage --cover-package=app
``` 
