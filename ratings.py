def ratings(team):
    team_ratings = {
        "ARI": 72,
        "ATL": 81,
        "BAL": 87,
        "BUF": 90,
        "CAR": 80,
        "CHI": 76,
        "CIN": 89,
        "CLE": 87,
        "DAL": 88,
        "DEN": 79,
        "DET": 86,
        "GB": 79,
        "HOU": 78,
        "IND": 77,
        "JAX": 84,
        "KC": 92,
        "LV": 79,
        "LAC": 85,
        "LAR": 73,
        "MIA": 86,
        "MIN": 85,
        "NE": 82,
        "NO": 82,
        "NYG": 82,
        "NYJ": 84,
        "PHI": 91,
        "PIT": 81,
        "SF": 86,
        "SEA": 83,
        "TB": 81,
        "TEN": 74,
        "WAS": 80
    }

    return team_ratings.get(team)  # default rating if team not found

