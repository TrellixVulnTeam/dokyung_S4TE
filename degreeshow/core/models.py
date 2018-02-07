from django.db import models

class ArtWork(models.Model):
    title = models.CharField(max_length=30)
    creater = models.CharField(max_length=5)
    image = models.ImageField(upload_to='artwork/%Y/%m/%d/')
    description = models.TextField()

    def __str__(self):
        return '{0}. {1}'.format(self.pk, self.title)