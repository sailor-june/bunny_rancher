from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about, name='about'),
    path('bunnies/', views.bunnies_index, name='bunnies'),
    path('bunnies/<int:pk>/', views.BunnyDetail.as_view(), name='detail'),
    path('bunnies/train/<int:bunny_id>/', views.training_index, name='training'),
        path('bunny/<int:pk>/add_strength/', views.add_strength, name='add_strength'),
        ]
