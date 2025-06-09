import random
teams = {
    "ARI": {
        "QB": "Kyler Murray",
        "WR": ["Marvin Harrison Jr.", "Greg Dortch", "Michael Wilson", "Trey McBride"],
        "RB": ["James Conner", "Trey Benson"],
        "Secondary": ["Will Johnson", "Budda Baker", "Jalen Thompson", "Garrett Williams"],
        "Rush": ["Josh Sweat", "Kyzir White", "Mack Wilson Sr.", "BJ Ojulari", "Bilal Nichols"]
    },
    "ATL": {
        "QB": "Michael Penix Jr.",
        "WR": ["Drake London", "Darnell Mooney", "Ray-Ray McCloud III", "Kyle Pitts"],
        "RB": ["Bijan Robinson", "Tyler Allgeier"],
        "Secondary": ["AJ Terrell", "Jessie Bates III", "Jordan Fuller", "Dee Alford"],
        "Rush": ["Morgan Fox", "Kaden Elliss", "Leonard Floyd", "David Onyemata", "James Pearce Jr."]
    },
    "BAL": {
        "QB": "Lamar Jackson",
        "WR": ["Zay Flowers", "Rashod Bateman", "DeAndre Hopkins", "Mark Andrews"],
        "RB": ["Derrick Henry", "Justice Hill"],
        "Secondary": ["Marlon Humphrey", "Kyle Hamilton", "Chidobe Awuzie", "Malaki Starks"],
        "Rush": ["Nnamdi Madubuike", "Travis Jones", "Kyle Van Noy", "Roquan Smith", "Odafe Oweh"]
    },
    "BUF": {
        "QB": "Josh Allen",
        "WR": ["Khalil Shakir", "Joshua Palmer", "Keon Coleman", "Dawson Knox"],
        "RB": ["James Cook", "Ray Davis"],
        "Secondary": ["Christian Benford", "Maxwell Hairston", "Taylor Rapp", "Taron Johnson"],
        "Rush": ["Greg Rousseau", "Matt Milano", "Joey Bosa", "DaQuan Jones", "Ed Oliver"]
    },
    "CAR": {
        "QB": "Bryce Young",
        "WR": ["Tetairoa McMillan", "Adam Theieln", "Xavier Legette", "Tommy Tremble"],
        "RB": ["Chubba Hubbard", "Rico Dowdle"],
        "Secondary": ["Michael Jackson", "Nick Scott", "Jaycee Horn", "Tre'von Moehrig"],
        "Rush": ["A'Shawn Robinson", "Derrick Brown", "Bobby Brown III", "Tershawn Wharton", "Shy Tuttle"]
    },
    "CHI": {
        "QB": "Caleb Williams",
        "WR": ["DJ Moore", "Luther Burden III", "Rome Odunze", "Cole Kmet"],
        "RB": ["D'Andre Swift", "Roschon Johnson"],
        "Secondary": ["Jaylon Johnson", "Kevin Byard III", "Jaquan Brisker", "Tyrique Stevenson"],
        "Rush": ["Grady Jarrett", "Tremaine Edmunds", "TJ Edwards", "Gervon Dexter Sr.", "Montez Sweat"]
    },
    "CIN": {
        "QB": "Joe Burrow",
        "WR": ["Ja'Marr Chase", "Tee Higgins", "Andrei Iosivas", "Mike Gesicki"],
        "RB": ["Zack Moss", "Chase Brown"],
        "Secondary": ["Cam Taylor-Britt", "Geno Stone", "Dax Hill", "DJ Turner II"],
        "Rush": ["Joseph Ossai", "Logan Wilson", "Shemar Stewart", "Trey Hendrickson", "BJ Hill"]
    },
    "CLE": {
        "QB": "Joe Flacco",
        "WR": ["Cedric Tillman", "Jerry Jeudy", "Dionate Johnson", "David Njoku"],
        "RB": ["Jerome Ford", "Quinshon Judkins"],
        "Secondary": ["Denzel Ward", "Ronnie Hickman", "Grant Delpit", "Greg Newsome II"],
        "Rush": ["Mason Graham", "Maliek Collins", "Isaiah McGuire", "Jordan Hicks", "Myles Garrett"]
    },
    "DAL": {
        "QB": "Dak Prescott",
        "WR": ["CeeDee Lamb", "George Pickens", "Jalen Tolbert", "Jake Ferguson"],
        "RB": ["Javonte Williams", "Miles Sanders"],
        "Secondary": ["DaRon Bland", "Donovan Wilson", "Malik Hooker", "Trevon Diggs"],
        "Rush": ["Dante Fowler Jr.", "DeMarvion Overshown", "Mazi Smith", "Micah Parsons"]
    },
    "DEN": {
        "QB": "Bo Nix",
        "WR": ["Courtland Sutton", "Devaughn Vele", "Marvin Mims Jr.", "Evan Engram"],
        "RB": ["RJ Harvey", "Audric Estime"],
        "Secondary": ["Talanoa Hufanga", "Brandon Jones", "Riley Moss", "Pat Surtain II"],
        "Rush": ["Zach Allen", "Alex Singleton", "Nik Bonitto", "Dre Greenlaw", "DJ Jones"]
    },
    "DET": {
        "QB": "Jared Goff",
        "WR": ["Amon-Ra St. Brown", "Jameson Williams", "Tim Patrick", "Sam LaPorta"],
        "RB": ["David Montgomery", "Jahmyr Gibbs"],
        "Secondary": ["Terrion Arnold", "DJ Reed", "Brian Branch", "Kerby Joseph"],
        "Rush": ["Aiden Hutchinson", "Jack Campbell", "Alex Anzalone", "Derrick Barnes", "Alim McNeill"]
    },
    "GB": {
        "QB": "Jordan Love",
        "WR": ["Matthew Golden", "Romeo Doubs", "Jayden Reed", "Tucker Kraft"],
        "RB": ["Josh Jacobs", "MarShawn Lloyd"],
        "Secondary": ["Keisan Nixon", "Xavier McKinney", "Javon Bullard", "Evan Williams"],
        "Rush": ["Lukas Van Ness", "Quay Walker", "Edgerrin Cooper", "Rashan Gary", "Kenny Clark"]
    },
    "HOU": {
        "QB": "CJ Stroud",
        "WR": ["Christian Kirk", "Nico Collins", "Tank Dell", "Dalton Schultz"],
        "RB": ["Joe Mixon", "Nick Chubb"],
        "Secondary": ["CJ Gardner-Johnson", "Jalen Pitre", "Calen Bullock", "Derek Stingley Jr."],
        "Rush": ["Will Anderson Jr.", "Denico Autry", "Azeez-Al-Shaair", "Tim Settle Jr.", "Danielle Hunter"]
    },
    "IND": {
        "QB": "Anthony Richardson",
        "WR": ["Michael Pittman Jr.", "Josh Downs", "Alec Pierce", "Tyler Warren"],
        "RB": ["Jonathon Taylor", "Khalil Herbert"],
        "Secondary": ["Charvarius Ward", "Nick Cross", "Camryn Bynum", "Kenny Moore II"],
        "Rush": ["Kwity Paye", "Laiatu Latu", "Zaire Franklin", "Grover Stewart", "DeForest Buckner"]
    },
    "JAX": {
        "QB": "Trevor Lawrence",
        "WR": ["Travis Hunter", "Dyami Brown", "Brian Thomas Jr.", "Brenton Strange"],
        "RB": ["Travis Etienne Jr.", "Tank Bigsby"],
        "Secondary": ["Travis Hunter", "Darnell Savage", "Jourdan Lewis", "Tyson Campbell"],
        "Rush": ["Arik Armstead", "Josh Allen", "Travon Walker", "Devin Lloyd", "DaVon Hamilton"]
    },
    "KC": {
        "QB": "Patrick Mahomes",
        "WR": ["Rashee Rice", "Marquise Brown", "Xavier Worthy", "Travis Kelce"],
        "RB": ["Isiah Pacheco", "Kareem Hunt"],
        "Secondary": ["Trent McDuffie", "Bryan Cook", "Jayden Hicks", "Kristian Fulton"],
        "Rush": ["George Karlaftis", "Mike Danna", "Nick Bolton", "Leo Chenal", "Chris Jones"]
    },
    "LV": {
        "QB": "Geno Smith",
        "WR": ["Tre Tcuker", "Jakobi Meyers", "Jack Bech", "Brock Bowers"],
        "RB": ["Ashton Jeanty", "Raheem Mostert"],
        "Secondary": ["Eric Stokes", "Jeremy Chinn", "Darnay Holmes", "Elandon Roberts"],
        "Rush": ["Maxx Crosby", "Chrstian Wilkins", "Devin White", "Elandon Roberts"]
    },
    "LAC": {
        "QB": "Justin Herbert",
        "WR": ["Mike Williams", "Quentin Johnston", "Ladd McConkey", "Will Dissly"],
        "RB": ["Najee Harris", "Omarion Hampton"],
        "Secondary": ["Donte Jackson", "Alohi Gilman", "Derwin James Jr.", "Cam Hart"],
        "Rush": ["Teair Tart", "Junior Colson", "Denzel Perryman", "Khalil Mack", "Da'Shawn Hand"]
    },
    "LAR": {
        "QB": "Matthew Stafford",
        "WR": ["Davante Adams", "Puka Nacua", "Tutu Atwell", "Tyler Higbee"],
        "RB": ["Kyren Williams", "Blake Corum"],
        "Secondary": ["Quentin Lake", "Ahkello Witherspoon", "Kamren Curl", "Darious Williams"],
        "Rush": ["Braden Fiske", "Jared Verse", "Byron Young", "Troy Reeder", "Kobie Turner"]
    },
    "MIA": {
        "QB": "Tua Tagovailoa",
        "WR": ["Tyreek Hill", "Jaylen Waddle", "Nick Westbrook-Ikhine", "Jonnu Smith"],
        "RB": ["Jaylen Wright", "De'Von Achane"],
        "Secondary": ["Storm Duck","Ifeatu Melifonwu", "Ashtyn Davis" "Jalen Ramsey"],
        "Rush": ["Zach Sieler", "Neville Gallimore", "Calais Campbell", "Jaelen Phillips", "Bradley Chubb"]
    },
    "MIN": {
        "QB": "JJ McCarthy",
        "WR": ["Justin Jefferson", "Jordan Addison", "Jalen Nailor", "TJ Hockenson"],
        "RB": ["Aaron Jones", "Jordan Mason"],
        "Secondary": ["Isiah Rodgers", "Mekhi Blackmon", "Harrison Smith", "Byron Murphy Jr."],
        "Rush": ["Jonathan Allen", "Ivan Pace Jr.", "Andrew Van Ginkel", "Javon Hargrave", "Harrison Phillips"]
    },
    "NE": {
        "QB": "Drake Maye",
        "WR": ["Stefon Diggs", "DeMario Douglas", "Mack Hollins", "Hunter Henry"],
        "RB": ["Rhamondre Stevenson", "Antonio Gibson"],
        "Secondary": ["Carlton Davis III", "Jabrill Peppers", "Kyle Dugger", "Christian Gonzalez"],
        "Rush": ["Harold Landry III","Robert Spillane", "Josh Uche", "Christian Barmore"]
    },
    "NO": {
        "QB": "Tyler Shough",
        "WR": ["Chris Olave", "Rashid Shaheed", "Brandin Cooks", "Juwan Johnson"],
        "RB": ["Alvin Kamara", "Kendre Miller"],
        "Secondary": ["Kool-Aid McKinstry", "Tyrann Mathieu", "Justin Reid", "Alontae Taylor"],
        "Rush": ["Cameron Jordan", "Khalen Saunders", "Chase Young", "Demario Davis", "Davon Godchaux"]
    },
    "NYG": {
        "QB": "Russell Wilson",
        "WR": ["Malik Nabers", "Darius Slayton", "Wan'Dale Robinson", "Theo Johnson"],
        "RB": ["Devin Singletary", "Tyrone Tracy Jr."],
        "Secondary": ["Paulson Adebo", "Jevon Holland", "Deontae Banks"],
        "Rush": ["DJ Davidson", "Dexter Lawrence II", "Brian Burns", "Kayvon Thibodeaux", "Abdul Carter"]
    },
    "NYJ": {
        "QB": "Justin Fields",
        "WR": ["Garrett Wilson", "Josh Reynolds", "Allen Lazard", "Mason Taylor"],
        "RB": ["Breece Hall", "Braelon Allen"],
        "Secondary": ["Sauce Gardner", "Andre Cisco", "Tony Adams", "Michael Carter II"],
        "Rush": ["Jermaine Johnson", "Derrick Nnadi", "Will McDonald IV", "Quincy Williams", "Quinnen Williams"]
    },
    "PHI": {
        "QB": "Jalen Hurts",
        "WR": ["AJ Brown", "DeVonta Smith", "Jahan Dotson", "Dallas Goedert"],
        "RB": ["Saquon Barkley", "Will Shipley"],
        "Secondary": ["Quinyon Mitchell", "Cooper DeJean", "Reed Blankenship", "Kelee Ringo"],
        "Rush": ["Jordan Davis", "Nakobe Dean", "Zack Baun", "Nolan Smith", "Jalen Carter"]
    },
    "PIT": {
        "QB": "Aaron Rodgers Wilson",
        "WR": ["DK Metcalf", "Robert Woods", "Roman Wilson", "Pat Freiermuth"],
        "RB": ["Kaleb Johnson", "Jaylen Warren"],
        "Secondary": ["Darius Slay Jr.", "Minkah Fitzpatrick", "DeShon Elliott", "Beanie Bishop Jr."],
        "Rush": ["Derrick Harmon", "TJ Watt", "Patrick Queen", "Alex Highsmith", "Cameron Heyward"]
    },
    "SF": {
        "QB": "Brock Purdy",
        "WR": ["Ricky Pearsall", "Brandon Aiyuk", "Jauan Jennings", "George Kittle"],
        "RB": ["Christian McCaffrey", "Isaac Gurendo"],
        "Secondary": ["Jason Pinnock", "Renardo Green", "Ji'Ayir Brown", "Deommodore Lenoir"],
        "Rush": ["Nick Martin", "Bryce Huff", "Fred Warner", "Mykel Williams", "Nick Bosa"]
    },
    "SEA": {
        "QB": "Sam Darnold",
        "WR": ["Cooper Kupp", "Marquez Valdes-Scantling", "Jaxon Smith-Njigba", "Noah Fant"],
        "RB": ["Kenneth Walker III", "Zach Charbonnet"],
        "Secondary": ["Devon Witherspoon", "Julian Love", "Josh Jobe", "Riq Woolen"],
        "Rush": ["Byron Murphy II", "DeMarcus Lawrence", "Jarran Reed", "Leonard Williams"]
    },
    "TB": {
        "QB": "Baker Mayfield",
        "WR": ["Mike Evans", "Chris Godwin", "Emeka Egbuka", "Cade Otton"],
        "RB": ["Rachaad White", "Bucky Irving"],
        "Secondary": ["Jamel Dean", "Antoine Winfield Jr.", "Tykee Smith", "Zyon McCollum"],
        "Rush": ["Vita Vea", "Anthony Walker Jr.", "Lavonte David", "Calijah Kancey", "Logan Hall"]
    },
    "TEN": {
        "QB": "Cam Ward",
        "WR": ["Calvin Ridley", "Tyler Lockett", "Treylon Burks", "Chig Okonkwo"],
        "RB": ["Tony Pollard", "Tyjae Spears"],
        "Secondary": ["Xavier Woods", "Roger McCreary", "Amani Hooker", "L'Jarius Sneed"],
        "Rush": ["Sebastian Joseph-Day", "Cody Barton", "Arden Key", "Jeffrey Simmons"]
    },
    "WAS": {
        "QB": "Jayden Daniels",
        "WR": ["Terry McLaurin", "Deebo Samuel", "Noah Brown", "Zach Ertz"],
        "RB": ["Austin Ekeler", "Brian Robinson Jr."],
        "Secondary": ["Noah Igbinoghene.", "Will Harris", "Marshon Lattimore", "Mike Sainristil"],
        "Rush": ["Javon Kinlaw.", "Bobby Wagner", "Jamin Davis", "Daron Payne", "Jonathan Allen"]
    }
}

def choose_player(team, position): #Generates players for each team; QB, WR, and RB
    if(position == "QB"):
        return (teams[team][position])
    else:
        return random.choice(teams[team][position])