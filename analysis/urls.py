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
    
    path('upazila', views.upazila_analysis_view, name='upazila_analysis'),
    path('u-winning/<str:upazila_name>/', views.upazila_winning_details_rate, name='upazila_winning_details_rate'),
    path('u-losing/<str:upazila_name>/', views.upazila_losing_details_rate, name='upazila_losing_details_rate'),
    path('u-winning-count/<str:upazila_name>/', views.upazila_winning_details_count, name='upazila_winning_details_count'),
    path('u-losing-count/<str:upazila_name>/', views.upazila_losing_details_count, name='upazila_losing_details_count'),
    
    path('union', views.union_analysis_view, name='union_analysis'),
    path('un-winning/<str:union_name>/', views.union_winning_details_rate, name='union_winning_detailnion'),
    path('un-losing/<str:union_name>/', views.union_losing_details_rate, name='union_losing_details_rate'),
    path('un-winning-count/<str:union_name>/', views.union_winning_details_count, name='union_winning_details_count'),
    path('un-losing-count/<str:union_name>/', views.union_losing_details_count, name='union_losing_details_count'),
    
    path('upazila_wise_union/', views.upazila_wise_union_view, name='upazila_wise_union'),
    path('union_list', views.summary_report, name='union_list'),
]
