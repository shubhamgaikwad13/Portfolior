from django.urls import path
from core import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('signup', views.signup, name='signup'),
    path('portfolio', views.portfolio, name='portfolio'),
]
