from django.contrib import admin
from django.urls import path, include
from authentication import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('userView', views.userView, name="userView"),
    path('selectBus', views.selectBus, name="selectBus"),
    path('pdetails', views.pdetails, name="pdetails"),
    path('thankyou', views.thankyou, name="thankyou"),
]
