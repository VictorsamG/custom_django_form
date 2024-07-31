from django.urls import path
from . import views

urlpatterns = [
    path('form/',views.login_user, name='login'),
]
