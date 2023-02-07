from django.db import models
import random


# Create your models here.

class Bunny(models.Model):
        hp =  models.IntegerField()
        level = models.IntegerField()
        intell = models.IntegerField()
        defense  = models.IntegerField()
        strength  = models.IntegerField()
        speed  =models.IntegerField()
        color = models.CharField(max_length=20)
        experience  =  models.IntegerField()
        owner = models.CharField(max_length=20)
        name  = models.CharField(max_length=20)
        active = models.BooleanField()


       
        def add_str(self):
                self.strength +=(random.randint(5,10))
                self.speed -=(random.randint(1,4))
        
# bunnies= [
#     Bunny('Alpha', 1, 0, 10, 5, 5, 5, 5, 'RED', 0000, False),
#     Bunny('Alpha', 1, 0, 10, 5, 5, 5, 5, 'BLUE', 0000, False),
#     Bunny('Alpha', 1, 0, 10, 5, 5, 5, 5, 'YELLOW', 0000, False)

# ]