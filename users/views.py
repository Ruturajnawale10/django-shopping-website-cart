from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':           #when you click submit button, it comes back here to check if form is valid
        form = UserCreationForm(request.POST) #imfo from the submitted form is loaded back here
        if form.is_valid():
            form.save()                       #user is created
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created!You can now login')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form' : form})
