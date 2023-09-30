from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignupForm


# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/signup.html"

def SignUpView(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add additional actions here, like sending a welcome email
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = SignupForm()

    return render(request, 'registration/signup.html', {'form': form})