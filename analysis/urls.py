from django.urls import path,include
from . import views

urlpatterns = [
    path('strong_centers',views.plot_vote_rates,name='strong_centers'),
    path('centers/dominant_rate/', views.center_detail, name='strongest_centers_rate'),
    path('centers/solid_rate/', views.center_detail, name='strong_centers_rate'),
    path('centers/critical_rate/', views.center_detail, name='critical_centers_rate'),
    path('centers/contested_rate/', views.center_detail, name='competitive_centers_rate'),
    path('centers/struggling_rate/', views.center_detail, name='weak_centers_rate'),
    path('centers/underperforming_rate/', views.center_detail, name='very_weak_centers_rate'),
    path('centers/winning_rate/', views.center_detail, name='winning_centers_rate'),
    path('centers/losing_rate/', views.center_detail, name='losing_centers_rate'),
    
    path('centers/dominant_count/', views.center_detail_count, name='strongest_centers_count'),
    path('centers/solid_count/', views.center_detail_count, name='strong_centers_count'),
    path('centers/critical_count/', views.center_detail_count, name='critical_centers_count'),
    path('centers/contested_count/', views.center_detail_count, name='competitive_centers_count'),
    path('centers/struggling_count/', views.center_detail_count, name='weak_centers_count'),
    path('centers/underperforming_count/', views.center_detail_count, name='very_weak_centers_count'),
    path('centers/winning_count/', views.center_detail_count, name='winning_centers_count'),
    path('centers/losing_count/', views.center_detail_count, name='losing_centers_count'),
]
