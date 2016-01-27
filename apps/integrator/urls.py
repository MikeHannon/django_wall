from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
app_name = 'integrator'
urlpatterns = [
    url(r'^$', views.login_2.as_view(), name = 'login'),
    url(r'^register/?$', views.register.as_view(), name = 'register'),
    url(r'^the_wall/?$',views.index, name = 'index'),
    url(r'^create/?$', views.create_message.as_view(), name = 'create_message'),
    url(r'^create_comment/?$', views.create_comment.as_view(), name = 'create_comment'),
]
