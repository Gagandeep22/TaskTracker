from django.conf.urls import url
from . import views

app_name = 'todo'

urlpatterns = [
    url(r'^home/', views.IndexView.as_view(), name='index'),
    url(r'todo/ns/$', views.FilterView.as_view(), {'status': 'Not Started'}, name='not-start'),
    url(r'todo/d/$', views.FilterView.as_view(), {'status': 'Done'}, name='done'),
    url(r'todo/ip/$', views.FilterView.as_view(), {'status': 'In Progress'}, name='in-progress'),
    url(r'todo/create/$', views.TodoCreate.as_view(), name='todo-add'),
    url(r'todo/(?P<pk>[0-9]+)/$', views.TodoUpdate.as_view(), name='todo-update'),
    url(r'todo/(?P<pk>[0-9]+)/delete/$', views.TodoDelete.as_view(), name='todo-delete'),

]