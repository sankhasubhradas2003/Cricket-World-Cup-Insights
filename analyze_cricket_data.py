"""
Cricket World Cup Insights - Data Analysis Script
This script analyzes the Cricket World Cup dataset and generates insights.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

def load_data():
    """Load all CSV files"""
    print("Loading data...")
    matches = pd.read_csv('matches.csv')
    players = pd.read_csv('players.csv')
    venues = pd.read_csv('venues.csv')
    return matches, players, venues

def analyze_matches(matches):
    """Analyze match data"""
    print("\n" + "="*50)
    print("MATCH ANALYSIS")
    print("="*50)
    
    print(f"\nTotal Matches: {len(matches)}")
    print(f"Years covered: {matches['year'].min()} - {matches['year'].max()}")
    
    # Team performance
    print("\n--- Team Win Statistics ---")
    win_counts = matches['winner'].value_counts()
    print(win_counts)
    
    # Year-wise analysis
    print("\n--- Matches by Year ---")
    matches_by_year = matches['year'].value_counts().sort_index()
    print(matches_by_year)
    
    return win_counts, matches_by_year

def analyze_players(players):
    """Analyze player data"""
    print("\n" + "="*50)
    print("PLAYER ANALYSIS")
    print("="*50)
    
    print(f"\nTotal Player Records: {len(players)}")
    
    # Top run scorers
    print("\n--- Top 10 Run Scorers ---")
    top_scorers = players.nlargest(10, 'runs')[['player_name', 'team', 'runs', 'year']]
    print(top_scorers.to_string(index=False))
    
    # Team-wise runs
    print("\n--- Total Runs by Team ---")
    team_runs = players.groupby('team')['runs'].sum().sort_values(ascending=False)
    print(team_runs)
    
    return top_scorers, team_runs

def analyze_venues(venues):
    """Analyze venue data"""
    print("\n" + "="*50)
    print("VENUE ANALYSIS")
    print("="*50)
    
    print(f"\nTotal Venues: {len(venues)}")
    
    # Most used venues
    print("\n--- Most Used Venues ---")
    venue_usage = venues.sort_values('matches_played', ascending=False)
    print(venue_usage[['venue', 'city', 'country', 'matches_played', 'matches_won']].to_string(index=False))
    
    return venue_usage

def create_visualizations(matches, players, venues, win_counts, top_scorers, team_runs):
    """Create visualizations"""
    print("\n" + "="*50)
    print("GENERATING VISUALIZATIONS")
    print("="*50)
    
    # Create figure with subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Cricket World Cup Insights', fontsize=16, fontweight='bold')
    
    # 1. Team Win Counts
    ax1 = axes[0, 0]
    win_counts.plot(kind='bar', ax=ax1, color='steelblue')
    ax1.set_title('Total Wins by Team')
    ax1.set_xlabel('Team')
    ax1.set_ylabel('Number of Wins')
    ax1.tick_params(axis='x', rotation=45)
    
    # 2. Top Run Scorers
    ax2 = axes[0, 1]
    top_10 = top_scorers.head(10)
    ax2.barh(range(len(top_10)), top_10['runs'], color='coral')
    ax2.set_yticks(range(len(top_10)))
    ax2.set_yticklabels(top_10['player_name'])
    ax2.set_title('Top 10 Run Scorers')
    ax2.set_xlabel('Total Runs')
    ax2.invert_yaxis()
    
    # 3. Team Runs
    ax3 = axes[1, 0]
    team_runs.plot(kind='bar', ax=ax3, color='green')
    ax3.set_title('Total Runs by Team')
    ax3.set_xlabel('Team')
    ax3.set_ylabel('Total Runs')
    ax3.tick_params(axis='x', rotation=45)
    
    # 4. Matches by Year
    ax4 = axes[1, 1]
    matches_by_year = matches['year'].value_counts().sort_index()
    matches_by_year.plot(kind='line', marker='o', ax=ax4, color='purple')
    ax4.set_title('Matches Played by Year')
    ax4.set_xlabel('Year')
    ax4.set_ylabel('Number of Matches')
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('cricket_insights.png', dpi=300, bbox_inches='tight')
    print("\nVisualization saved as 'cricket_insights.png'")
    plt.show()

def main():
    """Main function"""
    try:
        # Load data
        matches, players, venues = load_data()
        
        # Analyze data
        win_counts, matches_by_year = analyze_matches(matches)
        top_scorers, team_runs = analyze_players(players)
        venue_usage = analyze_venues(venues)
        
        # Create visualizations
        create_visualizations(matches, players, venues, win_counts, top_scorers, team_runs)
        
        print("\n" + "="*50)
        print("ANALYSIS COMPLETE!")
        print("="*50)
        
    except FileNotFoundError as e:
        print(f"Error: Could not find file - {e}")
        print("Make sure all CSV files (matches.csv, players.csv, venues.csv) are in the current directory.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

