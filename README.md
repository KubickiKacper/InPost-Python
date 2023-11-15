# Python-task
To complete Junior Python Developer task I decided to use ORM built in Django framework. Use of this framework gave me opportunity to extend possibilities, that's why I decided to create web application. Application contains interface to create new objects to database and read them; create promotion sets including computer & printer and generate CSV files about specified objects.


## How to start
1. Install requirements (venv recommended):
 - python -m venv venv
 - venv\Scripts\activate
 - pip install -r requirements.txt
2. Use django manage.py to start localhost webapp:
 - cd Python-task
 - python manage.py runserver

## Database
Given database schema is implemented in Python-task/products/models.py file where all required informations are specified.  
The changes in database model should be implemented by:
  - python manage.py makemigrations products
  - python manage.py migrate

## Task 1
Check if model of product is PC or laptop is implemented  in type_check() function in utils.py.  
Profitability ratio is function profitability_ratio() in same file.  
The result of equation is in PC and laptop CSV raports or in website describing the device.  

## Task 2
All the promotion sets are in "Promos" tab. At the bottom of the page is option to create new set with objects located in DB.  
There is also option to generate CSV file, which includes information about devices and price of entire set with discount.  
