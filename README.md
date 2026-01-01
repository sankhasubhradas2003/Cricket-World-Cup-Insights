# Cricket World Cup Insights - BI & Data Visualization Project

Dataset and tools for creating a comprehensive Cricket World Cup analytics dashboard in Google Looker Studio.

**GitHub Repository:** [https://github.com/sankhasubhradas2003/Cricket-World-Cup-Insights](https://github.com/sankhasubhradas2003/Cricket-World-Cup-Insights)

## 📋 Project Status

**⚠️ INCOMPLETE - Dashboard Required**

This project requires a **Looker Studio dashboard** to be built and published. Currently, you have:
- ✅ Data files (CSV)
- ✅ Python analysis script (optional)
- ❌ **Looker Studio dashboard** (REQUIRED)
- ❌ **Published shareable link** (REQUIRED for submission)

## 🎯 Required Dashboard Features

1. **Filters**: Country-based performance (wins, most runs)
2. **Player Analytics**: Filter by wide balls, no balls, and total runs
3. **Comparisons**: Side-by-side player vs. player performance charts
4. **Trends**: Visualization of highest runs in a single innings over time
5. **Geospatial**: Best performing venues for the Indian team

## 🚀 Quick Start

### Step 1: Validate Your Data
```bash
python validate_data.py
```
This checks if your data supports all required features.

### Step 2: Build Looker Studio Dashboard

**📖 Follow the detailed guide:** `LOOKER_STUDIO_SETUP_GUIDE.md`

Quick steps:
1. Go to [Looker Studio](https://lookerstudio.google.com/)
2. Create new report → Upload CSV files
3. Implement all 5 required features (see guide)
4. Publish and get shareable link

### Step 3: (Optional) Python Analysis
```bash
pip install -r requirements.txt
python analyze_cricket_data.py
```

## 📁 Project Files

### Data Files
- **matches.csv**: Match results, teams, winners, scores, and venues
- **players.csv**: Individual player statistics (runs, balls, boundaries, wide balls, no balls)
- **venues.csv**: Venue details, match counts, and win statistics

### Documentation
- **LOOKER_STUDIO_SETUP_GUIDE.md**: Step-by-step dashboard creation guide
- **PROJECT_REQUIREMENTS_CHECKLIST.md**: Complete requirements checklist
- **DATA_ENHANCEMENT_GUIDE.md**: Tips for enhancing data if needed

### Scripts
- **validate_data.py**: Validates data against requirements
- **analyze_cricket_data.py**: Python-based data analysis (optional)

## ✅ Submission Checklist

Before submitting, ensure:
- [ ] Looker Studio dashboard is created
- [ ] All 5 required features are implemented
- [ ] Dashboard is published and shareable
- [ ] You have the shareable link ready
- [ ] Dashboard is tested and working correctly

## 📚 Documentation

- **LOOKER_STUDIO_SETUP_GUIDE.md**: Complete guide for building the dashboard
- **PROJECT_REQUIREMENTS_CHECKLIST.md**: Detailed requirements breakdown
- **DATA_ENHANCEMENT_GUIDE.md**: Data structure analysis and enhancement tips