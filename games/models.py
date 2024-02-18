from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Game(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    owner = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    slug = models.SlugField(unique= True)
    price = models.DecimalField(max_digits= 6, decimal_places= 2)
    created = models.DateTimeField(auto_now_add= True)
    update_time = models.DateTimeField(auto_now= True)
    image = models.ImageField(blank = True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('game', args = [self.slug])
    
    

# Create your models here.
