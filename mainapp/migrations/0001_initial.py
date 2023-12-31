# Generated by Django 3.2.23 on 2023-12-19 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='Image/')),
                ('content', models.CharField(max_length=100000)),
                ('date', models.DateField()),
            ],
        ),
    ]
