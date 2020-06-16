from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    # home page
    url(r'^$', views.index, name='index'),
    
    path('sample/json/', views.sampleJson),

]
