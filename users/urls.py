from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, VerifyTemplateView, verify_email_page, \
    EmailVerifyUnsuccessful, UserListView, is_active_setting_for_stuff

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(),  name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('', VerifyTemplateView.as_view(), name='email_verify_sended'),
    path('email_verify_done/<token>', verify_email_page, name='email_verify_done'),
    path('email_verify_unsuccessful/', EmailVerifyUnsuccessful.as_view(), name='email_verify_unsuccessful'),
    path('list_user/', UserListView.as_view(), name='list_user'),
    path('is_active_setting_for_stuff/<int:pk>/', is_active_setting_for_stuff, name='is_active_setting_for_stuff'),


]
