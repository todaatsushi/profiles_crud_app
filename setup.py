"""
Make a .env and set up Oauth.
"""

# Set up all auth.
print("This is a script to set up the CRUD app's Oauth login through GitHub.\n")
print("Please make sure you have a GitHub Oauth application and the client id and secret keys.")
print("You can make an Oauth application here: https://github.com/settings/applications/new.\n\n")

# Make .env file
import set_up.make_env
import subprocess


# Create dataabases
subprocess.run(["python", "manage.py", "migrate"])


# Create all-auth models
import set_up.set_up_all_auth

# Testing
testing = ''
while testing not in ['yes', 'no']:
    testing = input('Do you want to run tests now? ("yes" or "no"): ')

if testing == 'yes':
    subprocess.run(["python", "manage.py", "test", "-v", "2"])


# Create static files
subprocess.run(["python", "manage.py", "collectstatic"])

# Create superuser
superuser = ''
while superuser not in ['yes', 'no']:
    superuser = input('Do you want to create a superuser (to use the admin site)? ("yes" or "no"): ')

if superuser =='yes':
    subprocess.run(["python", "manage.py", "createsuperuser",])