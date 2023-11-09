from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class User(models.Model):
    
    name = models.TextField(max_length=100, validators=[MinLengthValidator(4)])
    email = models.EmailField(max_length=200, default='x')
    job_title = models.TextField(validators=[MinLengthValidator(14)], max_length=200)
    password = models.CharField(validators=[MinLengthValidator(6)], max_length = 200)

    def __str__(self):
        return self.name

