
# Profiles CRUD app

This app allows users to create, retrieve, update and delete their information/profiles onto the site with the purpose
of showing off their professional skills. Using Oauth, users can also have a profile using their GitHub accounts.

Built with Django and PostgreSQL as the database. The app also uses Docker for deployment, Selenium & Django's
test functionality for testing.


## Set Up

These instructions will get you a copy of the project up and running on your local machine.

We're going to run the application in a Docker container. First you need to build the Docker image:
```
$ docker-compose build
```

### Oauth with GitHub
Before running the script to set up the app, you will need a client ID and secret key for a GitHub Oauth app. You can set one up on GitHub [here](https://github.com/settings/applications/new). The next command will prompt you for the ID and secret key.

### Building the app
To build the rest of the app, run:
```
$ docker-compose run web python setup.py
```
This will set up your .env file, database, initial models, staticfiles, superuser and tests.

### Run
```
$ docker-compose up
```

And you're up! Visit [http://localhost:8000](http://localhost:8000) to see it in action.

## Testing
The app has a suite of tests that can be run with:
```
$ docker-compose run web python manage.py test
```

Both unit and functional tests are tagged `'unit'` and `'functional'` respectively.
i.e. You can run the unit tests only by adding `--exclude-tag=functional` and vice versa.

## Built With

* [Django](https://docs.djangoproject.com/en/2.2/) - The web framework used


## Authors

* **Me, Atsushi Toda** - [GitHub](https://github.com/todaatsushi) - [My personal website](https://www.atsushi.dev)

## License

This project is licensed under the MIT License.
