from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),#todo change to the homepage (should be in 3 part for each diffrent usr)
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
    url(r'^(?P<pke>\d+)/emp_transactions$', views.see_employee_transactions, name='see_employee_transactions'),
    url(r'^(?P<pkt>\d+)/emp_transactions_context$', views.see_transaction_context, name='see_transaction_context'),
    url(r'^bala_edit_emp$', views.bala_edit_emp, name='bala_edit_emp'),
    url(r'^edit_employee_profile$', views.edit_employee_profile, name='edit_employee_profile'),
    url(r'^bala_edit_manager$', views.bala_edit_manager, name='bala_edit_manager'),
    url(r'^edit_manager_profile$', views.edit_manager_profile, name='edit_manager_profile'),
    url(r'^(?P<pke>\d+)/usr_transactions$', views.see_usr_transactions, name='see_usr_transactions'),
    url(r'^(?P<pke>\d+)/usrProfile$', views.see_usr_profile, name='see_usr_profile'),
    url(r'^usr_list$', views.usr_list, name='employee_list'),
    url(r'^(?P<pke>\d+)/usr_ban$', views.ban_usr, name='ban-usr'),
    url(r'^(?P<pke>\d+)/ban_emp$', views.ban_emp, name='ban_employee'),
    url(r'^arz_convert$', views.tabdil_arz, name='arz_convert'),

    url(r'^nerkh_arz$', views.nerkh_arz2, name='nerkh_arz'),

]