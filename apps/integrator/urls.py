from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
app_name = 'integrator'
urlpatterns = [
    url(r'^$', views.login.as_view(), name = 'login'),
    url(r'^register/?$', views.register.as_view(), name = 'register'),
    #url(r'^index/?$',views.index, name = 'index'),
]
