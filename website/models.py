from django.db import models


class Social(models.Model):
    youtube = models.CharField(verbose_name="YouTube", max_length=200, null=True, blank=True)
    twitter = models.CharField(verbose_name="Twitter", max_length=200, null=True, blank=True)
    instagram = models.CharField(verbose_name="Instagram", max_length=200, null=True, blank=True)
    facebook = models.CharField(verbose_name="Facebook", max_length=200, null=True, blank=True)
    linkedin = models.CharField(verbose_name="LinkedIn", max_length=200, null=True, blank=True)
    reddit = models.CharField(verbose_name="Reddit", max_length=200, null=True, blank=True)
