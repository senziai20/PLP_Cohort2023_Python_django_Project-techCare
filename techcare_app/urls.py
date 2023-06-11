from django .urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_us, name='about_us'),
    path('repair_requests/', views.repair_requests, name='repair_requests'),
    path('create_repair_request/', views.create_repair_request,
         name='create_repair_request'),
]