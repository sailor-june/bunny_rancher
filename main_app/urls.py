from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home, name='landing'),
    path('home/', views.home, name='home'),
    path('about/',views.about, name='about'),
    path('bunnies/', views.bunnies_index, name='bunnies'),
    path('bunnies/<int:pk>/', views.BunnyDetail.as_view(), name='detail'),
    path('bunnies/train/<int:pk>/', views.training_index, name='training'),
    path('bunny/<int:pk>/add_strength/', views.add_strength, name='add_strength'),
    path('bunny/<int:pk>/add_speed/', views.add_speed, name='add_speed'),
    path('bunny/<int:pk>/add_defense/', views.add_defense, name='add_defense'),
    path('bunny/<int:pk>/add_intell/', views.add_intell, name='add_intell'),        
    path('generate/', views.create_bunny, name='generate_bunny'),
    path('add/', views.add_bunny, name='add_bunny'),
    # path('bunnies/change_bunny/', views.change_bunny, name='change_bunny'),
    path('bunnies/combine/', views.combine_bunny, name='combine_bunnies'), 
    path('sign_up/', views.sign_up, name='signup')    ]
