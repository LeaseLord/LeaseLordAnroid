from django.urls import path
from postAnnouncement import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('announcements/', views.displayannouncement),
   path('newannouncement/', views.postAnnouncement),
]
