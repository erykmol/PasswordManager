from django import forms
from .models import Site_data

class SiteForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	site_url = forms.URLField()
	class Meta:
		model = Site_data
		fields = [
			'site_name',
			'site_url',
			'site_login', 
			'password'
		]

		widgets = {
			'password': forms.PasswordInput(),
		}