import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

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

    # Filter strongest centers (≥ 80% for either candidate)
    strong_centers = df[(df['our_percentage'] >= 80) | (df['opponent_percentage'] >= 80)][
        ['id', 'center_name', 'our_votes', 'opponent_votes', 'total_legal_vote', 'our_percentage', 'opponent_percentage']
    ]

    # Sort by our percentage (descending), then opponent percentage
    strong_centers = strong_centers.sort_values(by=['our_percentage', 'opponent_percentage'], ascending=False)

    return strong_centers

def plot_strong_centers(strong_centers, output_path):
    if strong_centers.empty:
        # Create a blank image if no data
        plt.figure(figsize=(12, 6))
        plt.text(0.5, 0.5, 'No centers with ≥ 80% for either candidate', 
                 horizontalalignment='center', verticalalignment='center')
        plt.axis('off')
        plt.savefig(output_path)
        plt.close()
        return

    plt.figure(figsize=(12, 6))

    # Data for plotting
    centers = strong_centers['id']
    our_percentages = strong_centers['our_percentage']
    opponent_percentages = strong_centers['opponent_percentage']

    # Bar positions
    bar_width = 0.35
    r1 = np.arange(len(centers))  # Positions for our bars
    r2 = [x + bar_width for x in r1]  # Positions for opponent bars

    # Plot bars
    plt.bar(r1, our_percentages, color='blue', width=bar_width, label='Our Candidate (7)')
    plt.bar(r2, opponent_percentages, color='red', width=bar_width, label='Opponent (2)')

    # Customize plot
    plt.axhline(y=80, color='black', linestyle='--', label='80% Threshold')
    plt.xlabel('Vote Center')
    plt.ylabel('Vote Percentage (%)')
    plt.title('Strongest Vote Centers (≥ 80% for Either Candidate)')
    plt.xticks([r + bar_width/2 for r in r1], centers, rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()

    # Save plot
    plt.savefig(output_path)
    plt.close()

if __name__ == "__main__":
    # For testing standalone
    csv_path = os.path.join(os.path.dirname(__file__), '../data/election_data.csv')
    strong_centers = analyze_election_data(csv_path)
    print("Strong Centers (≥ 80% for either candidate):\n", strong_centers)
    plot_strong_centers(strong_centers, os.path.join(os.path.dirname(__file__), '../images/combined_strong_centers.png'))