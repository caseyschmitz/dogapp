from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Breed(models.Model):
    TINY = 'tiny'
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
    BREED_SIZE_CHOICES = [
        (TINY, 'Tiny'), 
        (SMALL, 'Small'), 
        (MEDIUM, 'Medium'), 
        (LARGE, 'Large')
    ]

    name = models.CharField(max_length=100, unique=True, blank=False)
    size = models.CharField(max_length=6, choices=BREED_SIZE_CHOICES)
    friendliness = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    trainability = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    sheddingamount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    exerciseneeds = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.name

class Dog(models.Model):
    name = models.CharField(max_length=100, blank=False)
    age = models.PositiveIntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, blank=False)
    color = models.CharField(max_length=20, blank=False)
    favoritefood = models.CharField(max_length=100, blank=False)
    favoritetoy = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name
