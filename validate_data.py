"""
Data Validation Script
Checks if the data files support all required Looker Studio dashboard features.
"""

import pandas as pd

def validate_data():
    """Validate that data supports all requirements"""
    print("="*60)
    print("CRICKET WORLD CUP DATA VALIDATION")
    print("="*60)
    
    try:
        matches = pd.read_csv('matches.csv')
        players = pd.read_csv('players.csv')
        venues = pd.read_csv('venues.csv')
        
        print("\n[OK] All CSV files loaded successfully")
        print(f"   - Matches: {len(matches)} records")
        print(f"   - Players: {len(players)} records")
        print(f"   - Venues: {len(venues)} records")
        
    except FileNotFoundError as e:
        print(f"\n[X] Error: {e}")
        return False
    
    print("\n" + "="*60)
    print("REQUIREMENT CHECKLIST")
    print("="*60)
    
    checks = []
    
    # 1. Country-based performance (wins, most runs)
    print("\n1. Country-based Performance Filters")
    if 'winner' in matches.columns:
        print("   [OK] Wins by country: Available (matches.winner)")
        checks.append(True)
    else:
        print("   [X] Wins by country: Missing 'winner' field")
        checks.append(False)
    
    if 'team' in players.columns and 'runs' in players.columns:
        print("   [OK] Most runs by country: Available (players.team, players.runs)")
        checks.append(True)
    else:
        print("   [X] Most runs by country: Missing fields")
        checks.append(False)
    
    # 2. Player Analytics: Filter by wide balls, no balls, total runs
    print("\n2. Player Analytics Filters")
    if 'wide_balls' in players.columns:
        print("   [OK] Wide balls filter: Available")
        checks.append(True)
    else:
        print("   [X] Wide balls filter: Missing 'wide_balls' field")
        checks.append(False)
    
    if 'no_balls' in players.columns:
        print("   [OK] No balls filter: Available")
        checks.append(True)
    else:
        print("   [X] No balls filter: Missing 'no_balls' field")
        checks.append(False)
    
    if 'runs' in players.columns:
        print("   [OK] Total runs filter: Available")
        checks.append(True)
    else:
        print("   [X] Total runs filter: Missing 'runs' field")
        checks.append(False)
    
    # 3. Player vs Player Comparison
    print("\n3. Player vs Player Comparison")
    if 'player_name' in players.columns:
        print("   [OK] Player comparison: Available (players.player_name)")
        checks.append(True)
    else:
        print("   [X] Player comparison: Missing 'player_name' field")
        checks.append(False)
    
    # 4. Trends: Highest runs in single innings over time
    print("\n4. Trends: Highest Runs Over Time")
    if 'runs' in players.columns and 'year' in players.columns:
        print("   [OK] Highest runs over time: Available (players.runs, players.year)")
        print("      Note: Using MAX(runs) grouped by year")
        checks.append(True)
    else:
        print("   [X] Highest runs over time: Missing required fields")
        checks.append(False)
    
    # 5. Geospatial: Best performing venues for Indian team
    print("\n5. Geospatial: Best Venues for Indian Team")
    if 'venue' in venues.columns and 'matches_won' in venues.columns:
        print("   [OK] Venue performance: Available (venues.venue, venues.matches_won)")
        checks.append(True)
    else:
        print("   [X] Venue performance: Missing required fields")
        checks.append(False)
    
    if 'team' in venues.columns:
        india_venues = venues[venues['team'] == 'India']
        if len(india_venues) > 0:
            print(f"   [OK] India team filter: Available ({len(india_venues)} records)")
            checks.append(True)
        else:
            print("   [WARNING] India team filter: No records found for India")
            checks.append(False)
    else:
        print("   [X] India team filter: Missing 'team' field")
        checks.append(False)
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    passed = sum(checks)
    total = len(checks)
    print(f"\n[OK] Passed: {passed}/{total} checks")
    
    if passed == total:
        print("\n[SUCCESS] All data requirements met! Ready for Looker Studio.")
        print("\nNext steps:")
        print("1. Follow LOOKER_STUDIO_SETUP_GUIDE.md")
        print("2. Build the dashboard in Looker Studio")
        print("3. Publish and get shareable link")
    else:
        print(f"\n[WARNING] {total - passed} requirement(s) need attention")
        print("   Check DATA_ENHANCEMENT_GUIDE.md for solutions")
    
    return passed == total

if __name__ == "__main__":
    validate_data()

