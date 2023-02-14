from django.contrib.auth.models import User

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
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        name  = models.CharField(max_length=20, unique=True)
        t_days = models.IntegerField()
        # active = models.BooleanField()
        parent_1 = models.CharField(max_length=200)
        parent_2= models.CharField(max_length=200)



        def add_str(self):
                if self.t_days==0:
                        return
                else:
                        self.t_days -=1
                        dice_a = random.randint(5,8)
                        dice_b = random.randint(1,4)
                        self.strength +=(dice_a)
                        self.speed -=(dice_b)
                        self.experience += (dice_a/dice_b)
        
        def add_spd(self):
                if self.t_days==0:
                        return
                else:
                        self.t_days -=1
                        dice_a = random.randint(5,8)
                        dice_b = random.randint(1,4)
                        self.experience += (dice_a/dice_b)
                        self.speed +=(dice_a)
                        self.intell -=(dice_b)
       
        def add_int(self):
                if self.t_days==0:
                        return
                else:
                        self.t_days -=1
                        dice_a = random.randint(5,8)
                        dice_b = random.randint(1,4)
                        self.experience += (dice_a/dice_b)
                        self.intell +=(dice_a)
                        self.defense -=(dice_b)
        
        def add_def(self):
                if self.t_days==0:
                        return
                else:
                        self.t_days -=1
                        dice_a = random.randint(5,8)
                        dice_b = random.randint(1,4)
                        self.experience += (dice_a/dice_b)
                        self.defense +=(dice_a)
                        self.strength -=(dice_b)

        def put_away(self):
                self.active=False 
        def take_out(self):
                self.active=True  
# bunnies= [
#     Bunny('Alpha', 1, 0, 10, 5, 5, 5, 5, 'RED', 0000, False),
#     Bunny('Alpha', 1, 0, 10, 5, 5, 5, 5, 'BLUE', 0000, False),
#     Bunny('Alpha', 1, 0, 10, 5, 5, 5, 5, 'YELLOW', 0000, False)

# ]