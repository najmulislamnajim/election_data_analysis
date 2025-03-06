import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os
import numpy as np

def analyze_election_data(csv_path):
    # Load the CSV file
    df = pd.read_csv(csv_path)
    # Rename columns for clarity
    # df.columns = ['id', 'center_name', 'total_voter', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', 'total_legal_vote', 'total_cancelled_vote', 'total_vote', 'total_vote_rate']
    
    # Calculate vote percentages
    df['our_vote_rate'] = np.where(df['total_legal_vote'] > 0, (df['7'] / df['total_legal_vote']) * 100, 0)
    df['opponent_vote_rate'] = np.where(df['total_legal_vote'] > 0, (df['2'] / df['total_legal_vote']) * 100, 0)
    
    df['our_vote_rate'] = df['our_vote_rate'].round(2)
    df['opponent_vote_rate'] = df['opponent_vote_rate'].round(2)

    
    our_strongest_centers = df[df['our_vote_rate'] >= 80][['id', 'center_name', 'our_vote_rate','opponent_vote_rate']]
    
    opponent_strongest_centers = df[df['opponent_vote_rate'] >= 80][['id', 'center_name', 'our_vote_rate','opponent_vote_rate']]
    
    # Select centers where the 'our_vote_rate' is between 60 and 80
    our_strong_centers = df[(df['our_vote_rate'] >= 60) & (df['our_vote_rate'] < 80)][['id', 'center_name', 'our_vote_rate', 'opponent_vote_rate']]

    # Select centers where the 'opponent_vote_rate' is between 60 and 80
    opponent_strong_centers = df[(df['opponent_vote_rate'] >= 60) & (df['opponent_vote_rate'] < 80)][['id', 'center_name', 'our_vote_rate', 'opponent_vote_rate']]

    
    # Select specific columns to save
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')  # Navigate to the 'data' folder
    os.makedirs(output_dir, exist_ok=True)  # Ensure the directory exists

    # Construct the full path for the file
    output_file_path = os.path.join(output_dir, 'vote_rates.csv')
    
    plot_vote_rates(our_strong_centers)
    print(our_strong_centers)

def plot_vote_rates(our_strong_centers):
    try:
        # Set Bengali font
        font_path = os.path.join(os.path.dirname(__file__), '../fonts/kalpurush.ttf')
        prop = fm.FontProperties(fname=font_path)
        
        # Set up the plot
        plt.figure(figsize=(12, 6))

        # Plot the bar chart
        bar_width = 0.35
        index = range(len(our_strong_centers))

        plt.bar(index, our_strong_centers['our_vote_rate'], bar_width, label='Our Vote Rate', color='b')
        plt.bar([i + bar_width for i in index], our_strong_centers['opponent_vote_rate'], bar_width, label='Opponent Vote Rate', color='r')

        # Set the x-axis labels (center names)
        plt.xticks([i + bar_width / 2 for i in index], our_strong_centers['center_name'],rotation=60, ha='right', fontproperties=prop)

        # Labeling the axes and the chart
        plt.xlabel('Voting Centers', fontproperties=prop)
        plt.ylabel('Vote Rates (%)', fontproperties=prop)
        plt.title('Vote Rates for Our and Opponent in Strong Centers', fontproperties=prop)

        # Display legend
        plt.legend()

        # Show the plot
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error: {e}")    
    
if __name__ == "__main__":
    # For testing standalone
    csv_path = os.path.join(os.path.dirname(__file__), '../data/election_data.csv')
    analyze_election_data(csv_path)
