from django.db import models

# Create your models here.

class Students(models.Model):
    std_rn = models.CharField(max_length=100)
    std_name = models.CharField(max_length=100)
    std_contact = models.CharField(max_length=100)
    std_email = models.EmailField()
    def __str__(self):
        return self.std_name