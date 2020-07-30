from django.urls import path
from .views import SignUpView,CustomerCreate

urlpatterns = [
    path('signup/',CustomerCreate.as_view(),name='signup'),
]