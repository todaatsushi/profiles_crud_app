"""
Generate an .env file and set env variables.
"""

import os, uuid


def write_to_env(env_field, message='', input_required=True, default_value=''):
    """
    Writes to the .env file with the format:
    'env_field="env_value"'

    Inputs:
        - env_field - capitalised string
        - message - string:  the message to display to the user.
        - input_required - bool: if user is needed for env_field, prompts input.
        - default_value - any: if not input_required, the value to add.
    """

    with open('.env', 'a') as env:
        env_value = input(message) if input_required else default_value
        env.write('{}={}\n'.format(env_field, env_value))
        os.environ[env_field] = env_value
        f.close()


print('Generating your .env file!\n')

# GitHub Oauth settings
write_to_env('GITHUB_CLIENT_ID', 'GitHub Oauth app client ID: ')
write_to_env('GITHUB_CLIENT_SECRET', 'GitHub Oauth app client secret: ')


# Oauth test details
need_github_login = ''
while need_github_login not in ['yes', 'no']:
    need_github_login = input(
        'Do you want to run the Oauth functional test? ("yes" or "no"): '
    ).replace("\"", '')

if need_github_login == 'yes':
    write_to_env('GITHUB_USERNAME', 'GitHub username: ')
    write_to_env('GITHUB_PASSWORD', 'GitHub password: ')


# Settings module
write_to_env('DJANGO_SETTINGS_MODULE', input_required=False,
             default_value='profiles.settings')

# Secret key
write_to_env('SECRET_KEY', input_required=False, default_value=uuid.uuid4().hex)

print('.env file done and set!\n')
