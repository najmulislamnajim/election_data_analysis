import pandas as pd 
import os
import numpy as np
from django.utils.text import slugify

def analyze_election_data():
    csv_path = os.path.join(os.path.dirname(__file__), './data/election_data.csv')
    # Load the CSV file
    df = pd.read_csv(csv_path)
    
    # Sort Data
    df = df.sort_values(by='total_voter')
    df['center_name'] = df['center_name'].apply(lambda x: ','.join(x.rsplit(',', 1)[:-1]) if ',' in x else x)
    
    # Calculate vote percentages
    df['our_vote_rate'] = np.where(df['total_legal_vote'] > 0, (df['7'] / df['total_legal_vote']) * 100, 0)
    df['opponent_vote_rate'] = np.where(df['total_legal_vote'] > 0, (df['2'] / df['total_legal_vote']) * 100, 0)
    
    df['our_vote_rate'] = df['our_vote_rate'].round(2)
    df['opponent_vote_rate'] = df['opponent_vote_rate'].round(2)

    # Strongest center >= 80% vote cast
    our_strongest_centers = df[df['our_vote_rate'] >= 80][['id', 'center_name', 'our_vote_rate','opponent_vote_rate', '7', '2', 'total_voter', 'total_legal_vote']]
    opponent_strongest_centers = df[df['opponent_vote_rate'] >= 80][['id', 'center_name', 'our_vote_rate','opponent_vote_rate', '7', '2', 'total_voter', 'total_legal_vote']]
    
    # strong center >= 60% and < 80% vote cast
    our_strong_centers = df[(df['our_vote_rate'] >= 60) & (df['our_vote_rate'] < 80)][['id', 'center_name', 'our_vote_rate', 'opponent_vote_rate', '7', '2', 'total_voter', 'total_legal_vote']]
    opponent_strong_centers = df[(df['opponent_vote_rate'] >= 60) & (df['opponent_vote_rate'] < 80)][['id', 'center_name', 'our_vote_rate', 'opponent_vote_rate', '7', '2', 'total_voter', 'total_legal_vote']]
    
    # critical center >= 50% and < 59% vote cast
    our_critical_centers = df[(df['our_vote_rate'] >= 50) & (df['our_vote_rate'] < 59)][['id', 'center_name', 'our_vote_rate', 'opponent_vote_rate', '7', '2', 'total_voter', 'total_legal_vote']]
    opponent_critical_centers = df[(df['opponent_vote_rate'] >= 50) & (df['opponent_vote_rate'] < 59)][['id', 'center_name', 'our_vote_rate', 'opponent_vote_rate', '7', '2', 'total_voter', 'total_legal_vote']]
    
    # competitive center >= 40% and < 49% vote cast
    our_competitive_centers = df[(df['our_vote_rate'] >= 40) & (df['our_vote_rate'] < 49)][['id', 'center_name', 'our_vote_rate', 'opponent_vote_rate', '7', '2', 'total_voter', 'total_legal_vote']]
    opponent_competitive_centers = df[(df['opponent_vote_rate'] >= 40) & (df['opponent_vote_rate'] < 49)][['id', 'center_name', 'our_vote_rate', 'opponent_vote_rate', '7', '2', 'total_voter', 'total_legal_vote']]
    
    # Struggling center >= 20% and < 39% vote cast
    our_struggling_centers = df[(df['our_vote_rate'] >= 20) & (df['our_vote_rate'] < 39)][['id', 'center_name', 'our_vote_rate', 'opponent_vote_rate', '7', '2', 'total_voter', 'total_legal_vote']]
    opponent_struggling_centers = df[(df['opponent_vote_rate'] >= 20) & (df['opponent_vote_rate'] < 39)][['id', 'center_name', 'our_vote_rate', 'opponent_vote_rate', '7', '2', 'total_voter', 'total_legal_vote']]
    
    # Underperforming center  < 20% vote cast
    our_underperforming_centers = df[df['our_vote_rate'] < 20][['id', 'center_name', 'our_vote_rate', 'opponent_vote_rate', '7', '2', 'total_voter', 'total_legal_vote']]
    opponent_underperforming_centers = df[df['opponent_vote_rate'] < 20][['id', 'center_name', 'our_vote_rate', 'opponent_vote_rate', '7', '2', 'total_voter', 'total_legal_vote']]
    
    # Winning Centers
    our_winning_centers = df[df['7'] > df['2']][['id', 'center_name', 'our_vote_rate', 'opponent_vote_rate','7', '2', 'total_voter', 'total_legal_vote']]
    opponent_winning_centers = df[df['2'] > df['7']][['id', 'center_name', 'our_vote_rate', 'opponent_vote_rate', '7', '2', 'total_voter', 'total_legal_vote']]
    
    # Losing Centers
    our_losing_centers = df[df['7'] < df['2']][['id', 'center_name', 'our_vote_rate', 'opponent_vote_rate', '7', '2', 'total_voter', 'total_legal_vote']]
    opponent_losing_centers = df[df['2'] < df['7']][['id', 'center_name', 'our_vote_rate', 'opponent_vote_rate','7', '2', 'total_voter', 'total_legal_vote']]
    
    total_voters = df['total_voter'].sum()
    total_legal_votes = df['total_legal_vote'].sum()
    total_cancelled_votes = df['total_cancelled_vote'].sum()
    total_votes = df['total_vote'].sum()
    total_vote_rate = df['total_vote_rate'].sum()
    our_casted_votes = df['7'].sum()
    opponent_casted_votes = df['2'].sum()
    total_centers = df['id'].count()
    our_total_winning_centers =our_winning_centers['id'].count()
    opponent_total_winning_centers = opponent_winning_centers['id'].count()
    our_total_losing_centers = our_losing_centers['id'].count()
    opponent_total_losing_centers = opponent_losing_centers['id'].count()
    
    data ={
        'our_strong_centers': our_strong_centers.to_dict(orient='records'),
        'opponent_strong_centers': opponent_strong_centers.to_dict(orient='records'),
        'our_strongest_centers': our_strongest_centers.to_dict(orient='records'),
        'opponent_strongest_centers': opponent_strongest_centers.to_dict(orient='records'),
        'our_critical_centers': our_critical_centers.to_dict(orient='records'),
        'opponent_critical_centers': opponent_critical_centers.to_dict(orient='records'),
        'our_competitive_centers': our_competitive_centers.to_dict(orient='records'),
        'opponent_competitive_centers': opponent_competitive_centers.to_dict(orient='records'),
        'our_struggling_centers': our_struggling_centers.to_dict(orient='records'),
        'opponent_struggling_centers': opponent_struggling_centers.to_dict(orient='records'),
        'our_underperforming_centers': our_underperforming_centers.to_dict(orient='records'),
        'opponent_underperforming_centers': opponent_underperforming_centers.to_dict(orient='records'),
        'our_winning_centers': our_winning_centers.to_dict(orient='records'),
        'opponent_winning_centers': opponent_winning_centers.to_dict(orient='records'),
        'our_losing_centers': our_losing_centers.to_dict(orient='records'),
        'opponent_losing_centers': opponent_losing_centers.to_dict(orient='records'),
        'total_centers': total_centers,
        'winning_centers': our_total_winning_centers,
        'losing_centers': our_total_losing_centers,
        'total_voters': total_voters,
        'total_legal_votes': total_legal_votes,
        'total_cancelled_votes': total_cancelled_votes,
        'total_votes': total_votes,
        'total_vote_rate': total_vote_rate,
        'our_casted_votes': our_casted_votes,
        'opponent_casted_votes': opponent_casted_votes,
    }
    return data



def upazila_analysis():
    election_data = pd.read_csv(os.path.join(os.path.dirname(__file__), './data/election_data.csv'))
    center_data = pd.read_csv(os.path.join(os.path.dirname(__file__), './data/center_details.csv'))
    df = election_data.merge(center_data, on='id')
    
    # Calculate vote percentages
    df['our_vote_rate'] = np.where(df['total_legal_vote'] > 0, (df['7'] / df['total_legal_vote']) * 100, 0)
    df['opponent_vote_rate'] = np.where(df['total_legal_vote'] > 0, (df['2'] / df['total_legal_vote']) * 100, 0)
    df['our_vote_rate'] = df['our_vote_rate'].round(2)
    df['opponent_vote_rate'] = df['opponent_vote_rate'].round(2)
    
    upazila_group = df.groupby('upazila')
    upazila = dict()
    for name, entries in upazila_group:
        total_centers = len(entries)
        winning_centers= entries[entries['7'] > entries['2']].reset_index(drop=True)
        losing_centers = entries[entries['7'] < entries['2']].reset_index(drop=True)
        opponent_winning_centers= entries[entries['7'] < entries['2']].reset_index(drop=True)
        opponent_losing_centers = entries[entries['7'] > entries['2']].reset_index(drop=True)
        winning_count = len(winning_centers)
        losing_count = len(losing_centers)
        winning_percentage = (len(winning_centers) / total_centers) * 100
        losing_percentage = (len(losing_centers) / total_centers) * 100
        total_voters = entries['total_voter'].sum()
        total_votes = entries['total_legal_vote'].sum()
        our_votes = entries['7'].sum()
        opponent_votes = entries['2'].sum()
        cancelled_votes = entries['total_cancelled_vote'].sum()
        key = slugify(name.lower())
        data = {
            'name': name,
            'total_centers' : entries.to_dict(orient='records'),
            'winning_centers': winning_centers.to_dict(orient='records'),
            'losing_centers': losing_centers.to_dict(orient='records'),
            'opponent_winning_centers': opponent_winning_centers.to_dict(orient='records'),
            'opponent_losing_centers': opponent_losing_centers.to_dict(orient='records'),
            'total_center_count': total_centers,
            'winning_center_count': winning_count,
            'losing_center_count': losing_count,
            'winning_percentage': winning_percentage,
            'losing_percentage': losing_percentage,
            'total_voters': total_voters,
            'total_votes': total_votes,
            'our_casted_votes': our_votes,
            'opponent_casted_votes': opponent_votes,
            'total_cancelled_votes': cancelled_votes,
        }
        upazila[key] = data
    return upazila

def union_analysis():
    election_data = pd.read_csv(os.path.join(os.path.dirname(__file__), './data/election_data.csv'))
    center_data = pd.read_csv(os.path.join(os.path.dirname(__file__), './data/center_details.csv'))
    df = election_data.merge(center_data, on='id')
    
    # Calculate vote percentages
    df['our_vote_rate'] = np.where(df['total_legal_vote'] > 0, (df['7'] / df['total_legal_vote']) * 100, 0)
    df['opponent_vote_rate'] = np.where(df['total_legal_vote'] > 0, (df['2'] / df['total_legal_vote']) * 100, 0)
    df['our_vote_rate'] = df['our_vote_rate'].round(2)
    df['opponent_vote_rate'] = df['opponent_vote_rate'].round(2)
    
    union_group = df.groupby('union')
    union = dict()
    for name, entries in union_group:
        total_centers = len(entries)
        winning_centers= entries[entries['7'] > entries['2']].reset_index(drop=True)
        losing_centers = entries[entries['7'] < entries['2']].reset_index(drop=True)
        opponent_winning_centers= entries[entries['7'] < entries['2']].reset_index(drop=True)
        opponent_losing_centers = entries[entries['7'] > entries['2']].reset_index(drop=True)
        winning_count = len(winning_centers)
        losing_count = len(losing_centers)
        winning_percentage = (len(winning_centers) / total_centers) * 100
        losing_percentage = (len(losing_centers) / total_centers) * 100
        total_voters = entries['total_voter'].sum()
        total_votes = entries['total_legal_vote'].sum()
        our_votes = entries['7'].sum()
        opponent_votes = entries['2'].sum()
        cancelled_votes = entries['total_cancelled_vote'].sum()
        key = slugify(name.lower())
        data = {
            'name': name,
            'total_centers' : entries.to_dict(orient='records'),
            'winning_centers': winning_centers.to_dict(orient='records'),
            'losing_centers': losing_centers.to_dict(orient='records'),
            'opponent_winning_centers': opponent_winning_centers.to_dict(orient='records'),
            'opponent_losing_centers': opponent_losing_centers.to_dict(orient='records'),
            'total_center_count': total_centers,
            'winning_center_count': winning_count,
            'losing_center_count': losing_count,
            'winning_percentage': winning_percentage,
            'losing_percentage': losing_percentage,
            'total_voters': total_voters,
            'total_votes': total_votes,
            'our_casted_votes': our_votes,
            'opponent_casted_votes': opponent_votes,
            'total_cancelled_votes': cancelled_votes,
        }
        union[key] = data
    return union


def union_analysis_2():
    election_data = pd.read_csv(os.path.join(os.path.dirname(__file__), './data/election_data.csv'))
    center_data = pd.read_csv(os.path.join(os.path.dirname(__file__), './data/center_details.csv'))
    df = election_data.merge(center_data, on='id')
    
    # Calculate vote percentages
    df['our_vote_rate'] = np.where(df['total_legal_vote'] > 0, (df['7'] / df['total_legal_vote']) * 100, 0)
    df['opponent_vote_rate'] = np.where(df['total_legal_vote'] > 0, (df['2'] / df['total_legal_vote']) * 100, 0)
    df['our_vote_rate'] = df['our_vote_rate'].round(2)
    df['opponent_vote_rate'] = df['opponent_vote_rate'].round(2)
    
    # Group by upazila first, then by union
    upazila_group = df.groupby('upazila')
    upazila_data = dict()
    
    for upazila_name, upazila_entries in upazila_group:
        union_group = upazila_entries.groupby('union')
        unions = dict()
        
        for union_name, entries in union_group:
            total_centers = len(entries)
            winning_centers = entries[entries['7'] > entries['2']].reset_index(drop=True)
            losing_centers = entries[entries['7'] < entries['2']].reset_index(drop=True)
            opponent_winning_centers = losing_centers
            opponent_losing_centers = winning_centers
            winning_count = len(winning_centers)
            losing_count = len(losing_centers)
            winning_percentage = (winning_count / total_centers) * 100 if total_centers > 0 else 0
            losing_percentage = (losing_count / total_centers) * 100 if total_centers > 0 else 0
            total_voters = entries['total_voter'].sum()
            total_votes = entries['total_legal_vote'].sum()
            our_votes = entries['7'].sum()
            opponent_votes = entries['2'].sum()
            cancelled_votes = entries['total_cancelled_vote'].sum()
            key = slugify(union_name.lower())
            data = {
                'name': union_name,
                'total_centers': entries.to_dict(orient='records'),
                'winning_centers': winning_centers.to_dict(orient='records'),
                'losing_centers': losing_centers.to_dict(orient='records'),
                'opponent_winning_centers': opponent_winning_centers.to_dict(orient='records'),
                'opponent_losing_centers': opponent_losing_centers.to_dict(orient='records'),
                'total_center_count': total_centers,
                'winning_center_count': winning_count,
                'losing_center_count': losing_count,
                'winning_percentage': winning_percentage,
                'losing_percentage': losing_percentage,
                'total_voters': total_voters,
                'total_votes': total_votes,
                'our_casted_votes': our_votes,
                'opponent_casted_votes': opponent_votes,
                'total_cancelled_votes': cancelled_votes,
            }
            unions[key] = data
        
        upazila_data[slugify(upazila_name.lower())] = {
            'name': upazila_name,
            'unions': unions
        }
    
    return upazila_data


def upazila_wise_union():
    election_data = pd.read_csv(os.path.join(os.path.dirname(__file__), './data/election_data.csv'))
    center_data = pd.read_csv(os.path.join(os.path.dirname(__file__), './data/center_details.csv'))
    df = election_data.merge(center_data, on='id')

    # Calculate vote percentages
    df['our_vote_rate'] = np.where(df['total_legal_vote'] > 0, (df['7'] / df['total_legal_vote']) * 100, 0).round(2)
    df['opponent_vote_rate'] = np.where(df['total_legal_vote'] > 0, (df['2'] / df['total_legal_vote']) * 100, 0).round(2)

    # Build nested dict: {upazila -> {union -> [center rows as dict]}}
    nested_data = {}
    for _, row in df.iterrows():
        upazila = row['upazila']
        union = row['union']
        center_info = {
            'center_name': row['center_name'],
            'total_voter': row['total_voter'],
            'total_legal_vote': row['total_legal_vote'],
            'our_vote': row['7'],
            'opponent_vote': row['2'],
            'our_vote_rate': row['our_vote_rate'],
            'opponent_vote_rate': row['opponent_vote_rate'],
            'status': 'win' if row['our_vote_rate'] > row['opponent_vote_rate'] else 'lose'
        }

        nested_data.setdefault(upazila, {}).setdefault(union, []).append(center_info)

    return nested_data

def get_upazila_union_summary():
    election_data = pd.read_csv(os.path.join(os.path.dirname(__file__), './data/election_data.csv'))
    center_data = pd.read_csv(os.path.join(os.path.dirname(__file__), './data/center_details.csv'))
    df = election_data.merge(center_data, on='id')

    df['our_vote_rate'] = np.where(df['total_legal_vote'] > 0, (df['7'] / df['total_legal_vote']) * 100, 0).round(2)
    df['opponent_vote_rate'] = np.where(df['total_legal_vote'] > 0, (df['2'] / df['total_legal_vote']) * 100, 0).round(2)

    summary = {}

    grouped = df.groupby(['upazila', 'union'])
    for (upazila, union), group in grouped:
        total_voter = group['total_voter'].sum()
        total_legal_vote = group['total_legal_vote'].sum()
        our_vote = group['7'].sum()
        opponent_vote = group['2'].sum()

        our_vote_rate = round((our_vote / total_legal_vote) * 100, 2) if total_legal_vote > 0 else 0
        opponent_vote_rate = round((opponent_vote / total_legal_vote) * 100, 2) if total_legal_vote > 0 else 0
        status = 'win' if our_vote_rate > opponent_vote_rate else 'lose'

        union_data = {
            'total_voter': total_voter,
            'total_legal_vote': total_legal_vote,
            'our_vote': our_vote,
            'opponent_vote': opponent_vote,
            'our_vote_rate': our_vote_rate,
            'opponent_vote_rate': opponent_vote_rate,
            'status': status
        }

        summary.setdefault(upazila, {})[union] = union_data

    return summary
