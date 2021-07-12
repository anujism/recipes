### APICBASE Recipes

## Not covered in this repo
- The app can be extended to have a register user functionality.
- When it's starting to become complex we can create a SPA or move views/templates/forms out of Admin.
- More controlled permissions can be added.
- The app can be extended to use multiple tenant setup (each having their own ingredients and recipes database).

## Local Setup
- Create virtualenv.
- Install requirements - `pip install -r requirements-dev.txt`.
- Copy recipes/.env.template to recipes/.env. (Adjust env variables as necessary).
- Run `python manage.py runserver 0:8080`. Open your browser at http://localhost:8080.
- Run `python.manage.py migrate` to migrate all migrations.
- Create superuser - `python manage.py createsuperuser`.
- Login using superuser credentials at http://localhost:8080.
- Create more staff users as required.

## Tests
- Run `pytest`. It will run all the tests.

## Deploy on heroku
- Add git remote for your heroku app.
- Make changes.
- git push heroku master.
- TODO: we can later connect it with github repo and make automatic deployments
