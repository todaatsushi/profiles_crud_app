import django.views.generic as generics

from users.models import BaseUser


class AllUsersView(generics.ListView):
    model = BaseUser
    template_name = 'users/all_users.html'
    context_object_name = 'users'
    ordering = ['-created_at']
    paginate_by = 8
        

class UserDetailView(generics.DetailView):
    model = BaseUser
    template_name = 'users/user_detail.html'
    context_object_name = 'target_user'
