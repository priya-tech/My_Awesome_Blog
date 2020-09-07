from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfileView, EditProfileView, CreateProfilePageView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='user_edit'),
    path('password/', PasswordsChangeView.as_view(), name='password_change'),
    path('<int:pk>/profile/', ShowProfileView.as_view(), name='show_profile'),
    path('<int:pk>/edit_profile_page/', EditProfileView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),
]
