from django.test import LiveServerTestCase, tag
from django.test.utils import override_settings
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import socket
import os
import allauth.socialaccount.models as all_auth_models


def wait_for_page_load():
    """
    Calls time.sleep(2) if not using Docker to allow tests to run as
    expected.
    """
    import time
    if not settings.DOCKER:
        time.sleep(2)


class FunctionalTestBaseTestCase(LiveServerTestCase):
    """
    Declares the webdriver variable for Docker and non
    Docker tests.
    """
    # Allow external access
    host = '0.0.0.0'
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # Make webdriver
        if settings.DOCKER:
             # Set host to externally accessible web server address
            cls.host = socket.gethostbyname(socket.gethostname())
            cls.browser = webdriver.Remote(
                command_executor='http://selenium:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.CHROME,
            )
        else:
            # cls.browser = webdriver.Chrome(executable_path='./chromedriver')
            cls.browser = webdriver.Firefox(executable_path='./geckodriver')

        cls.browser.implicitly_wait(3)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()


@override_settings(DEBUG=True)
class ProfilesCRUDFunctionalTestsTestCase(FunctionalTestBaseTestCase):

    fixtures = [
        'users_functional',
    ]

    @tag('functional')
    def test_user_visits_site_to_view_profiles(self):
        """
        User goes to the '/' page and sees the home title and the registered
        users listed. User visists a users profile.
        """

        self.browser.get(self.live_server_url)

        # Find a user's name in page
        assert 'Janet' in self.browser.page_source

        # See options
        assert 'Sign Up' in self.browser.page_source

        # Wants to see more about Janet so clicks on her profile
        janet_profile = self.browser.find_element_by_link_text('Janet')
        janet_profile.click()
        
        wait_for_page_load()

        # Sees profile
        assert 'None' in self.browser.page_source
        
        # Cannot update her profile
        assert 'Update your profile' not in self.browser.page_source
    
    @tag('functional')
    def test_user_visits_site_to_sign_up(self):
        """
        User goes to the '/' page and sees the home title and the two registered
        users listed. User then signs up for an account.
        """

        # Create page
        self.browser.get(self.live_server_url + reverse('user-create'))

        # Find a user's name in page
        assert 'Create your profile.' in self.browser.page_source

        # Get fields
        username = self.browser.find_element_by_id('id_username')
        email = self.browser.find_element_by_id('id_email')
        first_name = self.browser.find_element_by_id('id_first_name')
        last_name = self.browser.find_element_by_id('id_last_name')
        about = self.browser.find_element_by_id('id_about')
        company = self.browser.find_element_by_id('id_company')
        role = self.browser.find_element_by_id('id_role')
        responsibilities = self.browser.find_element_by_id('id_responsibilities')
        password1 = self.browser.find_element_by_id('id_password1')
        password2 = self.browser.find_element_by_id('id_password2')
        submit = self.browser.find_element_by_id('id_submit')

        # Fill form data
        username.send_keys('testuser')
        email.send_keys('test@email.com')
        first_name.send_keys('Johnny')
        last_name.send_keys('Doe')
        about.send_keys('Lorem ipsum')
        company.send_keys('foo')
        role.send_keys('bar')
        responsibilities.send_keys('lorem ipsum')
        password1.send_keys('testing321')
        password2.send_keys('testing321')

        # Submit form
        submit.send_keys(Keys.RETURN)
        
        wait_for_page_load()

        # See login page
        assert 'Login' in self.browser.page_source

        # Message displayed confirms registration
        assert 'Welcome Johnny' in self.browser.page_source

        # Login to new account
        login_username = self.browser.find_element_by_id('id_username')
        login_password = self.browser.find_element_by_name('password')
        login_submit = self.browser.find_element_by_id('id_submit')

        login_username.send_keys('testuser')
        login_password.send_keys('testing321')
        login_submit.send_keys(Keys.RETURN)
        
        wait_for_page_load()


        # Nav options should change now that user is logged in
        assert 'Logout' in self.browser.page_source
        
        # User should be in all users
        assert 'Johnny' in self.browser.page_source

        # User logs out
        logout = self.browser.find_element_by_link_text('Logout')
        logout.click()
        
        wait_for_page_load()

        # Back home
        assert 'Login' in self.browser.page_source
        assert 'Home' in self.browser.page_source

    @tag('functional')
    def test_user_can_update_own_data(self):
        """
        User goes to the '/' page and attempts to login. Having logged in,
        user attempts to update their own information having recently got a
        promotion. User updates info and sees new info in their profile.
        """
        self.browser.get(self.live_server_url)
        login = self.browser.find_element_by_link_text('Login')
        login.click()
        
        wait_for_page_load()

        # Login to account
        login_username = self.browser.find_element_by_id('id_username')
        login_password = self.browser.find_element_by_name('password')
        login_submit = self.browser.find_element_by_id('id_submit')

        login_username.send_keys('john')
        login_password.send_keys('foo')
        login_submit.send_keys(Keys.RETURN)
        
        wait_for_page_load()

        # Click into own profile
        profile = self.browser.find_element_by_link_text('John')
        profile.click()
        
        wait_for_page_load()

        # Own profile
        assert 'Update your profile' in self.browser.page_source
        update_link = self.browser.find_element_by_link_text('Update your profile')
        update_link.click()

        # Update page
        assert 'Change your details below.' in self.browser.page_source

        # Change company
        self.browser.find_element_by_id('id_company').clear()

        company = self.browser.find_element_by_id('id_company')
        submit = self.browser.find_element_by_id('id_submit')

        company.send_keys('Foo LTD')
        submit.send_keys(Keys.RETURN)
        
        wait_for_page_load()

        assert 'Your profile was updated successfully.' in self.browser.page_source

    @tag('functional')
    def test_user_can_delete_profile(self):
        """
        User John logs into his account and attempts to delete the account and his profile.
        """
        self.browser.get(self.live_server_url)

        # Find a user's name in page
        assert 'John' in self.browser.page_source

        self.browser.get(self.live_server_url + reverse('user-login'))

        # Login to account
        login_username = self.browser.find_element_by_id('id_username')
        login_password = self.browser.find_element_by_name('password')
        login_submit = self.browser.find_element_by_id('id_submit')

        login_username.send_keys('john')
        login_password.send_keys('foo')
        login_submit.send_keys(Keys.RETURN)
        
        wait_for_page_load()

        # Click into own profile
        profile = self.browser.find_element_by_link_text('John')
        profile.click()
        
        wait_for_page_load()

        # Own profile
        assert 'Delete your profile' in self.browser.page_source
        delete_link = self.browser.find_element_by_link_text('Delete your profile')
        delete_link.click()
        
        wait_for_page_load()

        # Confirm delete page
        assert 'Delete User - John Doe' in self.browser.page_source
        submit = self.browser.find_element_by_id('id_submit')
        submit.click()
        
        wait_for_page_load()

        # User not on home page anymore
        assert 'John' not in self.browser.page_source

    @tag('functional')
    def test_user_can_change_their_password(self):
        # Login as a user
        self.browser.get(self.live_server_url + reverse('user-login'))

        # Login to new account
        login_username = self.browser.find_element_by_id('id_username')
        login_password = self.browser.find_element_by_name('password')
        login_submit = self.browser.find_element_by_id('id_submit')

        login_username.send_keys('john')
        login_password.send_keys('foo')
        login_submit.send_keys(Keys.RETURN)
        
        wait_for_page_load()

        self.browser.get(self.live_server_url + reverse('user-update', kwargs={'slug': 'john'}))

        # Click change password link
        self.browser.find_element_by_link_text('Change password').click()
        
        wait_for_page_load()

        assert "Are you sure that you'd like to change your password?" in self.browser.page_source

        old_password = self.browser.find_element_by_name('old_password')
        new_password1 = self.browser.find_element_by_name('new_password1')
        new_password2 = self.browser.find_element_by_name('new_password2')

        # Enter details
        old_password.send_keys('foo')
        new_password1.send_keys('testing321')
        new_password2.send_keys('testing321')

        self.browser.find_element_by_id('id_submit').click()
        
        wait_for_page_load()

        assert 'Success!' in self.browser.page_source

