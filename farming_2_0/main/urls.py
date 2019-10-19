from django.urls import path

from . import views

urlpatterns = [
    path('crops/', views.GetCrops, name='GetCrops'),
    path('stages/<str:crop_id>/', views.GetStages, name='GetStages'),
    path('machines/<str:stage_id>/', views.GetMachines, name='GetMachines')
]
