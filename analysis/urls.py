from django.urls import path,include
from . import views

urlpatterns = [
    path('strong_centers',views.plot_vote_rates,name='strong_centers'),
]
