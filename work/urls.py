from django.urls import path, re_path, include
from . import views

app_name = 'work'

urlpatterns = [
	path('', views.work, name='work'),
]
