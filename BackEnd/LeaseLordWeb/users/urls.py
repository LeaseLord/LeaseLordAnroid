from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('register/', views.registercheck),
   path('login/', auth_views.LoginView.as_view()),
<<<<<<< HEAD
   path('registerten/', views.registerten),
   path('registerland/', views.registerland)
=======
   path('registerten/',views.registerten),
>>>>>>> 305dba5faea05c46f06739e4c13147b8ccab3210
]
