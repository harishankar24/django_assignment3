from django.db import models

# Create your models here.
class Course(models.Model):
    cname = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    instructor = models.CharField(max_length=40)
    rating = models.DecimalField(blank=True, max_digits=3, decimal_places=1)

    class Meta:
        db_table = 'course'