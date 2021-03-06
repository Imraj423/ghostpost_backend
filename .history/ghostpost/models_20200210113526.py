from django.db import models


class ghostPost(models.Model):
    title = models.CharField(max_length=30)
    isRoast = models.BooleanField()
    submitDate = models.DateField()

    def __str__(self):
        return self.title
