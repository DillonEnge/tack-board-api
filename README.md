# TACK-BOARD-API
## Setup:
* Create a virtual environment with python 3.6.0
```shell
virtualenv venv -p python3.6
``` 
* Activate your environment
```shell
. venv/bin/activate
``` 
* Install all dependencies from requirements.txt
```shell
pip install -r requirements.txt
``` 
* Create a .env file in the root directory then populate it with SECRET_KEY, USER, and PASSWORD
```shell
touch .env
```
* Run migrations (Make sure your PostgreSQL daemon is running on your machine)
```shell
python manage.py makemigrations example
python manage.py migrate
```
* Spin up server
```shell
python manage.py runserver
```
* Confirm it's working by visiting [localhost:8000/example](localhost:8000/example)
