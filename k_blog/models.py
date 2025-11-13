from django.db import models

# Create your models here.
class KPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    #picture = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
