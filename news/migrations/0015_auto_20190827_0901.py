# Generated by Django 2.2 on 2019-08-27 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_auto_20190827_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newscategory',
            name='display_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tags',
            name='display_name',
            field=models.CharField(max_length=200),
        ),
    ]
