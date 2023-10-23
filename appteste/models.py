from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField()
    content = models.TextField()
    created_on = models.DateTimeField(date_now=:qa
                                      )
    modified_on = models.TextField()
