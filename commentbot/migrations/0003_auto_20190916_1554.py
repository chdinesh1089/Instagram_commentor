# Generated by Django 2.2.5 on 2019-09-16 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentbot', '0002_auto_20190914_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='latest_post_id',
            field=models.CharField(default='na', max_length=40),
        ),
        migrations.AddField(
            model_name='page',
            name='task_id',
            field=models.CharField(default='na', max_length=60),
        ),
    ]