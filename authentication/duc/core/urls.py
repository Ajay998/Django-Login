from  django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('signup/',SignupView.as_view(),name='signup'),
    path('login/',MyloginView.as_view(),name='login')
]