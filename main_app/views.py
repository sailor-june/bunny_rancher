from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import (
 
    DetailView,
)
from django.contrib.auth import login

import random, math

from .models import Bunny

# Create your views here.
from django.http import HttpResponse


def change_bunny(request):
    current_bunny = Bunny.objects.filter(user=request.user.id, active=False)
    bunnies = Bunny.objects.exclude(id=current_bunny.id)

    if request.method == "POST":
        
        new_bunny_id = request.POST.get("bunny")
        current_bunny.active = False
        current_bunny.save()
        new_bunny = Bunny.objects.get(id=new_bunny_id)
        new_bunny.active = True
        new_bunny.save()
        return redirect("change_bunny")

    if (Bunny.objects.get(user=request.user.id, active=True)):
        context = {
            "current_bunny": current_bunny,
            "bunnies": bunnies,
        }
    else: 
        context={
            "bunnies":bunnies
        }
    return render(request, "change_bunny.html", context)


def add_strength(request, pk):
    bunny = Bunny.objects.get(pk=pk)
    bunny.add_str()
    bunny.save()
    return redirect("training", pk=bunny.pk)


def add_speed(request, pk):
    bunny = Bunny.objects.get(pk=pk)
    bunny.add_spd()
    bunny.save()
    return redirect("training", pk=bunny.pk)


def add_intell(request, pk):
    bunny = Bunny.objects.get(pk=pk)
    bunny.add_int()
    bunny.save()
    return redirect("training", pk=bunny.pk)


def add_defense(request, pk):
    bunny = Bunny.objects.get(pk=pk)
    bunny.add_def()
    bunny.save()
    return redirect("training", pk=bunny.pk)


def create_bunny(request):
    new_bunny = Bunny(
        hp=random.randint(10, 20),
        level=1,
        intell=random.randint(1, 10),
        defense=random.randint(1, 10),
        strength=random.randint(1, 10),
        speed=random.randint(1, 10),
        color=random.choice(["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]),
        experience=0,
        user=request.user,
        name="",
        active=False,
        parent_1='',
        parent_2=''
    )
    return render(request, "bunnies/generate_bunny.html", {"bunny": new_bunny})


def add_bunny(request):
    if request.method == "POST":
        if request.POST.get("name")=="":
            return redirect('home')
        hp = request.POST.get("hp")
        level = request.POST.get("level")
        intelligence = request.POST.get("intell")
        defense = request.POST.get("defense")
        strength = request.POST.get("strength")
        speed = request.POST.get("speed")
        color = request.POST.get("color")
        experience = request.POST.get("experience")
        name = request.POST.get("name")
        
        parent_1 = request.POST.get("parent_1")
        parent_2 = request.POST.get("parent_2")

        bunny = Bunny.objects.create(
            name=name,
            hp=hp,
            level=level,
            intell=intelligence,
            defense=defense,
            strength=strength,
            speed=speed,
            color=color,
            t_days=10,
            active=False,
            experience=experience,
            user=request.user,
            parent_1=parent_1,
            parent_2=parent_2
        )
        
        if request.POST.get("confirm") == 'on':
            colors = ["Red","Orange","Yellow","Green", "Blue", "Purple"]
            bunny.active=True
            bunny.color = random.choice(colors)
            bunny.save()

            # get the parent bunnies ids and set them to b1 and b2
            
            
            b1 = Bunny.objects.get(id=parent_1.split(':')[1])
            b2 = Bunny.objects.get(id=parent_2.split(':')[1])
            b1.delete()
            b2.delete()
        else:
            bunny.save()
        
        return redirect("bunnies")
    else:
        return redirect("generate_bunny")


def combine_bunny(request):
    if request.method == "POST":
        b1_id = request.POST.get("bunny_1")
        b2_id = request.POST.get("bunny_2")
        if b1_id == b2_id:
            return redirect('combine_bunnies')
        
        # Get the two selected bunnies from the database
        b1 = Bunny.objects.get(id=b1_id)
        b2 = Bunny.objects.get(id=b2_id)
        if b1.active or b2.active:
            return redirect('combine_bunnies')
        # Generate a new bunny with the average stats of the two selected bunnies
        new_bunny = Bunny(
            hp=int(math.floor(b1.hp + b2.hp) / 2),
            level=int(math.floor(b1.level + b2.level) / 2),
            intell=int(math.floor(b1.intell + b2.intell) / 2),
            defense=int(math.floor(b1.defense + b2.defense) / 2),
            strength=int(math.floor(b1.strength + b2.strength) / 2),
            speed=int(math.floor(b1.speed + b2.speed) / 2),
            color="????",
            experience=int(math.floor(b1.experience + b2.experience) / 2),
            user= request.user,
            name="New Bunny",
            t_days=10,
            active=False,
        )
        
        
        return render(
            request,
            "combine_bunny.html",
            {"new_bunny": new_bunny, "bunny_1": b1, "bunny_2": b2},
            )
    bunnies = Bunny.objects.filter(user=request.user.id)
    return render(request, "combine_bunny.html", {"bunnies": bunnies})


class BunnyDetail(DetailView):
    model = Bunny
    fields = "__all__"



def sign_up(request):
    error_message=''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message='invalid_credentials'    
    #send form template
    form = UserCreationForm()
    return render(request, 'sign_up.html', {
        'form': form,
        'error': error_message
    })




def home(request):
    bunny = Bunny.objects.filter(user=request.user.id, active=True)
    return render(request, "home.html", {"bunny": bunny})


def about(request):
    return render(request, "about.html")


def bunnies_index(request):
    bunnies = Bunny.objects.filter(user=request.user.id)
    return render(request, "bunnies/index.html", {"bunnies": bunnies})


def bunnies_detail(request, bunny_id):
    bunny = Bunny.objects.get(id=bunny_id)
    return render(request, "bunnies/detail.html", {"bunny": bunny})


def training_index(request, pk):
    if Bunny.objects.filter(user=request.user.id, active=True):
        bunny = Bunny.objects.filter(user=request.user.id, active=True)
        
        return render(request, "bunnies/training.html", {"bunny": bunny})
    else:
        return render(request, "home.html")
