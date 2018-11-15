from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.login_view, name='Users-login'),
    path('signup/', views.signup_view, name='Users-signup'),

]