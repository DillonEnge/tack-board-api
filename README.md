# tack-board-api

## Setup:

    $ pip install -r requirements.txt

    $ cd fast_api

    $ uvicorn app.main:app --reload

## Todo:
* Add individual get fetch by ID for all crud get methods ('./fast_api/app/main.py', L20)
* Add sqlite/psql switch for uuid usage ('./fast_api/app/profiles/models.py', L8)
* Add sqlite/psql switch for uuid usage ('./fast_api/app/groups/models.py', L8)
* Add user operations suite ('./fast_api/app/user/__init__.py', L1)
* Enforce accessibility enum on the db side ('./fast_api/app/events/models.py', L6)
* Add URL switch between sqlite and psql for different environments ('./fast_api/app/db/database.py', L5)
* Add sqlite/psql switch for uuid usage ('./fast_api/app/tags/models.py', L8)
* Enforce enums on the db side ('./fast_api/app/polls/models.py', L5)
