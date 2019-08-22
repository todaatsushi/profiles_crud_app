"""
Sets up all-auths Site and Social Application model instances to set up the project.

Using user inputs for the GitHub Oauth client id and secret, this automates creating them for
the app.

Also generates the secret key and appends to .env
"""
import os, sys, json
import django


sys.path.append('/profiles/settings.py')
django.setup()

from django.core.management import call_command


print('Setting up Oauth.\n')

# Data for social apps
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

# Write to json
with open('users/fixtures/allauth_fixture.json', 'w') as json_file:
    json.dump(auth_models, json_file)
    json_file.close()

# Load to db
call_command('loaddata', 'allauth_fixture.json', verbosity=0)

# Check if loaded
from allauth.socialaccount.models import SocialApp

if not SocialApp.objects.first().name is not 'github':
    raise ImportError('SocialApp was not created properly - please implement manually using Django admin.')