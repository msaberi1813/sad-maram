from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('', views.profile, name='post_list'),#todo change to the homepage
    url(r'^upload_file$', views.upload_file, name='upload_file'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^edit$', views.edit, name='edit'),
    url(r'^ch_pass$', views.bala_pass, name='bala_pass'),
    url(r'^edit_user_profile$', views.edit_user_profile, name='edit_user_profile'),
    url(r'^change_pass$', views.change_pass, name='change_pass'),
    url(r'^bala_add_employee$', views.bala_add_employee, name='bala_add_employee'),
    url(r'^add_employee$', views.add_employee, name='add_employee'),
    url(r'^employee_list$', views.employee_list, name='employee_list'),
    url(r'^(?P<pke>\d+)/empProfile$', views.see_employee_profile, name='see_employee_profile'),
    url(r'^(?P<pke>\d+)/change_salaryyy$', views.bala_change_employee_salary, name='change_empsalary'),
    url(r'^(?P<pke>\d+)/change_salary$', views.change_salary, name='change_salary'),

]