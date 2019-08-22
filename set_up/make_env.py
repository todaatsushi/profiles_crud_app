"""
Generate an .env file and set env variables.
"""

import os
import uuid

testing = ''
while testing not in ['yes', 'no']:
    testing = input('Do you want to run the Oauth test? ("yes" or "no"): ')

print('\nGenerating your .env file!\n')

# Write .env
f = open('.env', 'w')

# Github Oauth settings
client_id = input("GitHub Oauth app client ID: ")
client_secret = input("GitHub Oauth app client secret: ")
f.write('GITHUB_CLIENT_ID="{}"\n'.format(client_id))
f.write('GITHUB_CLIENT_SECRET="{}"\n'.format(client_secret))

# set variables
os.environ.setdefault('GITHUB_CLIENT_ID', client_id)
os.environ.setdefault('GITHUB_CLIENT_SECRET', client_secret)

if testing == 'yes':
    # Github logins
    github_username = input("GitHub username: ")
    github_password = input("GitHub password: ")
    f.write('GITHUB_USERNAME="{}"\n'.format(client_id))
    f.write('GITHUB_PASSWORD="{}"\n'.format(client_secret))
    os.environ.setdefault('GITHUB_USERNAME', github_username)
    os.environ.setdefault('GITHUB_PASSWORD', github_password)

# Django settings
# Secret Key
key = uuid.uuid4().hex
f.write('SECRET_KEY="{}"\n'.format(key))
os.environ.setdefault('SECRET_KEY', key)

f.write('DJANGO_SETTINGS_MODULE="{}"\n'.format('profiles.settings'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'profiles.settings')

f.close()
print('\n.env file done and set!\n')
