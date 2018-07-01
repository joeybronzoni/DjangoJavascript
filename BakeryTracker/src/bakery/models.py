from django.db import models
from django.contrib.postgres.fields import ArrayField
from datetime import datetime

# Create your models here.
class Orders(models.Model):
    customer   = models.CharField(max_length=120, blank=True)
    mixins = models.CharField(max_length=1000, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    # mixins = ArrayField(
    #     ArrayField(
    #         models.CharField(max_length=10, blank=True),
    #         size=12,
    #     ),
    #     size=12,
    # )


    class Meta:
        verbose_name_plural = "Orders"
