from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name = "index"),
        url(r'^addcourse$', views.addcourse),
        url(r'^courses_app/remove/(?P<id>\d+)$', views.remove), 
]
