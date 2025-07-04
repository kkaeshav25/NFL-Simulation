from team_data import choose_player
from ratings import ratings
from utilities import generate_yards
import random
def attempt_pat():
    if random.random()<0.95809:
        return 1
    else:
        return 0
    
def generate_td_play(team, play_type):
    if play_type == "pass":
        return f"{team} {choose_player(team, 'WR')} {generate_yards()} yard pass from {choose_player(team, 'QB')}"
    elif play_type == "run":
        return f"{team} {choose_player(team, 'RB')} {generate_yards()} yard run"
    elif play_type == "int":
        return f"{team} {choose_player(team, 'Secondary')} {generate_yards()} yard interception return"
    elif play_type == "fumble":
        return f"{team} {choose_player(team, 'Rush')} {generate_yards()} yard fumble return"
    
def score_drive(team, how_score):
    points = 0
    if how_score < 43:  # Pass TD
        points += 6
        description = generate_td_play(team, "pass")
    elif 43 < how_score < 80:  # Run TD
        points += 6
        description = generate_td_play(team, "run")
    elif 80 < how_score < 97:  # FG
        print(f"{team} FG GOOD")
        return 3
    else:  # Defensive TD
        if random.randint(0, 100) < 67:
            description = generate_td_play(team, "int")
        else:
            description = generate_td_play(team, "fumble")
        points += 6

    pat = attempt_pat()
    points += pat
    print(f"{description}.{' PAT GOOD' if pat else ''}")
    return points

def calculate_threshold(team1, team2):
    return 50+0.75*(ratings(team1) - ratings(team2))

def overtime(team1, team2, score1, score2):
    threshold = calculate_threshold(team1, team2)

    team1_ot_score = score_drive(team1, random.randint(0, 100))
    score1 += team1_ot_score

    if team1_ot_score < 6:
        team2_ot_score = score_drive(team2, random.randint(0, 100))
        score2 += team2_ot_score

    ot_rounds = 0
    while score1 == score2 and ot_rounds < 4:
        ot_rounds += 1
        if random.randint(1, 100) < threshold:
            score1 += score_drive(team1, random.randint(0, 100))
        else:
            score2 += score_drive(team2, random.randint(0, 100))

    return score1, score2

def scoring(team1, team2):
    score1 = score2 = 0
    for q in range(4):
        print(f"Quarter {q + 1}")
        for _ in range(random.randint(4, 6)):
            if random.randint(1, 100) < 47:
                ratings_threshold = calculate_threshold(team1, team2)
                how_score = random.randint(0, 100)

                if random.randint(1,100) < ratings_threshold:
                    score1 += score_drive(team1, how_score)
                else:
                    score2 += score_drive(team2, how_score)
    if score1 == score2:
        score1, score2 = overtime(team1, team2, score1, score2)

    print(f"FINAL: {team1}:{score1} - {team2}:{score2}")
    if score1 > score2:
        return {"home_score": score1, "away_score": score2, "winner": team1}
    elif score2 > score1:
        return {"home_score": score1, "away_score": score2, "winner": team2}
    else:
        return {"home_score": score1, "away_score": score2, "winner": "Tie"}
