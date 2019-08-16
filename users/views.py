from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
import django.views.generic as generics
import django.contrib.auth.mixins as mixins

from users.models import BaseUser
import users.forms as forms
from users.mixins import IsOwnerOrStaffTestMixin


class AllBaseUsersView(generics.ListView):
    model = BaseUser
    template_name = 'users/user_list.html'
    context_object_name = 'users'
    ordering = ['-created_at']
    paginate_by = 8
        

class BaseUserDetailView(generics.DetailView):
    model = BaseUser
    template_name = 'users/user_detail.html'
    context_object_name = 'target_user'


class BaseUserCreateView(SuccessMessageMixin, IsLoggedOutTestMixin,
                         generics.CreateView):
    model = BaseUser
    template_name = 'users/user_create.html'
    form_class = forms.BaseUserForm
    success_message = 'Welcome %(first_name)s to the site!'


class BaseUserUpdateView(SuccessMessageMixin, IsOwnerOrStaffTestMixin,
                         generics.UpdateView):
    model = BaseUser
    template_name = 'users/user_update.html'
    form_class = forms.BaseUserForm
    success_message = 'Your profile was updated successfully.'


class BaseUserDeleteView(SuccessMessageMixin, IsOwnerOrStaffTestMixin,
                         generics.DeleteView):
    model = BaseUser
    template_name = 'users/user_confirm_delete.html'
    success_url = '/'
    success_message = "You've successfully deleted the user."
