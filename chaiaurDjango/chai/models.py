from django.db import models
from django.utils import timezone
# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICES = [
        ('ML','MASALA'),
        ('GR', 'GINGER'),
        ('KL','KIWI'),
        ('PL', 'PLAIN')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'chais/')
    date_added = models.DateTimeField(default=timezone.now)
    types = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES)


    def __str__(self):
        return self.name