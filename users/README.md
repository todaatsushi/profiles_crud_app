# Users App

The main bulk of this project is based on this users app. 

## Summary

Users can create a profile to display information about themselves to each other. Users
are split into two types: regular users and staff users.

Staff users can update and delete any accounts where regular users can only update and delete
their own accounts.

Users can also change their passwords.

## Layout
### Models
This app has one model - `BaseUser`. This is a custom user model in order to get around Django's
limited in-built model. It is has all the profile data along with regular login/admin/password management
functions.

`BaseUser` has a manager class - `CustomBaseUserManager`. The manager class has a custom `create_user` and `create_superuser` function which generate instances. The manager class also has `get_by_email` and `get_by_name` methods to help query users.

### Forms
Users has two main forms to create and update `BaseUser` instances - `BaseUserCreateForm` and `BaseUserUpdateForm` respectively.

### Views
This app has a view for each of the CRUD functions using Django's generic CBVs. These views are designed with limited authorisation e.g. Users can only update their own profiles unless they are staff.

These permissions are mixins which inherit from `UserPassesTestMixin` and can be found in the mixins.py module.


