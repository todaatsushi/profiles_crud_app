import django.views.generic as generics
import django.contrib.auth.mixins as mixins

from users.models import BaseUser


class AllBaseUsersView(generics.ListView):
    model = BaseUser
    template_name = 'users/all_users.html'
    context_object_name = 'users'
    ordering = ['-created_at']
    paginate_by = 8
        

class BaseUserDetailView(generics.DetailView):
    model = BaseUser
    template_name = 'users/user_detail.html'
    context_object_name = 'target_user'


class BaseUserCreateView(generics.CreateView):
    model = BaseUser
    template_name = 'users/create_user.html'
    fields = [
        'email', 'password'
    ]
