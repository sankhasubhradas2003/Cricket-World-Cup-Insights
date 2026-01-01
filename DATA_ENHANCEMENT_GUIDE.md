# Data Enhancement Guide

## Current Data Structure Analysis

### matches.csv
- Fields: `match_id`, `year`, `team_1`, `team_2`, `winner`, `venue`, `runs_team1`, `runs_team2`
- ✅ Good for: Wins by country, match statistics

### players.csv  
- Fields: `player_name`, `team`, `runs`, `balls`, `fours`, `sixes`, `wide_balls`, `no_balls`, `year`
- ✅ Good for: Player analytics, runs filtering, wide balls, no balls
- ⚠️ Note: `runs` appears to be per player per year, not per match/innings

### venues.csv
- Fields: `venue`, `city`, `country`, `team`, `matches_played`, `matches_won`
- ✅ Good for: Venue performance
- ⚠️ Missing: Latitude/longitude for true geospatial visualization

## Potential Enhancements

### 1. For "Highest Runs in Single Innings Over Time"

**Current Issue**: The `runs` field in players.csv might be aggregated per year, not per innings.

**Solution Options**:
- **Option A**: If data is already per-innings, use MAX(runs) grouped by year
- **Option B**: If data needs enhancement, add a `match_id` field to players.csv to link to matches
- **Option C**: Clarify requirement - does "single innings" mean:
  - Highest runs by any player in a year? (use MAX)
  - Highest runs in a specific match? (need match_id)

### 2. For Geospatial Visualization

**Add to venues.csv**:
```csv
venue,city,country,team,matches_played,matches_won,latitude,longitude
```

You can get coordinates from:
- Google Maps
- Geocoding APIs
- Online coordinate finders

### 3. For Better Player Comparisons

**Consider adding**:
- `match_id` to link players to specific matches
- `innings_number` if multiple innings per match
- `strike_rate` (calculated: runs/balls * 100)
- `average` (calculated: total_runs / dismissals)

## Quick Data Check Script

Run this to verify your data supports all requirements:

```python
import pandas as pd

matches = pd.read_csv('matches.csv')
players = pd.read_csv('players.csv')
venues = pd.read_csv('venues.csv')

print("=== DATA CHECK ===")
print(f"\nMatches: {len(matches)} records")
print(f"Players: {len(players)} records")
print(f"Venues: {len(venues)} records")

print("\n=== REQUIRED FIELDS CHECK ===")
print("\n1. Country-based wins: ✅" if 'winner' in matches.columns else "❌")
print("2. Country-based runs: ✅" if 'team' in players.columns and 'runs' in players.columns else "❌")
print("3. Wide balls filter: ✅" if 'wide_balls' in players.columns else "❌")
print("4. No balls filter: ✅" if 'no_balls' in players.columns else "❌")
print("5. Total runs filter: ✅" if 'runs' in players.columns else "❌")
print("6. Player comparison: ✅" if 'player_name' in players.columns else "❌")
print("7. Highest runs over time: ✅" if 'runs' in players.columns and 'year' in players.columns else "❌")
print("8. Venue performance: ✅" if 'venue' in venues.columns and 'matches_won' in venues.columns else "❌")
print("9. India team filter: ✅" if 'team' in venues.columns else "❌")
```

