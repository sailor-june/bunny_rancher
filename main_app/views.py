from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


from .models import Bunny
# Create your views here.
from django.http import HttpResponse


def add_strength(request, pk):
    bunny = Bunny.objects.get(pk=pk)
    bunny.add_str()
    bunny.save()
    return redirect('detail', pk=bunny.pk )



 
class BunnyDetail(DetailView):
  model = Bunny
  fields = '__all__'


def home(request):
    return HttpResponse('<h1>uwu  </h1>')

def about(request):
    return render(request, 'about.html')

def bunnies_index(request):
    bunnies = Bunny.objects.all
    return render(request, 'bunnies/index.html', {'bunnies': bunnies })

def bunnies_detail(request, bunny_id):
    bunny = Bunny.objects.get(id=bunny_id)
    return render(request, 'bunnies/detail.html', { 'bunny' : bunny } )

def training_index(request, bunny_id):
    bunny= Bunny.objects.get(id=bunny_id)
    return render(request, 'bunnies/training.html', {'bunny':bunny})