### APICBASE Recipes

## Not covered in this repo
- The app can be extended to have a register user functionality.
- When it's starting to become complex we can create a SPA or move views/templates/forms out of Admin.
- More controlled permissions can be added.
- The app can be extended to use multiple tenant setup (each having their own ingredients and recipes database).

## Local Setup
- Create virtualenv.
- Install requirements - `pip install -r requirements-dev.txt`.
- Run `python manage.py runserver 0:8080`. Open your browser at http://localhost:8080.
- Create superuser - `python manage.py createsuperuser`.
- Login using superuser credentials at http://localhost:8080.
- Create more staff users as required.

## Tests
- Run `pytest`. It will run all the tests.

## Deploy on heroku
-