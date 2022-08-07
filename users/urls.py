from django.urls import path

from .views import *

urlpatterns = [
    path('users/signup/', SignUpView.as_view(), name='signup'),
]
