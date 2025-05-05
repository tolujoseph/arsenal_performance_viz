import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from datetime import datetime

# ------------------ CONFIGURATION ------------------
API_TOKEN = 'YOUR_API_TOKEN'  # football-data.org API token
TEAM_ID = 57  # Arsenal FC
COMPETITION_CODE = 'PL'  # Premier League
SEASON_YEAR = 2024  # Adjust as needed
OUTPUT_DIR = 'output'

HEADERS = {'X-Auth-Token': API_TOKEN}

os.makedirs(OUTPUT_DIR, exist_ok=True)
# ---------------------------------------------------

def fetch_arsenal_matches():
    url = f'https://api.football-data.org/v4/teams/{TEAM_ID}/matches'
    params = {
        'competitions': COMPETITION_CODE,
        'season': SEASON_YEAR,
        'status': 'FINISHED'
    }
    response = requests.get(url, headers=HEADERS, params=params)
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")
    data = response.json()
    matches = data.get('matches', [])
    return matches

def process_matches(matches):
    records = []
    for match in matches:
        date = match['utcDate'][:10]
        home_team = match['homeTeam']['name']
        away_team = match['awayTeam']['name']
        home_score = match['score']['fullTime']['home']
        away_score = match['score']['fullTime']['away']
        is_home = home_team == 'Arsenal FC'
        opponent = away_team if is_home else home_team
        goals_for = home_score if is_home else away_score
        goals_against = away_score if is_home else home_score
        if goals_for > goals_against:
            result = 'W'
        elif goals_for == goals_against:
            result = 'D'
        else:
            result = 'L'
        records.append({
            'Date': date,
            'Opponent': opponent,
            'IsHome': is_home,
            'GF': goals_for,
            'GA': goals_against,
            'Result': result
        })
    df = pd.DataFrame(records)
    df['Date'] = pd.to_datetime(df['Date'])
    df.sort_values('Date', inplace=True)
    return df

def plot_form_trend(df):
    df['Points'] = df['Result'].map({'W': 3, 'D': 1, 'L': 0})
    df['RollingPoints'] = df['Points'].rolling(5).mean()
    plt.figure(figsize=(12, 5))
    sns.lineplot(x='Date', y='RollingPoints', data=df, marker='o')
    plt.title('Arsenal Rolling Form (Last 5 Matches Avg Points)')
    plt.ylabel('Avg Points')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/form_trend.png")
    plt.close()
    print("[INFO] Saved: form_trend.png")

def plot_goals_home_away(df):
    grouped = df.groupby('IsHome')[['GF', 'GA']].mean().rename(index={True: 'Home', False: 'Away'})
    grouped.plot(kind='bar', figsize=(8, 5))
    plt.title('Avg Goals Scored and Conceded (Home vs Away)')
    plt.ylabel('Goals per Game')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/goals_home_away.png")
    plt.close()
    print("[INFO] Saved: goals_home_away.png")

def plot_results_distribution(df):
    sns.countplot(data=df, x='Result', order=['W', 'D', 'L'], palette='pastel')
    plt.title('Arsenal Match Result Distribution')
    plt.xlabel('Result')
    plt.ylabel('Number of Matches')
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/result_distribution.png")
    plt.close()
    print("[INFO] Saved: result_distribution.png")

def main():
    print("[INFO] Fetching match data...")
    matches = fetch_arsenal_matches()
    print(f"[INFO] Retrieved {len(matches)} matches.")
    df = process_matches(matches)
    print("[INFO] Processing and generating visualizations...")
    plot_form_trend(df)
    plot_goals_home_away(df)
    plot_results_distribution(df)
    print(f"[INFO] All plots saved to '{OUTPUT_DIR}' directory.")

if __name__ == '__main__':
    main()
