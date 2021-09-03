from django.urls import path
from log_pay.views import *
from . import views
app_name = 'log_pay'
urlpatterns = [
    path('accounts/pass_reset/', views.password_reset, name='password_reset'),
    path('accounts/registration/', views.registration, name='registration'),
    path('accounts/logout/', views.logout, name='logout'),
    path('', views.index, name='index'),
    path('prognoz/', views.prognoz, name='prognoz'),
    path('edit/', views.edit, name='edit'),
]