from django.db import models

# Create your models here.


class News(models.Model):
    anchor = models.CharField(max_length=70)
    title = models.CharField(max_length=80)
    description = models.TextField()


    def __str__(self):
        return self.anchor


class SportNews(models.Model):
    anchor = models.CharField(max_length=70)
    title = models.CharField(max_length=80)
    description = models.TextField()


    def __str__(self):
        return self.anchor
