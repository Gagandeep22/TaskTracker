from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'login'

urlpatterns = [
    url(r'^$', auth_views.login, name='login'),
    url(r'^', include('todo.urls', namespace='todo')),
    url(r'^register/', views.Register.as_view(), name='register'),
]