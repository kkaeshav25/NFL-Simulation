from team_data import choose_player
from ratings import ratings
from utilities import generate_yards
import random

def scoring (team1,team2):
    winner = ""
    score1 = 0
    score2 = 0
    ratings_threshold = 0
    for i in range(4):
        print(f"Quarter {i+1}")
        drives_per_quarter = random.randint(4,5)
        for i in range(drives_per_quarter): #22 drives in a game
            if random.randint(1,100) < 41:
                which_team = random.randint(43,57)
                if ratings(team1)>ratings(team2):
                    ratings_threshold = 50+(0.5*(ratings(team1)-ratings(team2)))              
                elif ratings(team1)<ratings(team2):
                    ratings_threshold =50+(0.5*(ratings(team1)-ratings(team2)))
                elif ratings(team1)==ratings(team2):
                    ratings_threshold = 50
                how_score = random.randint(0,100)            
                if which_team < ratings_threshold: #Team1 scores
                    if how_score<43: #Passing Touchdowns
                        score1 +=6
                        if random.random() < 0.8614: #PAT
                            score1+=1
                            print (team1 + " " + choose_player(team1, "WR") + " "+ str(generate_yards())+ " yard pass from " + choose_player(team1, "QB")  +". PAT GOOD " + str(score1)+"-"+str(score2))
                        else: 
                            print (team1 + " " + choose_player(team1, "WR") + " "+ str(generate_yards())+ " yard pass from " + choose_player(team1, "QB") +". " + str(score1)+"-"+str(score2)) 
                    elif 43< how_score<80: #Rushing Touchdown
                        score1+=6
                        if random.random() < 0.8614: #PAT 
                            score1+=1
                            print (team1 + " "+ choose_player(team1, "RB") + " "+ str(generate_yards())+" yard run. PAT GOOD "+ str(score1)+"-"+str(score2))
                        else: 
                            print (team1 + " "+ choose_player(team1, "RB") + " "+ str(generate_yards())+" yard run "+ str(score1)+"-"+str(score2))
                    elif 80<how_score<97: #Field Goal
                        score1+=3
                        print (team1 + " FG GOOD "+ str(score1)+"-"+str(score2))
                    elif how_score>97: #Defensive Touchdown
                        defensive_possibilities = random.randint(0,100)
                        if defensive_possibilities<67:#Interception
                            score1+=6
                            if random.random() < 0.8614: #PAT
                                score1+=1
                                print (team1 + " " + choose_player(team1, "Secondary") + " "+ str(generate_yards())+ " yard interception return"  +". PAT GOOD " + str(score1)+"-"+str(score2))
                            else:
                                print (team1 + " " + choose_player(team1, "Secondary") + " "+ str(generate_yards())+ " yard interception return. " + str(score1)+"-"+str(score2))
                        elif defensive_possibilities >67: #Fumble
                            score1+=6
                            if random.random() < 0.8614: #PAT
                                score1+=1
                                print (team1 + " " + choose_player(team1, "Rush") + " "+ str(generate_yards())+ " yard fumble return"  +". PAT GOOD " + str(score1)+"-"+str(score2))
                            else:
                                print (team1 + " " + choose_player(team1, "Rush") + " "+ str(generate_yards())+ " yard fumble return. " + str(score1)+"-"+str(score2))                                  
                elif which_team > ratings_threshold: #Team 2 Scores
                    if how_score<43:
                        score2+=6
                        if random.random() < 0.8614:
                            score2+=1
                            print (team2 + " " + choose_player(team2, "WR") +  " "+ str(generate_yards())+" yard pass from " + choose_player(team2, "QB")  +". PAT GOOD " + str(score1)+"-"+str(score2))
                        else: 
                            print (team2 + " " + choose_player(team2, "WR") + " "+ str(generate_yards())+" yard pass from " + choose_player(team2, "QB") +"." + str(score1)+"-"+str(score2))
                    elif 43<how_score<80:
                        score2+=6
                        if random.random() < 0.8614:
                            score2+=1
                            print (team2 + " "+ choose_player(team2, "RB") + " "+ str(generate_yards())+ " yard run. PAT GOOD "+ str(score1)+"-"+str(score2))
                        else: 
                            print (team2 + " "+ choose_player(team2, "RB") + " "+ str(generate_yards())+ " yard run "+ str(score1)+"-"+str(score2))                 
                    elif 80<how_score<97:
                        score2+=3
                        print (team2 + " FG GOOD "+ str(score1)+"-"+str(score2))
                    elif how_score>97: #Defensive Touchdown
                        defensive_possibilities = random.randint(0,100)
                        if defensive_possibilities <67:#Interception
                            score2+=6
                            if random.random() < 0.8614: #PAT
                                score2+=1
                                print (team2 + " " + choose_player(team2, "Secondary") + " "+ str(generate_yards())+ " yard interception return"  +". PAT GOOD " + str(score1)+"-"+str(score2))
                            else:
                                print (team1 + " " + choose_player(team2, "Secondary") + " "+ str(generate_yards())+ " yard interception return. " + str(score1)+"-"+str(score2))
                        elif defensive_possibilities >67: #Fumble
                            score2+=6
                            if random.random() < 0.8614: #PAT
                                score2+=1
                                print (team2 + " " + choose_player(team2, "Rush") + " "+ str(generate_yards())+ " yard fumble return"  +". PAT GOOD " + str(score1)+"-"+str(score2))
                            else:
                                print (team2 + " " + choose_player(team2, "Rush") + " "+ str(generate_yards())+ " yard fumble return. " + str(score1)+"-"+str(score2))
                    
    if score1 == score2:
        print("TIE GAME! Going to OVERTIME...")

        ot_possessions = 0
        while score1 == score2 and ot_possessions < 10:  # Prevent infinite loop
            ot_possessions += 1
            which_team = random.randint(43, 57)
            ratings_threshold = 50 + 0.5 * (ratings(team1) - ratings(team2))
            how_score = random.randint(0, 100)

            if which_team < ratings_threshold:  # team1 scores
                if how_score < 43:  # Passing TD
                    score1 += 6
                    if random.random() < 0.8614:
                        score1 += 1
                        print(team1 + " " + choose_player(team1, "WR") + " " + str(generate_yards()) + " yard pass from " + choose_player(team1, "QB") + ". PAT GOOD " + str(score1) + "-" + str(score2))
                    else:
                        print(team1 + " " + choose_player(team1, "WR") + " " + str(generate_yards()) + " yard pass from " + choose_player(team1, "QB") + ". " + str(score1) + "-" + str(score2))
                elif 43 < how_score < 80:  # Rushing TD
                    score1 += 6
                    if random.random() < 0.8614:
                        score1 += 1
                        print(team1 + " " + choose_player(team1, "RB") + " " + str(generate_yards()) + " yard run. PAT GOOD " + str(score1) + "-" + str(score2))
                    else:
                        print(team1 + " " + choose_player(team1, "RB") + " " + str(generate_yards()) + " yard run. " + str(score1) + "-" + str(score2))
                elif 80 < how_score < 97:  # Field Goal
                    score1 += 3
                    print(team1 + " FG GOOD " + str(score1) + "-" + str(score2))
                else:  # Defensive score
                    if random.randint(0, 100) < 67:  # Interception return
                        score1 += 6
                        if random.random() < 0.8614:
                            score1 += 1
                            print(team1 + " " + choose_player(team1, "Secondary") + " " + str(generate_yards()) + " yard interception return. PAT GOOD " + str(score1) + "-" + str(score2))
                        else:
                            print(team1 + " " + choose_player(team1, "Secondary") + " " + str(generate_yards()) + " yard interception return. " + str(score1) + "-" + str(score2))
                    else:  # Fumble return
                        score1 += 6
                        if random.random() < 0.8614:
                            score1 += 1
                            print(team1 + " " + choose_player(team1, "Rush") + " " + str(generate_yards()) + " yard fumble return. PAT GOOD " + str(score1) + "-" + str(score2))
                        else:
                            print(team1 + " " + choose_player(team1, "Rush") + " " + str(generate_yards()) + " yard fumble return. " + str(score1) + "-" + str(score2))
            else:  # team2 scores
                if how_score < 43:
                    score2 += 6
                    if random.random() < 0.8614:
                        score2 += 1
                        print(team2 + " " + choose_player(team2, "WR") + " " + str(generate_yards()) + " yard pass from " + choose_player(team2, "QB") + ". PAT GOOD " + str(score1) + "-" + str(score2))
                    else:
                        print(team2 + " " + choose_player(team2, "WR") + " " + str(generate_yards()) + " yard pass from " + choose_player(team2, "QB") + ". " + str(score1) + "-" + str(score2))
                elif 43 < how_score < 80:
                    score2 += 6
                    if random.random() < 0.8614:
                        score2 += 1
                        print(team2 + " " + choose_player(team2, "RB") + " " + str(generate_yards()) + " yard run. PAT GOOD " + str(score1) + "-" + str(score2))
                    else:
                        print(team2 + " " + choose_player(team2, "RB") + " " + str(generate_yards()) + " yard run. " + str(score1) + "-" + str(score2))
                elif 80 < how_score < 97:
                    score2 += 3
                    print(team2 + " FG GOOD " + str(score1) + "-" + str(score2))
                else:
                    if random.randint(0, 100) < 67:
                        score2 += 6
                        if random.random() < 0.8614:
                            score2 += 1
                            print(team2 + " " + choose_player(team2, "Secondary") + " " + str(generate_yards()) + " yard interception return. PAT GOOD " + str(score1) + "-" + str(score2))
                        else:
                            print(team2 + " " + choose_player(team2, "Secondary") + " " + str(generate_yards()) + " yard interception return. " + str(score1) + "-" + str(score2))
                    else:
                        score2 += 6
                        if random.random() < 0.8614:
                            score2 += 1
                            print(team2 + " " + choose_player(team2, "Rush") + " " + str(generate_yards()) + " yard fumble return. PAT GOOD " + str(score1) + "-" + str(score2))
                        else:
                            print(team2 + " " + choose_player(team2, "Rush") + " " + str(generate_yards()) + " yard fumble return. " + str(score1) + "-" + str(score2))
    
    print("FINAL: " + team1 + ":" + str(score1) + " - " + team2 + ":" + str(score2))
    if(score1 > score2):
        winner = team1
    elif(score2>score1):
        winner =  team2
    else:
        winner = "Tie"
    return {"home_score": score1, "away_score": score2, "winner": winner}

