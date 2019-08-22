"""
Sets up all-auths Site and Social Application model instances to set up the project.

Using user inputs for the GitHub Oauth client id and secret, this automates creating them for
the app.
"""
print('Setting up Oauth.\n')

import os, sys
import json

print(os.environ.get("SECRET_KEY"))
sys.path.append('/profiles/settings.py')
os.environ['DJANGO_SETTINGS_MODULE'] = 'profiles.settings'

import django
django.setup()

from django.core.management import call_command

# from allauth.socialaccount.models import SocialApp


auth_models = [
    {
        "model": "sites.site",
        "pk": 1,
        "fields": {
            "domain": "localhost",
            "name": "example.com"
        }
    },
    {
        "model": "socialaccount.socialapp",
        "pk": 1,
        "fields": {
            "provider": "github",
            "name": "github",
            "client_id": os.environ.get('GITHUB_CLIENT_ID').replace("\"", ''),
            "secret": os.environ.get('GITHUB_CLIENT_SECRET').replace("\"", ''),
            "key": "",
            "sites": [
                [
                    "localhost"
                ]
            ]
        }
    }
]
print('Created JSON with data.\n', auth_models)

# app = SocialApp.objects.create(
#     pk=auth_models['app']['pk']
#     provider=auth_models['app']['fields']['provider'],
#     name=auth_models['app']['fields']['name'],
#     client_id=auth_models['app']['fields']['client_id'],
#     secret=auth_models['app']['fields']['secret'],
#     key=auth_models['app']['fields']['key'],
# )
# site = app.sites.create(
#     domain='localhost',
#     name='local'
# )

# if app and site:
#     print('Success!')
# else:
#     if not app:
#         print('The app object was not created properly.')
#     if not site:
#         print('The site object was not created properly')

# Write to json
with open('users/fixtures/allauth_fixture.json', 'w') as outfile:
    json.dump(auth_models, outfile)

# Load to db
call_command('loaddata', 'allauth_fixture.json', verbosity=0)

from allauth.socialaccount.models import SocialApp
print('Loaded JSON!\n', SocialApp.objects.first().name)

if not SocialApp.objects.first().name is not 'github':
    raise ImportError('SocialApp was not created properly - please implement manually using Django admin.')