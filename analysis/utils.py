import pandas as pd 
import os
import numpy as np

def analyze_election_data():
    csv_path = os.path.join(os.path.dirname(__file__), './data/election_data.csv')
    # Load the CSV file
    df = pd.read_csv(csv_path)
    
    # Sort Data
    df = df.sort_values(by='total_voter')
    
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


