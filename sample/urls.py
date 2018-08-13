from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login
from accounts.views import Index
from accounts import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^accounts/logout/$', logout_then_login, name='logout'),
    url(r'^accounts/index/$', views.form, name='account_index'),
    url(r'^list/', views.list, name='list'),
]