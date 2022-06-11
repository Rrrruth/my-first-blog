# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 15:29:36 2022

@author: ruthv
"""

from django.urls import path
from . import views

urlpatterns= [path('',views.post_list, name='post-list'),
              ]
