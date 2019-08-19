from django.test import LiveServerTestCase, tag
from django.urls import reverse
from django.contrib.auth import get_user_model

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class ProfilesCRUDFunctionalTests(LiveServerTestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            email='jane@mail.com',
            username='jane',
            password='foo',
            first_name='Jane',
            last_name='Doe',
            about='Test person',
            company='None',
            role='None',
            responsibilities='None'
        )

        self.user2 = User.objects.create_user(
            email='john@mail.com',
            password='foo',
            username='john',
            first_name='John',
            last_name='Doe',
            about='Test person',
            company='None',
            role='None',
            responsibilities='None'
        )

        self.staff = User.objects.create_superuser(
            email='staff@mail.com',
            password='foo',
            username='janet',
            first_name='Janet',
            last_name='Doel',
            about='Test person',
            company='None',
            role='None',
            responsibilities='None',

            is_staff=True,
            is_superuser=True
        )

        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.close()
    
    @tag('functional')
    def test_user_visits_site_to_view_profiles(self):
        """
        User goes to the '/' page and sees the home title and the registered
        users listed. User visists a users profile.
        """
        self.browser.get(self.live_server_url)
        time.sleep(3)

        # Find a user's name in page
        assert 'Janet' in self.browser.page_source

        # See options
        assert 'Sign Up' in self.browser.page_source

        # Wants to see more about Janet so clicks on her profile
        janet_profile = self.browser.find_element_by_link_text('Janet')
        janet_profile.click()
        time.sleep(3)

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
        time.sleep(1)

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
        time.sleep(3)

        # Submit form
        submit.send_keys(Keys.RETURN)

        # See login page
        assert 'Login' in self.browser.page_source

        time.sleep(3)
        # Message displayed confirms registration
        assert 'Welcome Johnny' in self.browser.page_source

        # Login to new account
        login_username = self.browser.find_element_by_id('id_username')
        login_password = self.browser.find_element_by_name('password')
        login_submit = self.browser.find_element_by_id('id_submit')

        login_username.send_keys('testuser')
        login_password.send_keys('testing321')
        login_submit.send_keys(Keys.RETURN)

        time.sleep(3)

        # Nav options should change now that user is logged in
        assert 'Logout' in self.browser.page_source
        
        # User should be in all users
        assert 'Johnny' in self.browser.page_source

        # User logs out
        logout = self.browser.find_element_by_link_text('Logout')
        logout.click()
        time.sleep(3)

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
        time.sleep(3)

        # Login to account
        login_username = self.browser.find_element_by_id('id_username')
        login_password = self.browser.find_element_by_name('password')
        login_submit = self.browser.find_element_by_id('id_submit')

        login_username.send_keys('john')
        login_password.send_keys('foo')
        login_submit.send_keys(Keys.RETURN)
        time.sleep(3)

        # Click into own profile
        profile = self.browser.find_element_by_link_text('John')
        profile.click()
        time.sleep(3)

        # Own profile
        assert 'Update your profile' in self.browser.page_source
        update_link = self.browser.find_element_by_link_text('Update your profile')
        update_link.click()
        time.sleep(3)

        # Update page
        assert 'Change your details below.' in self.browser.page_source

        # Change company
        self.browser.find_element_by_id('id_company').clear()

        company = self.browser.find_element_by_id('id_company')
        submit = self.browser.find_element_by_id('id_submit')

        company.send_keys('Foo LTD')
        submit.send_keys(Keys.RETURN)
        time.sleep(3)

        assert 'Your profile was updated successfully.' in self.browser.page_source

    @tag('functional')
    def test_user_can_delete_profile(self):
        """
        User John logs into his account and attempts to delete the account and his profile.
        """
        self.browser.get(self.live_server_url)
        time.sleep(3)

        # Find a user's name in page
        assert 'John' in self.browser.page_source

        self.browser.get(self.live_server_url + reverse('user-login'))
        time.sleep(3)

        # Login to account
        login_username = self.browser.find_element_by_id('id_username')
        login_password = self.browser.find_element_by_name('password')
        login_submit = self.browser.find_element_by_id('id_submit')

        login_username.send_keys('john')
        login_password.send_keys('foo')
        login_submit.send_keys(Keys.RETURN)
        time.sleep(3)

        # Click into own profile
        profile = self.browser.find_element_by_link_text('John')
        profile.click()
        time.sleep(3)

        # Own profile
        assert 'Delete your profile' in self.browser.page_source
        delete_link = self.browser.find_element_by_link_text('Delete your profile')
        delete_link.click()
        time.sleep(3)

        # Confirm delete page
        assert 'Delete User - John Doe' in self.browser.page_source
        submit = self.browser.find_element_by_id('id_submit')
        submit.click()
        time.sleep(3)

        # User not on home page anymore
        assert 'John' not in self.browser.page_source