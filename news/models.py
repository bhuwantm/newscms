import datetime

from ckeditor.fields import RichTextField
from django.db import models


class NewsCategory(models.Model):
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()


class Tags(models.Model):
    name = models.CharField(max_length=50, unique=True)
    display_name = models.CharField(max_length=200,unique=True)
    description = models.CharField(max_length=200)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()


class News(models.Model):
    news_type = (
        ('National', 'National'),
        ('International', 'International')
    )

    category = models.ForeignKey(NewsCategory, on_delete=models.PROTECT, related_name='cat_news')
    type = models.CharField(max_length=20, choices=news_type, default='National')
    author = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, unique=True)
    synopsis = models.CharField(max_length=100, null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    body = RichTextField()
    tags = models.ManyToManyField(Tags, blank=True)
    presentation_image = models.ImageField(null=True, blank=True)

    views_counter = models.PositiveIntegerField(default=0)
    likes_counter = models.PositiveIntegerField(default=0)
    create_ts = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return "{} | {} | {}".format(
            self.title,
            self.category.name,
            ' / '.join([x.name for x in self.tags.all()])
        )

    def __unicode__(self):
        return self.__str__()


class Ads(models.Model):
    name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    presentation_image = models.ImageField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()
