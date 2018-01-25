from django.db import models


class Portfolio(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='portfolio/%Y/%m/%d/')
    description = models.TextField()

    start_date = models.DateField()
    end_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0}. {1}'.format(self.pk, self.title)
