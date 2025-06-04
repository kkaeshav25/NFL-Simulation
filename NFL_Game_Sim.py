# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 18:56:26 2024

@author: kkaeshav
"""

#General Idea: Create a psuedo-box score for simulated NFL Game, ESPN style
import random
# How scoring is done    
def scoring (team1,team2):
    score1 = 0
    score2 = 0
    ratings_threshold = 0
    for i in range(4):
        print(f"Quarter {i+1}")
        drives_per_quarter = random.randint(4,5)
        for i in range(drives_per_quarter): #22 drives in a game
            if random.randint(1,100) < 28:
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
    else:
        print("FINAL: " + team1 + ":" + str(score1) + " - " + team2 + ":" + str(score2))



def choose_player(team, position): #Generates players for each team; QB, WR, and RB
    if team == "ARI":
        if position == "QB":
            return "Kyler Murray"
        elif position == "WR":
            WR_list = ["Marvin Harrison Jr.", "Zay Jones", "Michael Wilson", "Trey McBride"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["James Conner", "Trey Benson"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Sean Murphy-Bunting", "Budda Baker", "Jalen Thompson", "Garrett Williams"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["Zaven Collins", "Kyzir White", "Mack Wilson Sr.", "BJ Ojulari", "Bilal Nichols"]
            return random.choice(Rush_list)
    elif team == "ATL":
        if position == "QB":
            return "Kirk Cousins"
        elif position == "WR":
            WR_list = ["Drake London", "Darnell Mooney", "Rondale Moore", "Kyle Pitts"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Bijan Robinson", "Tyler Allgeier"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["AJ Terrell", "Jessie Bates III", "DeMarcco Hellams", "Clark Phillips III"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["Zach Harrison", "KAden Elliss", "Arnold Ebiketie", "Troy Andersen", "Grady Jarrett"]
            return random.choice(Rush_list)
    elif team == "BAL":
        if position == "QB":
            return "Lamar Jackson"
        elif position == "WR":
            WR_list = ["Zay Flowers", "Rashod Bateman", "Nelson Agholor", "Mark Andrews"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Derrick Henry", "Justice Hill"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Marlon Humphrey", "Kyle Hamilton", "Marcus Williams", "Brandon Stephens"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["Justin Madubuike", "Odafe Oweh", "Kyle Van Noy", "Roquan Smith", "Michael Pierce"]
            return random.choice(Rush_list)
    elif team == "BUF":
        if position == "QB":
            return "Josh Allen"
        elif position == "WR":
            WR_list = ["Khalil Shakir", "Marquez Valdes-Scantling", "Keon Coleman", "Dawson Knox"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["James Cook", "Ray Davis"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Rasul Douglas", "Mike Edwards", "Taylor Rapp", "Taron Johnson"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["Greg Rousseau", "Matt Milano", "Nicholas Morrow", "Von Miller", "Ed Oliver"]
            return random.choice(Rush_list)
    elif team == "CAR":
        if position == 'QB':
            return "Bryce Young"
        elif position == "WR":
            WR_list = ["Diontae Johnson", "Adam Theieln", "Xavier Legette", "Tommy Tremble"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Chubba Hubbard", "Jonathon Brooks"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Dane Jackson", "Xavier Woods", "Jordan Fuller", "Jaycee Horn"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["A'Shawn Robinson", "Shaq Thompson", "Jadeveon Clowney", "Dane Jackson", "Shy Tuttle"]
            return random.choice(Rush_list)
    elif team == "CHI":
        if position == "QB":
            return "Caleb Williams"
        elif position == "WR":
            WR_list = ["DJ Moore", "Keenan Allen", "Rome Odunze", "Cole Kmet"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["D'Andre Swift", "Khalil Herbert"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Jaylon Johnson", "Kevin Byard III", "Jaquan Brisker", "Tyrique Stevenson"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["DeMarcus Walker", "Tremaine Edmunds", "TJ Edwards", "Jack Sanborn", "Montez Sweat"]
            return random.choice(Rush_list)
    elif team == "CIN":
        if position == "QB":
            return "Joe Burrow"
        elif position == "WR":
            WR_list = ["Ja'Marr Chase", "Tee Higgins", "Jermaine Burton", "Mike Gesicki"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Zack Moss", "Chase Brown"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Cam Taylor-Britt", "Geno Stone", "Vonn Bell", "DJ Turner II"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["Sam Hubbard", "Logan Wilson", "Germaine Pratt", "Trey Hendrickson", "BJ Hill"]
            return random.choice(Rush_list)
    elif team == "CLE":
        if position == "QB":
            return "Deshaun Watson"
        elif position == "WR":
            WR_list = ["Amari Cooper", "Jerry Jeudy", "Elijah Moore", "David Njoku"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Nick Chubb", "Jerome Ford"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Denzel Ward", "Juan Thornhill", "Grant Delpit", "Greg Newsome II"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["Za'Darius Smith", "Devin Bush", "Jeremiah Owusu-Koramoah", "Jordan Hicks", "Myles Garrett"]
            return random.choice(Rush_list)
    elif team == "DAL":
        if position == "QB":
            return "Dak Prescott"
        elif position == "WR":
            WR_list = ["CeeDee Lamb", "Brandin Cooks", "Jalen Tolbert", "Jake Ferguson"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Ezekiel Elliot", "Rico Dowdle"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["DaRon Bland", "Donovan Wilson", "Malik Hooker", "Trevon Diggs"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["DeMarcus Lawrence", "Damone Clark", "Eric Kendricks", "Micah Parsons"]
            return random.choice(Rush_list)
    elif team == "DEN":
        if position == "QB":
            return "Bo Nix"
        elif position == "WR":
            WR_list = ["Courtland Sutton", "Josh Reynolds", "Marvin Mims Jr.", "Adam Trautman"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Javonte Williams", "Samaje Perine"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Levi Wallace", "Brandon Jones", "Caden Sterns", "Pat Surtain II"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["Zach Allen", "Alex Singleton", "Cody Barton", "Johnathon Cooper", "DJ Jones"]
            return random.choice(Rush_list)
    elif team == "DET":
        if position == "QB":
            return "Jared Goff"
        elif position == "WR":
            WR_list = ["Amon-Ra St. Brown", "Jameson Williams", "Kalif Raymond", "Sam LaPorta"]
            return random.choice(WR_list)
        elif position == 'RB':
            RB_list = ["David Montgomery", "Jahmyr Gibbs"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Terrion Arnold", "Carlton Davis III", "Brian Branch", "Kerby Joseph"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["Aiden Hutchinson", "Jack Campbell", "Alex Anzalone", "Derrick Barnes", "DJ Reader"]
            return random.choice(Rush_list)
    elif team == "GB":
        if position == "QB":
            return "Jordan Love"
        elif position == "WR":
            WR_list = ["Christian Watson", "Romeo Doubs", "Jayden Reed", "Luke Musgrave"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Josh Jacobs", "AJ Dillon"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Jaire Alexander", "Xavier McKinney", "Javon Bullard", "Eric Stokes"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["Preston Smith", "Quay Walker", "Edgerrin Cooper", "Isiah McDuffie", "Kenny Clark"]
            return random.choice(Rush_list)
    elif team == "HOU":
        if position == "QB":
            return "CJ Stroud"
        elif position == "WR":
            WR_list = ["Stefon Diggs", "Nico Collins", "Tank Dell", "Dalton Schultz"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Joe Mixon", "Dameon Pierce"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Jeff Okudah", "Jalen Pitre", "Jimmie Ward", "Derek Stingley Jr."]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["Will Anderson Jr.", "Denico Autry", "Christian Harris", "Derek Barnett", "Danielle Hunter"]
            return random.choice(Rush_list)
    elif team == "IND":
        if position == "QB":
            return "Anthony Richardson"
        elif position == "WR":
            WR_list = ["Michael Pittman Jr.", "Josh Downs", "Adonai Mitchell", "Jelani Woods"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Jonathon Taylor", "Trey Sermon"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Jaylin Simpson", "Nick Cross", "Julian Blackmon", "Kenny Moore II"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["Kwity Paye", "EJ Speed", "Zaire Franklin", "Samson Ebukam", "DeForest Buckner"]
            return random.choice(Rush_list)
    elif team == "JAX":
        if position == "QB":
            return "Trevor Lawrence"
        elif position == "WR":
            WR_list = ["Christian Kirk", "Gabe Davis", "Brian Thomas Jr.", "Evan Engram"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Travis Etienne Jr.", "Tank Bigsby"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Ronald Darby", "Terrell Edmunds", "Andre Cisco", "Tyson Campbell"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["Arik Armstead", "Josh Allen", "Travon Walker", "Devin Lloyd", "DaVon Hamilton"]
            return random.choice(Rush_list)
    elif team == "KC":
        if position == "QB":
            return "Patrick Mahomes"
        elif position == "WR":
            WR_list = ["Rashee Rice", "Marquise Brown", "Xavier Worthy", "Travis Kelce"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Isiah Pacheco", "Clyde Edwards-Helaire"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Trent McDuffie", "Bryan Cook", "Justin Reid", "Jaylen Watson"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["George Karlaftis", "Mike Danna", "Nick Bolton", "Derrick Nnadi", "Chris Jones"]
            return random.choice(Rush_list)
    elif team == "LV":
        if position == "QB":
            return "Aiden O'Connell"
        elif position == "WR":
            WR_list = ["Davante Adams", "Jakobi Mayers", "Michael Gallup", "Brock Bowers"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Zamir White", "Alexander Mattison"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Jack Jones", "Marcus Epps", "Tre'von Moehrig", "Nate Hobbs"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["Maxx Crosby", "Chrstian Wilkins", "Ropert Spillane", "Divine Deablo", "John Jenkins"]
            return random.choice(Rush_list)
    elif team == "LAC":
        if position == "QB":
            return "Justin Herbert"
        elif position == "WR":
            WR_list = ["Joshua Palmer", "Quentin Johnston", "Ladd McConkey", "Will Dissly"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Gus Edwards", "JK Dobbins"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Asante Samuel Jr.", "Alohi Gilman", "Derwin James Jr.", "Kristian Fulton"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["Poona Ford", "Junior Colson", "Denzel Perryman", "Khalil Mack", "Joey Bosa"]
            return random.choice(Rush_list)
    elif team == "LAR":
        if position == "QB":
            return "Matthew Stafford"
        elif position == "WR":
            WR_list = ["Cooper Kupp", "Puka Nacua", "Demarcus Robinson", "Tyler Higbee"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Kyren Williams", "Blake Corum"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Tre'Davious White", "Russ Yeast", "Kamren Curl", "Darious Williams"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["Braden Fiske", "Jared Verse", "Byron Young", "Troy Reeder", "Kobie Turner"]
            return random.choice(Rush_list)
    elif team == "MIA":
        if position == "QB":
            return "Tua Tagovailoa"
        elif position == "WR":
            WR_list = ["Tyreek Hill", "Jaylen Waddle", "Odell Beckham Jr.", "Jonnu Smith"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Raheem Mostert", "De'Von Achane"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Kendall Fuller", "Jevon Holland", "Jordan Poyer", "Jalen Ramsey"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["Zach Sieler", "Neville Gallimore", "Calais Campbell", "Jaelen Phillips", "Bradley Chubb"]
            return random.choice(Rush_list)
    elif team == "MIN":
        if position == "QB":
            return "JJ McCarthy"
        elif position == "WR":
            WR_list = ["Justin Jefferson", "Jordan Addison", "Brandon Powell", "TJ Hockenson"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Aaron Jones", "Ty Chandler"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Akayleb Evans", "Camryn Bynum", "Harrison Smith", "Byron Murphy Jr."]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["Jerry Tillery", "Blake Cashman", "Andrew Van Ginkel", "Kamu Gruiger-Hill", "Harrison Phillips"]
            return random.choice(Rush_list)
    elif team == "NE":
        if position == "QB":
            return "Drake Maye"
        elif position == "WR":
            WR_list = ["Kendrick Bourne", "DeMario Douglas", "JuJu Smith-Schuster", "Hunter Henry"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Rhamondre Stevenson", "Antonio Gibson"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Jonathan Jones", "Jabrill Peppers", "Kyle Dugger", "Christian Gonzalez"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["Keion White", "Matthew Judon", "Ja'Whuan Bentley", "Josh Uche", "Christian Barmore"]
            return random.choice(Rush_list)
    elif team == "NO":
        if position == "QB":
            return "Derek Carr"
        elif position == "WR":
            WR_list = ["Chris Olave", "Rashid Shaheed", "Cedrick Wilson Jr.", "Juwan Johnson"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Alvin Kamara", "Jamaal Williams"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Kool-Aid McKinstry", "Tyrann Mathieu", "Will Harris", "Marshon Lattimore"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["Cameron Jordan", "Nathan Shepherd", "Chase Young", "Demario Davis", "Willie Gay"]
            return random.choice(Rush_list)
    elif team == "NYG":
        if position == "QB":
            return "Daniel Jones"
        elif position == "WR":
            WR_list = ["Malik Nabers", "Darius Slayton", "Allen Robinson II", "Darren Waller"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Devin Singletary", "Eric Gray"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Cor'Dale Flott", "Jalen Mills", "Jason Pinnock", "Deontae Banks"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["DJ Davidson", "Dexter Lawrence II", "Brian Burns", "Kayvon Thibodeaux", "Isiah Simmons"]
            return random.choice(Rush_list)
    elif team == "NYJ":
        if position == "QB":
            return "Aaron Rodgers"
        elif position == "WR":
            WR_list = ["Garrett Wilson", "Mike Williams", "Allen Lazard", "Tyler Conklin"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Breece Hall", "Braelon Allen"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Sauce Gardner", "Chuck Clark", "Tony Adams", "DJ Reed"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["Jermaine Johnson", "CJ Mosley", "Haason Reddick", "Quincy Williams", "Quinnen Williams"]
            return random.choice(Rush_list)
    elif team == "PHI":
        if position == 'QB':
            return "Jalen Hurts"
        elif position == "WR":
            WR_list = ["AJ Brown", "DeVonta Smith", "Parris Campbell", "Dallas Goedert"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Saquon Barkley", "Kenneth Gainwell"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Quinyon Mitchell", "Cooper DeJean", "CJ Gardner-Johnson", "Darius Slay Jr."]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["Jordan Davis", "Nakobe Dean", "Devin White", "Nolan Smith", "Jalen Carter"]
            return random.choice(Rush_list)
    elif team == "PIT":
        if position == "QB":
            return "Russell Wilson"
        elif position == "WR":
            WR_list = ["George Pickens", "Van Jefferson", "Roman Wilson", "Pat Freiermuth"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Najee Harris", "Jaylen Warren"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Cam Sutton", "Minkah Fitzpatrick", "DeShon Elliott", "Donte Jackson"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["Larry Ogunjobi", "TJ Watt", "Patrick Queen", "Alex Highsmith", "Cameron Heyward"]
            return random.choice(Rush_list)
    elif team == "SF":
        if position == "QB":
            return "Brock Purdy"
        elif position == "WR":
            WR_list = ["Deebo Samuel", "Brandon Aiyuk", "Jauan Jennings", "George Kittle"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Christian McCaffrey", "Elijah Mitchell"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Charvarius Ward", "Talanoa Hufanga", "Ji'Ayir Brown", "Deommodore Lenoir"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["Leonard Floyd", "Dre Greenlaw", "Fred Warner", "De'Vondre Campbell", "Nick Bosa"]
            return random.choice(Rush_list)
    elif team == "SEA":
        if position == "QB":
            return "Geno Smith"
        elif position == "WR":
            WR_list = ["DK Metcalf", "Tyler Lockett", "Jaxon Smith-Njigba", "Noah Fant"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Kenneth Walker III", "Zach Charbonnet"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Devon Witherspoon", "Julian Love", "Rayshawn Jenkins", "Riq Woolen"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["Byron Murphy II", "Jerome Baker", "Uchenna Nwosu", "Tyrel Dodson", "Leonard Williams"]
            return random.choice(Rush_list)
    elif team == "TB":
        if position == "QB":
            return "Baker Mayfield"
        elif position == "WR":
            WR_list = ["Mike Evans", "Chris Godwin", "Trey Palmer", "Cade Otton"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Rachaad White", "Chase Edmonds"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Jamel Dean", "Antoine Winfield Jr.", "Jordan Whitehead", "Zyon McCollum"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["Vita Vea", "KJ Britt", "Lavonte David", "Joe Tryon-Shoyinka", "Logan Hall"]
            return random.choice(Rush_list)
    elif team == "TEN":
        if position == "QB":
            return "Will Levis"
        elif position == "WR":
            WR_list = ["Calvin Ridley", "DeAndre Hopkins", "Tyler Boyd", "Josh Whyle"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Tony Pollard", "Tyjae Spears"]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Chidobe Awuzie", "Elijah Molden", "Amani Hooker", "L'Jarius Sneed"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["Sebastian Joseph-Day", "Harold Landry III", "Kenneth Murray Jr.", "Arden Key", "Jeffrey Simmons"]
            return random.choice(Rush_list)
    elif team == "WAS":
        if position == "QB":
            return "Jayden Daniels"
        elif position == "WR":
            WR_list = ["Terry McLaurin", "Jahan Dotson", "Luke McCaffrey", "Zach Ertz"]
            return random.choice(WR_list)
        elif position == "RB":
            RB_list = ["Austin Ekeler", "Brian Robinson Jr."]
            return random.choice(RB_list)
        elif position == "Secondary":
            Secondary_list = ["Emmanuel Forbes Jr.", "Percy Butler", "Jeremy Chinn", "Mike Sainristil"]
            return random.choice(Secondary_list)
        elif position == "Rush":
            Rush_list = ["Dante Fowler Jr.", "Bobby Wagner", "Jamin Davis", "Daron Payne", "Jonathan Allen"]
            return random.choice(Rush_list)
        
        
def generate_yards(): #Generate random number of yards
    yards = int(random.triangular (0,99,6))
    return yards

def ratings (team):
    if team  == "ARI":
        Madden_Rating = 72
        return Madden_Rating
    elif team  == "ATL":
        Madden_Rating = 81
        return Madden_Rating
    elif team  == "BAL":
        Madden_Rating = 87
        return Madden_Rating
    elif team  == "BUF":
        Madden_Rating = 90
        return Madden_Rating
    elif team == "CAR":
        Madden_Rating = 80
        return Madden_Rating
    elif team  == "CHI":
        Madden_Rating = 76
        return Madden_Rating
    elif team  == "CIN":
        Madden_Rating = 89
        return Madden_Rating
    elif team  == "CLE":
        Madden_Rating = 87
        return Madden_Rating
    elif team  == "DAL":
        Madden_Rating = 88
        return Madden_Rating
    elif team  == "DET":
        Madden_Rating = 86
        return Madden_Rating
    elif team  == "GB":
        Madden_Rating = 79
        return Madden_Rating
    elif team  == "HOU":
        Madden_Rating = 78
        return Madden_Rating
    elif team  == "IND":
        Madden_Rating = 77
        return Madden_Rating
    elif team  == "JAX":
        Madden_Rating = 84
        return Madden_Rating
    elif team  == "KC":
        Madden_Rating = 92
        return Madden_Rating
    elif team  == "LV":
        Madden_Rating = 79
        return Madden_Rating
    elif team  == "LAC":
        Madden_Rating = 85
        return Madden_Rating
    elif team  == "LAR":
        Madden_Rating = 73
        return Madden_Rating
    elif team  == "MIA":
        Madden_Rating = 86
        return Madden_Rating
    elif team  == "MIN":
        Madden_Rating = 85
        return Madden_Rating
    elif team  == "NE":
        Madden_Rating = 82
        return Madden_Rating
    elif team  == "NO":
        Madden_Rating = 82
        return Madden_Rating
    elif team  == "NYG":
        Madden_Rating = 82
        return Madden_Rating
    elif team  == "NYJ":
        Madden_Rating = 84
        return Madden_Rating
    elif team  == "PHI":
        Madden_Rating = 91
        return Madden_Rating
    elif team  == "PIT":
        Madden_Rating = 81
        return Madden_Rating
    elif team  == "SF":
        Madden_Rating = 86
        return Madden_Rating
    elif team  == "SEA":
        Madden_Rating = 83
        return Madden_Rating
    elif team  == "TB":
        Madden_Rating = 81
        return Madden_Rating
    elif team  == "TEN":
        Madden_Rating = 74
        return Madden_Rating
    elif team  == "WAS":
        Madden_Rating = 80
        return Madden_Rating

#Startup
print("Welcome to NFL Game Sim!!!")
team_1 = input("Please enter the abbreviation of the home team: ")
team_2 = input("Enter the abbreviation of the away team: ") 
scoring(team_1, team_2)
