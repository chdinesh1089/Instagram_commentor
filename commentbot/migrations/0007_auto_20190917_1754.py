# Generated by Django 2.2.5 on 2019-09-17 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commentbot', '0006_auto_20190917_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
