from django.urls import path
from .views import login_view, success_view, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('success/', success_view, name='success'),
    path('logout/', logout_view, name='logout'),
]
