# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import SellPair, Sell


admin.site.register(SellPair)
admin.site.register(Sell)
