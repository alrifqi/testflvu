Test Project using Python

Clone Repository
```python
- git clone https://github.com/alrifqi/testflvu.git

Go into folder
```python
- cd testflvu

Install requirement
```python
- pip install -r requirements.txt

Migrate Database & Table
```python
- python manage.py db init
- python manage.py db migrate

Add Seed Data for Admin (see seed data at manage.py file)
```python
- python manage.py seed

Run Application
```python
- python run.py

Open on browser: localhost:8080
