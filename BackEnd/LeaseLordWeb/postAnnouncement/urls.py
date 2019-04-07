from django.urls import path
from postAnnouncement import views
from django.contrib.auth import views as auth_views

urlpatterns = [

   path('post/', views.post),
  # path('view/', views.view)

]
