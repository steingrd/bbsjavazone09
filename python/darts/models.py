#!/usr/bin/env python

from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    estimate = models.IntegerField()
    score = models.IntegerField(blank=True, null=True)
    result = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.email
