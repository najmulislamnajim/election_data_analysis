import pandas as pd
import matplotlib.pyplot as plt
import os

def analyze_election_data(csv_path):
    # Load the CSV file
    df = pd.read_csv(csv_path)

    # Rename columns for clarity
    df.columns = ['id', 'center_name', 'total_voter', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', 
                  'total_legal_vote', 'total_cancelled_vote', 'total_vote', 'total_vote_rate']

    # Calculate vote percentages
    df['our_votes'] = df['7']  # Our candidate (ID 7)
    df['opponent_votes'] = df['2']  # Main opponent (ID 2)
    df['our_percentage'] = (df['our_votes'] / df['total_legal_vote']) * 100
    df['opponent_percentage'] = (df['opponent_votes'] / df['total_legal_vote']) * 100

    # Filter strongest centers (≥ 80%)
    our_strong_centers = df[df['our_percentage'] >= 80][['id', 'center_name', 'our_votes', 'total_legal_vote', 'our_percentage']]
    opponent_strong_centers = df[df['opponent_percentage'] >= 80][['id', 'center_name', 'opponent_votes', 'total_legal_vote', 'opponent_percentage']]

    # Sort by percentage
    our_strong_centers = our_strong_centers.sort_values(by='our_percentage', ascending=False)
    opponent_strong_centers = opponent_strong_centers.sort_values(by='opponent_percentage', ascending=False)

    return our_strong_centers, opponent_strong_centers

def plot_strong_centers(our_strong_centers, opponent_strong_centers, output_path):
    plt.figure(figsize=(12, 6))

    # Plot our strong centers
    if not our_strong_centers.empty:
        plt.bar(our_strong_centers['center_name'], our_strong_centers['our_percentage'], 
                color='blue', label='Our Candidate (7)', alpha=0.7)

    # Plot opponent's strong centers
    if not opponent_strong_centers.empty:
        plt.bar(opponent_strong_centers['center_name'], opponent_strong_centers['opponent_percentage'], 
                color='red', label='Opponent (2)', alpha=0.7)

    plt.axhline(y=80, color='black', linestyle='--', label='80% Threshold')
    plt.title('Strongest Vote Centers (≥ 80%) for Candidate 7 and Candidate 2')
    plt.xlabel('Vote Center')
    plt.ylabel('Vote Percentage (%)')
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

if __name__ == "__main__":
    # For testing standalone
    csv_path = os.path.join(os.path.dirname(__file__), '../data/main_data.csv')
    our_strong, opponent_strong = analyze_election_data(csv_path)
    print("Our Strong Centers:\n", our_strong)
    print("\nOpponent Strong Centers:\n", opponent_strong)
    plot_strong_centers(our_strong, opponent_strong, os.path.join(os.path.dirname(__file__), '../images/combined_strong_centers.png'))