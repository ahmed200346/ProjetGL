from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'biography','is_artist']  
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
