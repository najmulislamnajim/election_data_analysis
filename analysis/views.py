from django.shortcuts import render
from .utils import analyze_election_data

def plot_vote_rates(request):
    data = analyze_election_data()
    # Pass the data to the template
    return render(request, 'test.html', {'data':data})


def home(request):
    return render(request, 'home.html')