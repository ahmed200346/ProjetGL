from django.urls import path
from .views import *


urlpatterns = [ 
    path('user/details/<int:pk>/', UserDetails.as_view(), name='user_details'),
    path('signup/', Register.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
]