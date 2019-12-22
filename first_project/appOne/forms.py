# from django import forms
from django.forms import ModelForm
from django.core import validators

from appOne.models import User

# def check_for_z(value):
# 	if value[0].lower() != 'z':
# 		raise forms.ValidationError('name needs to start with z')

# class FormName(forms.Form):
# 	name = forms.CharField(validators=[check_for_z])
# 	email = forms.EmailField()
# 	verify_email = forms.EmailField(label='Enter your email again:')
# 	text = forms.CharField(widget=forms.Textarea)
# 	botcatcher = forms.CharField(required = False,
# 								widget=forms.HiddenInput,
# 								validators=[validators.MaxLengthValidator(0)])

# 	def clean(self):
# 		all_clean_data = super().clean()
# 		email = all_clean_data['email']
# 		vemail = all_clean_data['verify_email']

# 		if email != vemail:
# 			raise forms.ValidationError('emaisl not correct')


class SignUpForm(ModelForm):
	class Meta:
		model = User
		fields = '__all__'
	# name = forms.CharField()
	# last_name = forms.CharField()
	# email = forms.EmailField()
	# verify_email = forms.EmailField(label='Enter your email again:')

	def clean(self):
		all_clean_data = super().clean()
		print(all_clean_data)
		# email = all_clean_data['email']
		# vemail = all_clean_data['verify_email']

		# if email != vemail:
		# 	raise forms.ValidationError('emails not correct')