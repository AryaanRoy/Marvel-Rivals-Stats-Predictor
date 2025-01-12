# Marvel Rivals Analytics Project

## Overview
A data science project that analyzes hero performance metrics in Marvel Rivals using advanced web scraping and machine learning techniques. The project combines automated data collection with predictive analytics to generate insights about character performance at high-level competitive play.

## Results
Feature Importances:
Pick Rate: 0.878
Character Type_Duelist: 0.047
Character Type_Strategist: 0.040
Character Type_Vanguard: 0.036

## Features
- Automated web scraping of real-time game statistics using Selenium
- Data preprocessing and feature engineering pipeline
- Machine learning model for win rate prediction using Random Forest
- Feature importance analysis and visualization
- Focus on high-rank (Grandmaster+) competitive play metrics

## Technologies Used
- **Python** - Core programming language
- **Selenium** - Web automation and data collection
- **Pandas** - Data manipulation and analysis
- **Scikit-learn** - Machine learning implementation
- **Matplotlib** - Data visualization
- **Chrome WebDriver** - Browser automation

## Installation

Install required packages: pip install -r requirements.txt

Make sure you have Chrome browser installed for the web scraper

## Usage

1. Run the data collection script: scrape.py

2. Run the analysis: main.py


### Data Collection (scrape.py)
- Automated navigation through Marvel Rivals website
- Handles dynamic content loading
- Extracts character statistics for high-rank gameplay
- Implements error handling and wait conditions
- Exports data to structured CSV format

### Analysis (main.py)
- Data preprocessing and cleaning
- Feature scaling and encoding
- Random Forest model implementation
- Performance metrics calculation
- Feature importance visualization

## Model Performance
- R² Score: ~0.52
- MSE: ~8.15
- Key predictive features identified through importance analysis

## Future Improvements
- Implementation of time-series analysis for meta trends
- Addition of cross-validation
- Extended feature engineering
