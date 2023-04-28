from django.db import models

# Create your models here.
class Marksheet(models.Model):
    rollno=models.IntegerField(max_length=20, db_column="St_Rollno")
    name=models.CharField(max_length=30)
    physics=models.FloatField(max_length=3)
    chemistry=models.FloatField(max_length=3)
    maths=models.FloatField(max_length=3)

    def __str__(self):
         return f"{self.name}"