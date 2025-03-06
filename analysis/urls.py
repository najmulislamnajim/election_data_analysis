from django.urls import path,include
from . import views

urlpatterns = [
    path('our_strong_centers',views.plot_vote_rates),
]
