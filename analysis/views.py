from django.shortcuts import render
from .utils import analyze_election_data

def plot_vote_rates(request):
    data = analyze_election_data()
    # Pass the data to the template
    return render(request, 'test.html', {'data':data})



def home(request):
    data = analyze_election_data()
    context = {
        'categories': [
            {'name': 'Winning Centers', 'range': 'More than opponent percentage', 'url_name': 'winning_centers_by_percentage', 'count': len(data['our_winning_centers'])},
            {'name': 'Losing Centers', 'range': 'Less than opponent percentage', 'url_name': 'losing_centers_by_percentage', 'count': len(data['our_losing_centers'])},
            {'name': 'Dominant Centers', 'range': '80% or Higher', 'url_name': 'strongest_centers', 'count': len(data['our_strongest_centers'])},
            {'name': 'Solid Centers', 'range': '60% to 79%', 'url_name': 'strong_centers', 'count': len(data['our_strong_centers'])},
            {'name': 'Critical Centers', 'range': '50% to 59%', 'url_name': 'critical_centers', 'count': len(data['our_critical_centers'])},
            {'name': 'Contested Centers', 'range': '40% to 49%', 'url_name': 'competitive_centers', 'count': len(data['our_competitive_centers'])},
            {'name': 'Struggling Centers', 'range': '20% to 39%', 'url_name': 'weak_centers', 'count': len(data['our_struggling_centers'])},
            {'name': 'Underperforming Centers', 'range': 'Below 20%', 'url_name': 'very_weak_centers', 'count': len(data['our_underperforming_centers'])},
            
        ]
    }
    return render(request, 'home.html', context)

def center_detail(request):
    data = analyze_election_data()
    category = request.path.split('/')[-2]  # Extracts 'dominant', 'solid', etc.

    category_map = {
        'dominant': ('Dominant Centers (80% or Higher)', data['our_strongest_centers'], data['opponent_strongest_centers']),
        'solid': ('Solid Centers (60% to 79%)', data['our_strong_centers'], data['opponent_strong_centers']),
        'critical': ('Critical Centers (50% to 59%)', data['our_critical_centers'], data['opponent_critical_centers']),
        'contested': ('Contested Centers (40% to 49%)', data['our_competitive_centers'], data['opponent_competitive_centers']),
        'struggling': ('Struggling Centers (20% to 39%)', data['our_struggling_centers'], data['opponent_struggling_centers']),
        'underperforming': ('Underperforming Centers (Below 20%)', data['our_underperforming_centers'], data['opponent_underperforming_centers']),
        'winning_by_percentage': ('Winning Centers (More than opponent percentage)', data['our_winning_centers'], data['opponent_winning_centers']),
        'losing_by_percentage': ('Losing Centers (Less than opponent percentage)', data['our_losing_centers'], data['opponent_losing_centers']),
    }

    title, our_centers, opponent_centers = category_map.get(category, ('Unknown Category', [], []))
    category_name = title.split(' (')[0]  # Extracts 'Dominant Centers', 'Solid Centers', etc.
    
    context = {
        'title': title,
        'category_name': category_name,
        'our_centers': our_centers,
        'opponent_centers': opponent_centers,
        'centers': our_centers,  # For initial count
    }
    return render(request, 'center_detail.html', context)