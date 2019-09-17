from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Page(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    account_id = models.CharField(max_length=30)
    RUN_STATUS = [
        ('yes', 'yes'),
        ('no', 'no')
    ]
    run_status = models.CharField(max_length=3,choices=RUN_STATUS,default='no')
    latest_post_id = models.CharField(max_length=30,default='na')
    task_id = models.CharField(max_length=60,default='na')
    comment = models.CharField(max_length=200,default='hi there!')

    def __str__(self):
        return self.account_id

class LoginDetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,unique=True)
    account_id = models.CharField(max_length=30)
    password = models.CharField(max_length=30)