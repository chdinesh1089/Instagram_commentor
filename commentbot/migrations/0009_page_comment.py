# Generated by Django 2.2.5 on 2019-09-17 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentbot', '0008_auto_20190917_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='comment',
            field=models.CharField(default='hi there!', max_length=200),
        ),
    ]
