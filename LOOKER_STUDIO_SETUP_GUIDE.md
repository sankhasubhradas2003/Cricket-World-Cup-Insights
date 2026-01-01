# Looker Studio Dashboard Setup Guide

## Step 1: Prepare Your Data

Your CSV files are ready:
- `matches.csv` - Match results and statistics
- `players.csv` - Player performance data  
- `venues.csv` - Venue information

## Step 2: Create Looker Studio Dashboard

### 2.1 Create New Report
1. Go to [https://lookerstudio.google.com/](https://lookerstudio.google.com/)
2. Click **"Create"** → **"Data source"**
3. Select **"File upload"** → **"CSV file"**
4. Upload `matches.csv` first
5. Click **"Add a data source"** to add `players.csv` and `venues.csv`

### 2.2 Create New Report with Data Sources
1. Click **"Create"** → **"Report"**
2. Select your data sources (matches, players, venues)
3. Click **"Add"**

## Step 3: Implement Required Features

### Feature 1: Country-Based Performance Filters

**Create Filters:**
1. Add a **Filter Control** component
2. Set dimension: `team` (from players.csv) or `winner` (from matches.csv)
3. Add charts:
   - **Scorecard**: Total wins by country (from matches.csv, count of `winner`)
   - **Bar Chart**: Most runs by country (from players.csv, sum of `runs` grouped by `team`)

**Steps:**
- Insert → Scorecard → Metric: `winner` (Count), Dimension: `winner`
- Insert → Bar Chart → Metric: `runs` (Sum), Dimension: `team`

### Feature 2: Player Analytics Filters

**Create Filters:**
1. Add **Filter Controls** for:
   - `wide_balls` (Range filter)
   - `no_balls` (Range filter)
   - `runs` (Range filter)
2. Add a **Table** showing:
   - `player_name`, `team`, `runs`, `wide_balls`, `no_balls`, `year`

**Steps:**
- Insert → Filter Control → Dimension: `wide_balls` (set as range)
- Insert → Filter Control → Dimension: `no_balls` (set as range)
- Insert → Filter Control → Dimension: `runs` (set as range)
- Insert → Table → Add dimensions: `player_name`, `team`, `year`
- Add metrics: `runs`, `wide_balls`, `no_balls`

### Feature 3: Player vs Player Comparison

**Create Side-by-Side Charts:**
1. Add **Filter Control** for player selection (multi-select)
2. Create two **Column Charts** side by side:
   - Chart 1: Runs comparison
   - Chart 2: Wide balls + No balls comparison

**Steps:**
- Insert → Filter Control → Dimension: `player_name` (multi-select)
- Insert → Column Chart → 
  - Metric: `runs` (Sum)
  - Dimension: `player_name`
  - Add filter: Selected players only
- Insert → Column Chart →
  - Metrics: `wide_balls` (Sum), `no_balls` (Sum)
  - Dimension: `player_name`
  - Chart type: Stacked column

### Feature 4: Trends - Highest Runs in Single Innings Over Time

**Create Time Series Chart:**
1. Add **Time Series Chart**
2. X-axis: `year`
3. Y-axis: Maximum `runs` per year

**Steps:**
- Insert → Time Series Chart
- Dimension: `year`
- Metric: `runs` (MAX) - This shows highest runs per year
- Chart type: Line chart
- Title: "Highest Runs in Single Innings Over Time"

**Note:** If you need highest runs per match (not per year), you may need to add a calculated field or restructure data.

### Feature 5: Geospatial - Best Performing Venues for Indian Team

**Create Map/Bar Chart:**
1. Filter venues data for `team = "India"`
2. Create visualization showing venue performance

**Option A - Bar Chart (if geospatial coordinates unavailable):**
- Insert → Bar Chart
- Dimension: `venue`
- Metric: `matches_won` (Sum) or win rate
- Filter: `team = "India"`
- Sort by: `matches_won` descending

**Option B - Geo Chart (if you add coordinates):**
- Add latitude/longitude to venues.csv
- Insert → Geo Chart
- Location dimension: `city` or `venue`
- Metric: `matches_won`
- Filter: `team = "India"`

**Steps:**
- Insert → Bar Chart
- Dimension: `venue`
- Metric: `matches_won` (Sum)
- Add filter: `team` = "India"
- Sort: Descending by `matches_won`

## Step 4: Enhance Data (Optional but Recommended)

### Add Geospatial Coordinates to venues.csv
If you want a true map visualization, add columns:
- `latitude`
- `longitude`

Example:
```csv
venue,city,country,team,matches_played,matches_won,latitude,longitude
Wankhede,Mumbai,India,India,10,8,19.0760,72.8777
```

## Step 5: Publish and Share

1. Click **"Share"** button (top right)
2. Click **"Get shareable link"**
3. Set permissions:
   - **"Anyone with the link can view"** (for submission)
   - Or **"Specific people"** if you prefer
4. Copy the shareable link
5. This link is what you submit!

## Step 6: Final Checklist

Before submission, verify:
- [ ] All 5 required features are implemented
- [ ] Filters work correctly
- [ ] Charts display data properly
- [ ] Dashboard is visually organized
- [ ] Dashboard is published and shareable
- [ ] You have the shareable link ready

## Tips

1. **Data Blending**: If you need to join data from multiple sources, use Looker Studio's data blending feature
2. **Calculated Fields**: Create calculated fields for ratios (e.g., win rate = matches_won / matches_played)
3. **Styling**: Use consistent colors and fonts for professional appearance
4. **Layout**: Organize filters at the top, charts below in a logical flow

## Troubleshooting

- **Missing data**: Ensure all CSV files are uploaded correctly
- **Filters not working**: Check that filter dimensions match chart dimensions
- **No geospatial data**: Use bar charts instead of maps, or add coordinates to venues.csv

