from django.contrib.messages.views import SuccessMessageMixin
import django.views.generic as generics
import django.contrib.auth.mixins as mixins

from users.models import BaseUser
import users.forms as forms


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


class BaseUserCreateView(SuccessMessageMixin, generics.CreateView):
    model = BaseUser
    template_name = 'users/user_create.html'
    form_class = forms.BaseUserForm
    success_message = 'Welcome %(first_name)s to the site!'


class BaseUserUpdateView(SuccessMessageMixin, generics.UpdateView):
    model = BaseUser
    template_name = 'users/user_update.html'
    form_class = forms.BaseUserForm
    success_message = 'Your profile was updated successfully.'

