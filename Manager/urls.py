from django.urls import path
from . import views


app_name='Manager'

urlpatterns = [

    path('', views.home, name='home'),
    path('create/', views.siteCreate, name='create'),
    path('update/<int:id_>', views.siteUpdate, name='update'),
    path('delete/<int:id_>', views.siteDelete, name='delete')

 ]