from django.db import models

class post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()
    



