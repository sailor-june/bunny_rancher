from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
import random

from .models import Bunny
# Create your views here.
from django.http import HttpResponse


def change_bunny(request):
    current_bunny = Bunny.objects.get(active=True)
    bunnies = Bunny.objects.exclude(id=current_bunny.id)

    if request.method == 'POST':
        new_bunny_id = request.POST.get('bunny')
        current_bunny.active = False
        current_bunny.save()
        new_bunny = Bunny.objects.get(id=new_bunny_id)
        new_bunny.active = True
        new_bunny.save()
        return redirect('change_bunny')

    context = {
        'current_bunny': current_bunny,
        'bunnies': bunnies,
    }
    return render(request, 'change_bunny.html', context)







def add_strength(request, pk):
    bunny = Bunny.objects.get(pk=pk)
    bunny.add_str()
    bunny.save()
    return redirect('training', pk=bunny.pk )
def add_speed(request, pk):
    bunny = Bunny.objects.get(pk=pk)
    bunny.add_spd()
    bunny.save()
    return redirect('training', pk=bunny.pk )
def add_intell(request, pk):
    bunny = Bunny.objects.get(pk=pk)
    bunny.add_int()
    bunny.save()
    return redirect('training', pk=bunny.pk )
def add_defense(request, pk):
    bunny = Bunny.objects.get(pk=pk)
    bunny.add_def()
    bunny.save()
    return redirect('training', pk=bunny.pk )

def create_bunny(request):
    new_bunny = Bunny(
        hp = random.randint(10, 20),
        level = 1,
        intell = random.randint(1, 10),
        defense = random.randint(1, 10),
        strength = random.randint(1, 10),
        speed = random.randint(1, 10),
        color = random.choice(['red','orange','yellow','green','blue','purple']),
        experience = 0,
        owner = "",
        name = "",
        active = False
    )
    return render(request, 'bunnies/generate_bunny.html', {'bunny':new_bunny})
 

def add_bunny(request):
    if request.method == 'POST':
        
        hp = request.POST.get('hp')
        level = request.POST.get('level')
        intelligence = request.POST.get('intell')
        defense = request.POST.get('defense')
        strength = request.POST.get('strength')
        speed = request.POST.get('speed')
        color = request.POST.get('color')
        experience = request.POST.get('experience')
        name = request.POST.get('name')
        
        

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
        experience=experience
    )
        bunny.save()
        return redirect('bunnies')
    else:
        return redirect('generate_bunny')




class BunnyDetail(DetailView):
  model = Bunny
  fields = '__all__'




def home(request):
    bunny= Bunny.objects.get(active=True)
    return render(request, 'home.html',{'bunny':bunny})

def about(request):
    return render(request, 'about.html')

def bunnies_index(request):
    bunnies = Bunny.objects.all
    return render(request, 'bunnies/index.html', {'bunnies': bunnies })

def bunnies_detail(request, bunny_id):
    bunny = Bunny.objects.get(id=bunny_id)
    return render(request, 'bunnies/detail.html', { 'bunny' : bunny } )

def training_index(request, pk):
    bunny= Bunny.objects.get(id=pk)
    return render(request, 'bunnies/training.html', {'bunny':bunny})