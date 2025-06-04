from scoring import scoring
import sys
def main(home_team, away_team):
    return scoring(home_team, away_team)
if __name__ == "__main__":
    print("Welcome to NFL Game Sim!!!")
    home_team = sys.argv[1]
    away_team = sys.argv[2]
    main(home_team, away_team)