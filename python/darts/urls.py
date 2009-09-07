#!/usr/bin/env python

from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

import views

urlpatterns = patterns('',
  url('^$', views.register_player),
  url('^throw_darts/$', views.register_result),
  url('^your_score/$', views.your_score),
)
