from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
   if request.method == "POST":
      form = UserRegisterForm(request.POST) # need to import
      if form.is_valid():
         form.save()
         username = form.cleaned_data.get('username')
         messages.success(request, f'Account {username} successfully created') #need to import
         return redirect('blog-home') # need to import
   else:
      form = UserRegisterForm()
   return render(request, 'users/register.html', {'form': form})

@login_required # need to import this
def profile(request):
   return render(request, 'users/profile.html')
