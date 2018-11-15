from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Site_data(models.Model):
    log_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    site_name = models.CharField(max_length=200)
    site_url = models.CharField(max_length=200)
    site_login = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)


    # def get_absolue_url(self):
    # 	return reverse("Manager:update", id_=self.id)
    
