from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . models import blog

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}), )

	
	class Meta:
		model = User
		fields = ('id','username',  'email', 'password1', 'password2',)

	def __init__(self, *args, **kwargs):
	    super(SignUpForm, self).__init__(*args, **kwargs)
	    self.fields['username'].widget.attrs['class'] = 'form-control'
	    self.fields['username'].widget.attrs['placeholder'] = 'User Name'
	    self.fields['username'].label = ''
	    
	    self.fields['password1'].widget.attrs['class'] = 'form-control'
	    self.fields['password1'].widget.attrs['placeholder'] = 'Password'
	    self.fields['password1'].label = ''
	    
	    self.fields['password2'].widget.attrs['class'] = 'form-control'
	    self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
	    self.fields['password2'].label = ''
	    



class blog_form(forms.ModelForm):
	photo = forms.ImageField()
	title = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'title'}))
	content = forms.CharField(label="" ,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'content'}))
	
	class Meta:
		model = blog
		fields = '__all__'
