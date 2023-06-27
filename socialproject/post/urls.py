from django.urls import path,include
from . import views

urlpatterns = [
    path('create/',views.post_create,name='create_post'),
]
