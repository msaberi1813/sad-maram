from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='post_list'),
    url(r'^upload_file$', views.upload_file, name='upload_file'),
    url(r'^profile$', views.profile, name='profile'),

]