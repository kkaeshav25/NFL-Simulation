import random
teams = {
    "ARI": {
        "QB": "Jacoby Brissett",
        "WR": ["Marvin Harrison Jr.", "Kendrick Bourne", "Michael Wilson", "Trey McBride"],
        "RB": ["Jeremiyah Love", "Tyler Allgeier"],
        "Secondary": ["Will Johnson", "Budda Baker", "Denzel Burke", "Garrett Williams"],
        "Rush": ["Josh Sweat", "Roy Lopez", "Mack Wilson Sr.", "Walter Nolen III", "Zaven Collins"]
    },
    "ATL": {
        "QB": "Michael Penix Jr.",
        "WR": ["Drake London", "Jahan Dotson", "Olamide Zaccheaus", "Kyle Pitts"],
        "RB": ["Bijan Robinson", "Brian Robinson Jr"],
        "Secondary": ["AJ Terrell", "Jessie Bates III", "Xavier Watts", "Mike Hughes"],
        "Rush": ["Brandon Dorlus", "Da'Shawn Hand", "Zach Harrison", "Divine Deablo", "James Pearce Jr."]
    },
    "BAL": {
        "QB": "Lamar Jackson",
        "WR": ["Zay Flowers", "Rashod Bateman", "Devontez Walker", "Mark Andrews"],
        "RB": ["Derrick Henry", "Justice Hill"],
        "Secondary": ["Marlon Humphrey", "Kyle Hamilton", "Nate Wiggins", "Malaki Starks"],
        "Rush": ["Nnamdi Madubuike", "Travis Jones", "Trey Hendrickson", "Roquan Smith", "John Jenkins"]
    },
    "BUF": {
        "QB": "Josh Allen",
        "WR": ["Khalil Shakir", "DJ Moore", "Joshua Palmer", "Dawson Knox"],
        "RB": ["James Cook", "Ty Johnson"],
        "Secondary": ["Christian Benford", "Maxwell Hairston", "Cole Bishop", "Geno Stone"],
        "Rush": ["Greg Rousseau", "Bradley Chubb", "TJ Sanders", "Ed Oliver"]
    },
    "CAR": {
        "QB": "Bryce Young",
        "WR": ["Tetairoa McMillan", "Jalen Coker", "Xavier Legette", "Tommy Tremble"],
        "RB": ["Chubba Hubbard", "Jonathon Brooks"],
        "Secondary": ["Mike Jackson", "Nick Scott", "Jaycee Horn", "Tre'von Moehrig"],
        "Rush": ["Derrick Brown", "Derrick Brown", "Bobby Brown III", "Devin Lloyd", "Jaelan Phillips"]
    },
    "CHI": {
        "QB": "Caleb Williams",
        "WR": ["Kalif Raymond", "Luther Burden III", "Rome Odunze", "Colston Loveland"],
        "RB": ["D'Andre Swift", "Kyle Monangai"],
        "Secondary": ["Jaylon Johnson", "Dillon Thieneman", "Coby Bryant", "Tyrique Stevenson"],
        "Rush": ["Grady Jarrett", "Devin Bush", "TJ Edwards", "Gervon Dexter Sr.", "Montez Sweat"]
    },
    "CIN": {
        "QB": "Joe Burrow",
        "WR": ["Ja'Marr Chase", "Tee Higgins", "Andrei Iosivas", "Mike Gesicki"],
        "RB": ["Chase Brown", "Samaje Perine"],
        "Secondary": ["Bryan Cook", "Jordan Battle", "Dax Hill", "DJ Turner II"],
        "Rush": ["Dexter Lawrence II", "Boye Mafe", "Jonathan Allen", "Myles Murphy", "Oren Burks"]
    },
    "CLE": {
        "QB": "Shedeur Sanders",
        "WR": ["KC Concepcion", "Jerry Jeudy", "Denzel Boston", "Harold Fannin Jr"],
        "RB": ["Quinshon Judkins", "Dylon Sampson"],
        "Secondary": ["Denzel Ward", "Ronnie Hickman", "Grant Delpit", "Tyson Campbell"],
        "Rush": ["Mason Graham", "Maliek Collins", "Carson Schwesinger", "Jared Verse"]
    },
    "DAL": {
        "QB": "Dak Prescott",
        "WR": ["CeeDee Lamb", "George Pickens", "Marquez Valdes-Scantling", "Jake Ferguson"],
        "RB": ["Javonte Williams", "Malik Davis"],
        "Secondary": ["DaRon Bland", "Caleb Downs", "Malik Hooker", "Cobie Durant"],
        "Rush": ["Quinnen Williams.", "DeMarvion Overshown", "Kenny Clark", "Rashan Gary"]
    },
    "DEN": {
        "QB": "Bo Nix",
        "WR": ["Courtland Sutton", "Jaylen Waddle", "Marvin Mims Jr.", "Evan Engram"],
        "RB": ["RJ Harvey", "JK Dobbins"],
        "Secondary": ["Talanoa Hufanga", "Brandon Jones", "Riley Moss", "Pat Surtain II"],
        "Rush": ["Zach Allen", "Alex Singleton", "Nik Bonitto", "Jonathon Cooper", "DJ Jones"]
    },
    "DET": {
        "QB": "Jared Goff",
        "WR": ["Amon-Ra St. Brown", "Jameson Williams", "ISaac TeSlaa", "Sam LaPorta"],
        "RB": ["Jahmyr Gibbs", "Isiah Pacheco"],
        "Secondary": ["Terrion Arnold", "DJ Reed", "Brian Branch", "Kerby Joseph"],
        "Rush": ["Aidan Hutchinson", "Jack Campbell", "Derrick Moore", "Derrick Barnes", "Alim McNeill"]
    },
    "GB": {
        "QB": "Jordan Love",
        "WR": ["Matthew Golden", "Christian Watson", "Jayden Reed", "Tucker Kraft"],
        "RB": ["Josh Jacobs", "Chris Brooks"],
        "Secondary": ["Keisean Nixon", "Xavier McKinney", "Javon Bullard", "Evan Williams"],
        "Rush": ["Lukas Van Ness", "Micah Parsons", "Edgerrin Cooper", "Javon Hargrave", "Devonte Wyatt"]
    },
    "HOU": {
        "QB": "CJ Stroud",
        "WR": ["Jayden Higgins", "Nico Collins", "Tank Dell", "Dalton Schultz"],
        "RB": ["David Montgomery", "Woody Marks"],
        "Secondary": ["Kamari Lassiter", "Jalen Pitre", "Calen Bullock", "Derek Stingley Jr."],
        "Rush": ["Will Anderson Jr.", "EJ Speed", "Azeez-Al-Shaair", "Sheldon Rankins", "Danielle Hunter"]
    },
    "IND": {
        "QB": "Daniel Jones",
        "WR": ["Nick Westbrook-Ikhine", "Josh Downs", "Alec Pierce", "Tyler Warren"],
        "RB": ["Jonathon Taylor", "DJ Giddens"],
        "Secondary": ["Charvarius Ward", "Sauce Gardner", "Cam Bynum", "Justin Walley"],
        "Rush": ["CJ Allen", "Laiatu Latu", "JT Tuimoloau", "Grover Stewart", "DeForest Buckner"]
    },
    "JAX": {
        "QB": "Trevor Lawrence",
        "WR": ["Jakobi Meyers", "Parker Washington", "Brian Thomas Jr.", "Brenton Strange"],
        "RB": ["Chris Rodriguez Jr.", "Bhayshul Tuten"],
        "Secondary": ["Travis Hunter", "Eric Murray", "Jourdan Lewis", "Antonio Johnson"],
        "Rush": ["Arik Armstead", "Josh Hines-Allen", "Travon Walker", "Jack Kiser", "DaVon Hamilton"]
    },
    "KC": {
        "QB": "Patrick Mahomes",
        "WR": ["Rashee Rice", "Tyquan Thornton", "Xavier Worthy", "Travis Kelce"],
        "RB": ["Kenneth Walker III", "Emmett Johnson"],
        "Secondary": ["Chamarri Conner", "Alohi Gilman", "Mansoor Delane", "Nohl Williams"],
        "Rush": ["George Karlaftis", "Drue Tranquill", "Nick Bolton", "Chris Jones"]
    },
    "LV": {
        "QB": "Fernando Mendoza",
        "WR": ["Tre Tucker", "Jalen Nailor", "Jack Bech", "Brock Bowers"],
        "RB": ["Ashton Jeanty", "Mike Washington Jr"],
        "Secondary": ["Eric Stokes", "Jeremy Chinn", "Taron Johnson", "Jermod McCoy"],
        "Rush": ["Maxx Crosby", "Quay Walker", "Kwity Paye", "Adam Butler"]
    },
    "LAC": {
        "QB": "Justin Herbert",
        "WR": ["Tre Harris", "Quentin Johnston", "Ladd McConkey", "Oronde Gadsden"],
        "RB": ["Omarion Hampton", "Keaton Mitchell"],
        "Secondary": ["Donte Jackson", "Elijah Molden", "Derwin James Jr.", "Cam Hart"],
        "Rush": ["Teair Tart", "Dalvin Tomlinson", "Denzel Perryman", "Khalil Mack", "Jamaree Caldwell"]
    },
    "LAR": {
        "QB": "Matthew Stafford",
        "WR": ["Davante Adams", "Puka Nacua", "Jordan Whittington", "Colby Parkinson"],
        "RB": ["Kyren Williams", "Blake Corum"],
        "Secondary": ["Trent McDuffie", "Kam Curl", "Kamren Curl", "jaylen Watson"],
        "Rush": ["Braden Fiske", "Myles Garrett", "Byron Young", "Poona Ford", "Kobie Turner"]
    },
    "MIA": {
        "QB": "Malik Willis",
        "WR": ["Malik Washington", "Jalen Tolbert", "Tutu Atwell", "Greg Dulcich"],
        "RB": ["De'Von Achane", "Jaylen Wright"],
        "Secondary": ["Storm Duck","Marco Wilson", "Chris Johnson" "Lonnie Johnson Jr"],
        "Rush": ["Zach Sieler", "Chop Robinson", "Kenneth Grant", "Josh Uche", "Willie Gay Jr"]
    },
    "MIN": {
        "QB": "Kyler Murray",
        "WR": ["Justin Jefferson", "Jordan Addison", "Jauan Jennings", "TJ Hockenson"],
        "RB": ["Aaron Jones", "Jordan Mason"],
        "Secondary": ["Isiah Rodgers", "Byron Murphy Jr", "Josh Metellus", "Theo Jackson"],
        "Rush": ["Caleb Banks", "Eric Wilson", "Andrew Van Ginkel", "Blake Cashman", "Jalen Redmond"]
    },
    "NE": {
        "QB": "Drake Maye",
        "WR": ["AJ Brown", "Romeo Doubs", "Kayshon Boutte", "Hunter Henry"],
        "RB": ["Rhamondre Stevenson", "TreyVeyon Henderson"],
        "Secondary": ["Carlton Davis III", "Marcus Jones", "Kevin Byard", "Christian Gonzalez"],
        "Rush": ["Harold Landry III","Robert Spillane", "Christian Elliss", "Christian Barmore"]
    },
    "NO": {
        "QB": "Tyler Shough",
        "WR": ["Chris Olave", "Jordyn Tyson", "Devaughn Vele", "Juwan Johnson"],
        "RB": ["Alvin Kamara", "Travis Etienne Jr"],
        "Secondary": ["Kool-Aid McKinstry", "Julian Blackmon", "Justin Reid", "Quincy Riley"],
        "Rush": ["Vernon Broughton", "Kaden Elliss", "Chase Young", "Pete Werner", "Davon Godchaux"]
    },
    "NYG": {
        "QB": "Jaxson Dart",
        "WR": ["Malik Nabers", "Darius Slayton", "Darnell Mooney", "Isaiah Likely"],
        "RB": ["Cam Skattebo", "Tyrone Tracy Jr."],
        "Secondary": ["Paulson Adebo", "Jevon Holland", "Greg Newsome II"],
        "Rush": ["DJ Reader", "Arvelle Reese", "Brian Burns", "Kayvon Thibodeaux", "Abdul Carter"]
    },
    "NYJ": {
        "QB": "Geno Smith",
        "WR": ["Garrett Wilson", "Adonai Mitchell", "Omar Cooper Jr", "Kenyon Sadiq"],
        "RB": ["Breece Hall", "Braelon Allen"],
        "Secondary": ["Minkah Fitzpatrick", "Andre Cisco", "Brandon Stephens", "Nahshon Wright"],
        "Rush": ["Demario Davis", "Harrison Phillips", "Will McDonald IV", "David Bailey"]
    },
    "PHI": {
        "QB": "Jalen Hurts",
        "WR": ["Makai Lemon", "DeVonta Smith", "Dontayvion Wicks", "Dallas Goedert"],
        "RB": ["Saquon Barkley", "Tank Bigsby"],
        "Secondary": ["Quinyon Mitchell", "Cooper DeJean", "Marcus Epps", "Riq Woolen"],
        "Rush": ["Jordan Davis", "Jonathan Greenard", "Zack Baun", "Nolan Smith", "Jalen Carter"]
    },
    "PIT": {
        "QB": "Aaron Rodgers",
        "WR": ["DK Metcalf", "Michael Pittman Jr", "Roman Wilson", "Pat Freiermuth"],
        "RB": ["Rico Dowdle", "Jaylen Warren"],
        "Secondary": ["Jalen Ramsey", "Jamel Dean", "DeShon Elliott", "Joey Porter Jr."],
        "Rush": ["Derrick Harmon", "TJ Watt", "Patrick Queen", "Alex Highsmith", "Cameron Heyward"]
    },
    "SF": {
        "QB": "Brock Purdy",
        "WR": ["Ricky Pearsall", "Mike Evans", "Christian Kirk", "George Kittle"],
        "RB": ["Christian McCaffrey", "Jordan James"],
        "Secondary": ["Malik Mustapha", "Renardo Green", "Ji'Ayir Brown", "Deommodore Lenoir"],
        "Rush": ["Dre Greenlaw", "CJ West", "Fred Warner", "Mykel Williams", "Nick Bosa"]
    },
    "SEA": {
        "QB": "Sam Darnold",
        "WR": ["Cooper Kupp", "Rashid Shaheed", "Jaxon Smith-Njigba", "AJ Barner"],
        "RB": ["Jadarian Price", "Zach Charbonnet"],
        "Secondary": ["Devon Witherspoon", "Julian Love", "Josh Jobe", "Mick Emmanwori"],
        "Rush": ["Byron Murphy II", "DeMarcus Lawrence", "Uchenna Nwosu", "Leonard Williams"]
    },
    "TB": {
        "QB": "Baker Mayfield",
        "WR": ["Jalen McMillan", "Chris Godwin", "Emeka Egbuka", "Cade Otton"],
        "RB": ["Kenneth Gainwell", "Bucky Irving"],
        "Secondary": ["Benjamin Morrison", "Antoine Winfield Jr.", "Tykee Smith", "Zyon McCollum"],
        "Rush": ["Vita Vea", "Rueben Bain Jr", "Alex Anzalone", "Yaya Diaby", "Elijah Roberts"]
    },
    "TEN": {
        "QB": "Cam Ward",
        "WR": ["Calvin Ridley", "Carnell Tate", "Wan'Dale Robinson", "Gunnar Helm"],
        "RB": ["Tony Pollard", "Tyjae Spears"],
        "Secondary": ["Amani Hooker", "Alontae Taylor", "Kevin Winston Jr", "Marcus Harris"],
        "Rush": ["John Franklin-Meyers", "Cody Barton", "Jermaine Johnson II", "Jeffrey Simmons"]
    },
    "WAS": {
        "QB": "Jayden Daniels",
        "WR": ["Terry McLaurin", "Luke McCaffrey", "Dyami Brown", "Chig Okonkwo"],
        "RB": ["Jacory Croskey-Merritt", "Rachaad White"],
        "Secondary": ["Amik Robertson", "Nick Cross", "Trey Amos", "Mike Sainristil"],
        "Rush": ["Javon Kinlaw", "Sonny Styles", "Odae Oweh", "Daron Payne", "Leo Chenal"]
    }
}

def choose_player(team, position): #Generates players for each team; QB, WR, and RB
    if(position == "QB"):
        return (teams[team][position])
    else:
        return random.choice(teams[team][position])