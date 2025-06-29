from django.shortcuts import render
from django.utils.text import slugify
from .utils import analyze_election_data, upazila_analysis, union_analysis, union_analysis_2
import json

def plot_vote_rates(request):
    data = analyze_election_data()
    # Pass the data to the template
    return render(request, 'test.html', {'data':data})



def home(request):
    data = analyze_election_data()
    context = {
        'rate_categories': [
            {'name': 'Winning Centers', 'range': 'More than opponent percentage', 'url_name': 'winning_centers_rate', 'count': len(data['our_winning_centers'])},
            {'name': 'Losing Centers', 'range': 'Less than opponent percentage', 'url_name': 'losing_centers_rate', 'count': len(data['our_losing_centers'])},
            {'name': 'Dominant Centers', 'range': '80% or Higher', 'url_name': 'strongest_centers_rate', 'count': len(data['our_strongest_centers'])},
            {'name': 'Solid Centers', 'range': '60% to 79%', 'url_name': 'strong_centers_rate', 'count': len(data['our_strong_centers'])},
            {'name': 'Critical Centers', 'range': '50% to 59%', 'url_name': 'critical_centers_rate', 'count': len(data['our_critical_centers'])},
            {'name': 'Contested Centers', 'range': '40% to 49%', 'url_name': 'competitive_centers_rate', 'count': len(data['our_competitive_centers'])},
            {'name': 'Struggling Centers', 'range': '20% to 39%', 'url_name': 'weak_centers_rate', 'count': len(data['our_struggling_centers'])},
            {'name': 'Underperforming Centers', 'range': 'Below 20%', 'url_name': 'very_weak_centers_rate', 'count': len(data['our_underperforming_centers'])},   
        ],
        'count_categories': [
            {'name': 'Winning Centers', 'range': 'More than opponent percentage', 'url_name': 'winning_centers_count', 'count': len(data['our_winning_centers'])},
            {'name': 'Losing Centers', 'range': 'Less than opponent percentage', 'url_name': 'losing_centers_count', 'count': len(data['our_losing_centers'])},
            {'name': 'Dominant Centers', 'range': '80% or Higher', 'url_name': 'strongest_centers_count', 'count': len(data['our_strongest_centers'])},
            {'name': 'Solid Centers', 'range': '60% to 79%', 'url_name': 'strong_centers_count', 'count': len(data['our_strong_centers'])},
            {'name': 'Critical Centers', 'range': '50% to 59%', 'url_name': 'critical_centers_count', 'count': len(data['our_critical_centers'])},
            {'name': 'Contested Centers', 'range': '40% to 49%', 'url_name': 'competitive_centers_count', 'count': len(data['our_competitive_centers'])},
            {'name': 'Struggling Centers', 'range': '20% to 39%', 'url_name': 'weak_centers_count', 'count': len(data['our_struggling_centers'])},
            {'name': 'Underperforming Centers', 'range': 'Below 20%', 'url_name': 'very_weak_centers_count', 'count': len(data['our_underperforming_centers'])},   
        ],
        'total_centers': data['total_centers'],
        'winning_centers': data['winning_centers'],
        'losing_centers': data['losing_centers'],
        'total_voters': data['total_voters'],
        'total_legal_votes': data['total_legal_votes'],
        'total_cancelled_votes': data['total_cancelled_votes'],
        'total_votes': data['total_votes'],
        'total_vote_rate': data['total_vote_rate'],
        'our_casted_votes': data['our_casted_votes'],
        'opponent_casted_votes': data['opponent_casted_votes'],
    }
    return render(request, 'home.html', context)

def center_detail(request):
    data = analyze_election_data()
    category = request.path.split('/')[-2]  # Extracts 'dominant', 'solid', etc.

    category_map = {
        'dominant_rate': ('Dominant Centers (80% or Higher)', data['our_strongest_centers'], data['opponent_strongest_centers']),
        'solid_rate': ('Solid Centers (60% to 79%)', data['our_strong_centers'], data['opponent_strong_centers']),
        'critical_rate': ('Critical Centers (50% to 59%)', data['our_critical_centers'], data['opponent_critical_centers']),
        'contested_rate': ('Contested Centers (40% to 49%)', data['our_competitive_centers'], data['opponent_competitive_centers']),
        'struggling_rate': ('Struggling Centers (20% to 39%)', data['our_struggling_centers'], data['opponent_struggling_centers']),
        'underperforming_rate': ('Underperforming Centers (Below 20%)', data['our_underperforming_centers'], data['opponent_underperforming_centers']),
        'winning_rate': ('Winning Centers (More than opponent percentage)', data['our_winning_centers'], data['opponent_winning_centers']),
        'losing_rate': ('Losing Centers (Less than opponent percentage)', data['our_losing_centers'], data['opponent_losing_centers']),
    }

    title, our_centers, opponent_centers = category_map.get(category, ('Unknown Category', [], []))
    category_name = title.split(' (')[0]  # Extracts 'Dominant Centers', 'Solid Centers', etc.
    
    context = {
        'title': title,
        'category_name': category_name,
        'our_centers': our_centers,
        'opponent_centers': opponent_centers,
        'centers': our_centers,
        'home_url': 'home',
        'home_url_text': 'Back to Home',
    }
    return render(request, 'center_detail.html', context)

def center_detail_count(request):
    data = analyze_election_data()
    category = request.path.split('/')[-2]  # Extracts 'dominant', 'solid', etc.

    category_map = {
        'dominant_count': ('Dominant Centers (80% or Higher)', data['our_strongest_centers'], data['opponent_strongest_centers']),
        'solid_count': ('Solid Centers (60% to 79%)', data['our_strong_centers'], data['opponent_strong_centers']),
        'critical_count': ('Critical Centers (50% to 59%)', data['our_critical_centers'], data['opponent_critical_centers']),
        'contested_count': ('Contested Centers (40% to 49%)', data['our_competitive_centers'], data['opponent_competitive_centers']),
        'struggling_count': ('Struggling Centers (20% to 39%)', data['our_struggling_centers'], data['opponent_struggling_centers']),
        'underperforming_count': ('Underperforming Centers (Below 20%)', data['our_underperforming_centers'], data['opponent_underperforming_centers']),
        'winning_count': ('Winning Centers (More than opponent percentage)', data['our_winning_centers'], data['opponent_winning_centers']),
        'losing_count': ('Losing Centers (Less than opponent percentage)', data['our_losing_centers'], data['opponent_losing_centers']),
    }

    title, our_centers, opponent_centers = category_map.get(category, ('Unknown Category', [], []))
    category_name = title.split(' (')[0]  # Extracts 'Dominant Centers', 'Solid Centers', etc.
    
    context = {
        'title': title,
        'category_name': category_name,
        'our_centers': our_centers,
        'opponent_centers': opponent_centers,
        'centers': our_centers,
        'home_url': 'home',
        'home_url_text': 'Back to Home',
    }
    return render(request, 'center_details_count.html', context)


def upazila_analysis_view(request):
    data = upazila_analysis()
    upazila_data = list(data.values())
    for u in upazila_data:
        u['total_center_count'] = int(u['total_center_count'])
        u['winning_center_count'] = int(u['winning_center_count'])
        u['losing_center_count'] = int(u['losing_center_count'])
        u['winning_percentage'] = float(u['winning_percentage'])
        u['losing_percentage'] = float(u['losing_percentage'])
        u['total_voters'] = int(u['total_voters'])
        u['total_votes'] = int(u['total_votes'])
        u['our_casted_votes'] = int(u['our_casted_votes'])
        u['opponent_casted_votes'] = int(u['opponent_casted_votes'])
        u['total_cancelled_votes'] = int(u['total_cancelled_votes'])
    
    final_data = [upazila_data[1], upazila_data[0]]

    context = {
        'upazilas': final_data,
        'upazilas_json': json.dumps(final_data)
    }
    return render(request, 'upazila.html', context)

def upazila_winning_details_rate(request, upazila_name=None):
    upazila_data = upazila_analysis()
    data = upazila_data[upazila_name]
    context = {
        'title': f'Winning Center ({data["name"]})',
        'category_name': 'Winning Centers',
        'our_centers': data['winning_centers'],
        'opponent_centers': data['opponent_winning_centers'],
        'centers': data['winning_centers'],
        'home_url':'upazila_analysis',
        'home_url_text': 'Back to Upazila Analysis'
    }
    return render(request, 'center_detail.html', context)

def upazila_losing_details_rate(request, upazila_name=None):
    upazila_data = upazila_analysis()
    data = upazila_data[upazila_name]
    context = {
        'title': f'Losing Center ({data["name"]})',
        'category_name': 'Losing Centers',
        'our_centers': data['losing_centers'],
        'opponent_centers': data['opponent_losing_centers'],
        'centers': data['losing_centers'],
        'home_url':'upazila_analysis',
        'home_url_text': 'Back to Upazila Analysis'
    }
    return render(request, 'center_detail.html', context)

def upazila_winning_details_count(request, upazila_name=None):
    upazila_data = upazila_analysis()
    data = upazila_data[upazila_name]
    context = {
        'title': f'Winning Center ({data["name"]})',
        'category_name': 'Winning Centers',
        'our_centers': data['winning_centers'],
        'opponent_centers': data['opponent_winning_centers'],
        'centers': data['winning_centers'],
        'home_url':'upazila_analysis',
        'home_url_text': 'Back to Upazila Analysis'
    }
    return render(request, 'center_details_count.html', context)

def upazila_losing_details_count(request, upazila_name=None):
    upazila_data = upazila_analysis()
    data = upazila_data[upazila_name]
    context = {
        'title': f'Losing Center ({data["name"]})',
        'category_name': 'Losing Centers',
        'our_centers': data['losing_centers'],
        'opponent_centers': data['opponent_losing_centers'],
        'centers': data['losing_centers'],
        'home_url':'upazila_analysis',
        'home_url_text': 'Back to Upazila Analysis'
    }
    return render(request, 'center_details_count.html', context)


# def union_analysis_view(request):
#     data = union_analysis()
#     union_data = list(data.values())
#     for u in union_data:
#         u['total_center_count'] = int(u['total_center_count'])
#         u['winning_center_count'] = int(u['winning_center_count'])
#         u['losing_center_count'] = int(u['losing_center_count'])
#         u['winning_percentage'] = float(u['winning_percentage'])
#         u['losing_percentage'] = float(u['losing_percentage'])
#         u['total_voters'] = int(u['total_voters'])
#         u['total_votes'] = int(u['total_votes'])
#         u['our_casted_votes'] = int(u['our_casted_votes'])
#         u['opponent_casted_votes'] = int(u['opponent_casted_votes'])
#         u['total_cancelled_votes'] = int(u['total_cancelled_votes'])
    
#     final_data = union_data

#     context = {
#         'upazilas': final_data,
#         'upazilas_json': json.dumps(final_data)
#     }
#     return render(request, 'union_test.html', context)

def union_analysis_view(request):
    data = union_analysis_2()
    upazila_data = list(data.values())
    
    for upazila in upazila_data:
        for union in upazila['unions'].values():
            union['total_center_count'] = int(union['total_center_count'])
            union['winning_center_count'] = int(union['winning_center_count'])
            union['losing_center_count'] = int(union['losing_center_count'])
            union['winning_percentage'] = float(union['winning_percentage'])
            union['losing_percentage'] = float(union['losing_percentage'])
            union['total_voters'] = int(union['total_voters'])
            union['total_votes'] = int(union['total_votes'])
            union['our_casted_votes'] = int(union['our_casted_votes'])
            union['opponent_casted_votes'] = int(union['opponent_casted_votes'])
            union['total_cancelled_votes'] = int(union['total_cancelled_votes'])
    
    context = {
        'upazilas': upazila_data,
        'upazilas_json': json.dumps(upazila_data)
    }
    return render(request, 'union.html', context)

def union_winning_details_rate(request, upazila_name=None):
    union_data = union_analysis()
    data = union_data[upazila_name]
    context = {
        'title': f'Winning Center ({data["name"]})',
        'category_name': 'Winning Centers',
        'our_centers': data['winning_centers'],
        'opponent_centers': data['opponent_winning_centers'],
        'centers': data['winning_centers'],
        'home_url':'union_analysis',
        'home_url_text': 'Back to Union Analysis'
    }
    return render(request, 'center_detail.html', context)

def union_losing_details_rate(request, union_name=None):
    union_data = union_analysis()
    data = union_data[union_name]
    context = {
        'title': f'Losing Center ({data["name"]})',
        'category_name': 'Losing Centers',
        'our_centers': data['losing_centers'],
        'opponent_centers': data['opponent_losing_centers'],
        'centers': data['losing_centers'],
        'home_url':'union_analysis',
        'home_url_text': 'Back to Union Analysis'
    }
    return render(request, 'center_detail.html', context)

def union_winning_details_count(request, union_name=None):
    union_data = union_analysis()
    data = union_data[union_name]
    context = {
        'title': f'Winning Center ({data["name"]})',
        'category_name': 'Winning Centers',
        'our_centers': data['winning_centers'],
        'opponent_centers': data['opponent_winning_centers'],
        'centers': data['winning_centers'],
        'home_url':'union_analysis',
        'home_url_text': 'Back to Union Analysis',
        'union_name': union_name
    }
    return render(request, 'center_details_count.html', context)

def union_losing_details_count(request, union_name=None):
    union_data = union_analysis()
    data = union_data[union_name]
    context = {
        'title': f'Losing Center ({data["name"]})',
        'category_name': 'Losing Centers',
        'our_centers': data['losing_centers'],
        'opponent_centers': data['opponent_losing_centers'],
        'centers': data['losing_centers'],
        'home_url':'union_analysis',
        'home_url_text': 'Back to Union Analysis'
    }
    return render(request, 'center_details_count.html', context)