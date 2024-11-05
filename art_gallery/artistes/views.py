
"""""
from django.shortcuts import render, redirect
from users.models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        # Vérification de l'unicité de l'email (facultatif)
        if User.objects.filter(email=email).exists():
            messages.error(request, "Cet email est déjà utilisé.")
            return redirect('register')

        # Création d'un nouvel utilisateur
        user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email
        )

        # Utilisation de set_password pour sécuriser le mot de passe
        user.set_password(password)
        user.save()
        messages.success(request, "Inscription réussie !")
        return redirect('login')

    return render(request, 'users/register.html')
"""