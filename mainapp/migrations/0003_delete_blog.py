# Generated by Django 3.2.23 on 2023-12-19 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_blog_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
