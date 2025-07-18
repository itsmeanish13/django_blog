from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_detail, name='post_detail'), 
    path('post/<int:id>/', views.bio, name='bio'),
]