"""
Make a .env and set up Oauth.
"""

# Set up all auth.
print("This is a script to set up the CRUD app.\n")
print("This will set up Oauth with GitHub, static files, database migration, superuser and the .env file.")
print("Please make sure you have a GitHub Oauth application and the client id and secret keys.")
print("You can make an Oauth application here: https://github.com/settings/applications/new.\n\n")

# Make .env file
import set_up.make_env
import subprocess, os

# Create dataabases
subprocess.run(["python", "manage.py", "migrate"])


# Create all-auth models
import set_up.set_up_all_auth


# Create static files
print('Building static files.')
subprocess.run(["python", "manage.py", "collectstatic"])

# Create superuser
superuser = ''
while superuser not in ['yes', 'no']:
    superuser = input('Do you want to create a superuser (to use the admin site)? ("yes" or "no"): ')

if superuser =='yes':
    subprocess.run(["python", "manage.py", "createsuperuser",])