# Generated by Django 2.2.5 on 2019-12-15 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appOne', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
