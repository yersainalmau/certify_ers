# Generated by Django 2.2 on 2019-04-11 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cert', '0008_person_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.CharField(default='', max_length=10),
        ),
    ]