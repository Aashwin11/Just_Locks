from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.index, name = 'home'),
    path("lock_keep", views.lock_keep, name = 'lock_keep'),
    path("in_out", views.in_out, name = 'in_out'),
    path("selectee", views.selectee, name = 'selectee'),
    path("payment", views.payment, name = 'payment'),
    path("qr_pay", views.qr_pay, name = 'qr_pay'),
    path("success", views.success, name = 'success'),
    path("login", views.login, name = 'login'),
    path("signup", views.signup, name = 'signup')
]
