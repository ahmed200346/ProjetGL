from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView
from django.urls import reverse
from .forms import RegisterForm,CustomUserChangeForm
from .models import User
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import redirect
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
class HomeView(TemplateView):
    template_name = "users/home.html"
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login') 
class UserUpdateView(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('user_details')  # Redirige vers la page de détails de l'utilisateur après la mise à jour

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Vos informations ont été mises à jour avec succès !')
        return super().form_valid(form)  
    def get_success_url(self):
        return reverse('user_details', kwargs={'pk': self.object.pk})
class DeleteUser(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'  # Template de confirmation
    context_object_name = 'user'  # Nom de la variable utilisée dans le template
    success_url = reverse_lazy('login')
    def get_object(self, queryset=None):
        return self.request.user  # Récupère l'utilisateur connecté

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()  # Supprime l'utilisateur
        return redirect(self.success_url)