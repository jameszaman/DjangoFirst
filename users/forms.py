from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
   email = forms.EmailField() #need to import this

   class Meta: #making a class which will tell our form additional data
      model = User # which table will our form use
      fields = [ # the order in which fields will be show in our form
         'username',
         'email',
         'password1', #not sure why password1 and 2. Maybe you have 
         'password2'  # to write them like this?
      ]

