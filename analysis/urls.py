from django.urls import path,include
from . import views

urlpatterns = [
    path('strong_centers',views.plot_vote_rates,name='strong_centers'),
    path('centers/dominant/', views.center_detail, name='strongest_centers'),
    path('centers/solid/', views.center_detail, name='strong_centers'),
    path('centers/critical/', views.center_detail, name='critical_centers'),
    path('centers/contested/', views.center_detail, name='competitive_centers'),
    path('centers/struggling/', views.center_detail, name='weak_centers'),
    path('centers/underperforming/', views.center_detail, name='very_weak_centers'),
]
