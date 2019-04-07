from django.urls import path
from maintenance import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('tickets/', views.displayticket),
   path('newticket/', views.newticket),
]
