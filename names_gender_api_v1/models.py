import imp
from operator import mod
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


from django.contrib.auth import get_user_model
# Create your models here.

class Names_Gender(models.Model):


    WHATEVER_CHOICE = 'unknown'
    MALE_CHOICE = 'male'
    FEMALE_CHOICE = 'female'
    SAMPLE_CHOICES = (
        (WHATEVER_CHOICE ,'unknown'),
        ( MALE_CHOICE, 'Male'),
        ( FEMALE_CHOICE, 'Female'),
    )
    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE , related_name='names_gender')
    the_name = models.CharField(max_length=256)
    gender = models.CharField(choices= SAMPLE_CHOICES, max_length=256, default= WHATEVER_CHOICE) 
    accurate = models.IntegerField(default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
     )
    data_created_at = models.DateTimeField(auto_now_add=True)
    data_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.the_name
