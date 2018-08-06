from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='post_list'),
    url(r'^upload_file$', views.upload_file, name='upload_file'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^edit$', views.edit, name='edit'),
    url(r'^ch_pass$', views.bala_pass, name='bala_pass'),
    url(r'^edit_user_profile$', views.edit_user_profile, name='edit_user_profile'),
    url(r'^change_pass$', views.change_pass, name='change_pass'),
    url(r'^bala_add_employee$', views.bala_add_employee, name='bala_add_employee'),
    url(r'^add_employee$', views.add_employee, name='add_employee'),

]