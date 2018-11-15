from django.shortcuts import render, get_object_or_404, redirect
from .models import Site_data
from .forms import SiteForm
from django.contrib.auth.models import User
from django.http import Http404
from django.views.generic.edit import CreateView,UpdateView
from django.contrib import messages

# class siteCreate(CreateView):
# 	template_name='Manager/siteform.html'
# 	form_class=SiteForm
# 	queryset=Site_data.objects.all()

# 	def form_valid(self, form):
# 		print(form.cleaned_data)
# 		return super().form_valid(form)

def siteCreate(request):
	if not request.user.is_authenticated:
		raise Http404

	form = SiteForm(request.POST or None)
	if form.is_valid():
		form.log_name=request.user
		form.save()
		return redirect('Manager:home')
	else:
		site={ 
			'site': form
		}
		return render(request, 'Manager/siteform.html',site)

def siteUpdate(request, id_):
	site=get_object_or_404(Site_data,id=id_)
	if request.POST=="POST":
		form=SiteForm(request.POST,instance=site)
		if form.is_valid():
			form.log_name=request.user
			form.save()
			return redirect('Manager:home')
	else:
		form=SiteForm(instance=site)
		site = {

			'site':form
		}
		return render(request,'Manager/siteform.html',site)


def siteDelete(request, id_):
	site=get_object_or_404(Site_data,id=id_)
	try:
		site.delete()
		return redirect('Manager:home')
	except Exception as e:
		messages.warning(request,'Site could not be deleted')
		return redirect('Manager.home')


def home(request):
	
	print(request.user)
	print(User.objects.get(username=request.user))
	user_name=User.objects.get(username=request.user)
	user_sites=Site_data.objects.filter(log_name=user_name)

	sites={ 
		'sites': user_sites
	}
	
	return render(request, 'Manager/home.html',sites)