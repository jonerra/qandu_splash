from django.conf.urls import patterns, include, url
from .views import *

url patterns = patterns ('',
                         url(r'^$', Home.as_view(), name='home'),
                        )