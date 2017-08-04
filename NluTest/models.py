from django.db import models


# Create your models here.
class TestCase(models.Model):
    qus = models.CharField(max_length=3000)
    ans = models.CharField(max_length=5000)

    def __str__(self):
        return self.qus