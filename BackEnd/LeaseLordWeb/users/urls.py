from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('register/', views.registercheck),
   path('login/', views.user_login),
   path('registerten/',views.registerten),
   path('registerpm/', views.registerpm),
   path('profile/',views.profile),
   path('logout/',views.log_out),
]
