import csv
import sys
from main import main as simulation

def load_schedule (schedule_file):
    schedule = []
    with open(schedule_file, newline = '') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def main(schedule_file, results_file):
    schedule = load_schedule(schedule_file)
    results = []
    for game in schedule:
        home = game['Home Team']
        away = game["Away Team"]
        result = simulation(home, away)
        results.append({
            "home_team": home,
            "away_team": away, 
            "home_score": result["home_score"],
            "away_score":result["away_score"],
            "winner": result["winner"]
        })
    with open(results_file, 'w', newline='') as csvfile:
        fieldnames = ['home_team', 'away_team', 'home_score', 'away_score', 'winner']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for r in results:
            writer.writerow(r)
main("Week 1.csv", "Week 1 Results.csv")