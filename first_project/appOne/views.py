from django.shortcuts import render
from django.http import HttpResponse
from appOne.models import Topic, Webpage, AccessRecord, User
from . import forms
# Create your views here.

def index(request):
	my_dict = {'insert_me':"Hello I am"}
	return render(request,'appOne/index.html',context=my_dict)


def help(request):
	my_dict = {'insert_me': "help page"}
	webpages_list = AccessRecord.objects.order_by('date')
	date_dict = {'access_records': webpages_list}
	return render(request,'appOne/help.html',context=date_dict)

def user(request):
	users_list = User.objects.order_by('last_name')
	users_dict = {'users_records': users_list}
	return render(request,'appOne/user.html',context=users_dict)

def form_name_view(request):
	form = forms.FormName()

	if request.method == 'POST':
		form = forms.FormName(request.POST)

		if form.is_valid():
			print("validation success!")
			print(form.cleaned_data['name'])
			print(form.cleaned_data['email'])
			print(form.cleaned_data['text'])

	return render(request, 'appOne/form_page.html', {'form': form})

def sign_up_page(request):
	form = forms.SignUpForm()

	if request.method == 'POST':
		form = forms.SignUpForm(request.POST)

		if form.is_valid():
			print("validation success!")
			new_user = form.save()
			return index(request)
		else:
			print('error')

	return render(request, 'appOne/sign_up.html', {'form': form})