
from django.urls import path
from .import views


urlpatterns = [
   path('', views.home, name="homepage"),
   path('form/', views.form, name="formpage"),
   path('criminal/', views.criminal, name="criminalpage"),
   path('signup/', views.signup, name="signuppage"),
   path('login/', views.login, name="loginpage"),
   path('logout/', views.logout, name="logoutpage"),
   
] 