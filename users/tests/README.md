# Testing

Tests in this app are split into four modules:
    - Forms
    - Models
    - Views
    - Functional

NOTE - If running tests in a virtualenv, make sure you have Chromedriver/Geckodriver installed and in the root directory.

## Forms
`test_forms.py` tests if both forms in the app can correctly validate data.


## Models
`test_models.py` tests manager methods - creating new users and filtering.


## Views
`test_views.py` tests if all views authorise as expected. This module also tests if views serve the correct templates with the appropriate response codes.


## Functional
`test_functional.py` tests each of the CRUD functions and therefore the logical user paths including logging in and out. This module runs tests on Chrome.

# Running the tests
On top of regular test specification, you can use `tags` to choose tests to run.

## All tests
`docker-compose run web python manage.py test`

## Unit tests
`docker-compose run web python manage.py test --exclude-tag=functional`

## Functional tests
`docker-compose run web python manage.py test --exclude-tag=unit`
