from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView 
from django.urls import reverse
from .forms import RegisterForm
from .models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
class Register(CreateView):
    
    model=User
    form_class= RegisterForm
    template_name = "users/signup.html"
    success_url = reverse_lazy('login')
class Login(LoginView):
    template_name="users/login.html"
    
    def get_success_url(self):
        return reverse('home')

class UserDetails(LoginRequiredMixin, DetailView):
    model = User
    template_name = "users/details.html"
    context_object_name = "user_details"  