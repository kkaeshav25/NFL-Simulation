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
        "QB": "Kirk Cousins",
        "WR": ["Drake London", "Darnell Mooney", "Rondale Moore", "Kyle Pitts"],
        "RB": ["Bijan Robinson", "Tyler Allgeier"],
        "Secondary": ["AJ Terrell", "Jessie Bates III", "DeMarcco Hellams", "Clark Phillips III"],
        "Rush": ["Zach Harrison", "KAden Elliss", "Arnold Ebiketie", "Troy Andersen", "Grady Jarrett"]
    },
    "BAL": {
        "QB": "Lamar Jackson",
        "WR": ["Zay Flowers", "Rashod Bateman", "Nelson Agholor", "Mark Andrews"],
        "RB": ["Derrick Henry", "Justice Hill"],
        "Secondary": ["Marlon Humphrey", "Kyle Hamilton", "Marcus Williams", "Brandon Stephens"],
        "Rush": ["Justin Madubuike", "Odafe Oweh", "Kyle Van Noy", "Roquan Smith", "Michael Pierce"]
    },
    "BUF": {
        "QB": "Josh Allen",
        "WR": ["Khalil Shakir", "Marquez Valdes-Scantling", "Keon Coleman", "Dawson Knox"],
        "RB": ["James Cook", "Ray Davis"],
        "Secondary": ["Rasul Douglas", "Mike Edwards", "Taylor Rapp", "Taron Johnson"],
        "Rush": ["Greg Rousseau", "Matt Milano", "Nicholas Morrow", "Von Miller", "Ed Oliver"]
    },
    "CAR": {
        "QB": "Bryce Young",
        "WR": ["Diontae Johnson", "Adam Theieln", "Xavier Legette", "Tommy Tremble"],
        "RB": ["Chubba Hubbard", "Jonathon Brooks"],
        "Secondary": ["Dane Jackson", "Xavier Woods", "Jordan Fuller", "Jaycee Horn"],
        "Rush": ["A'Shawn Robinson", "Shaq Thompson", "Jadeveon Clowney", "Dane Jackson", "Shy Tuttle"]
    },
    "CHI": {
        "QB": "Caleb Williams",
        "WR": ["DJ Moore", "Keenan Allen", "Rome Odunze", "Cole Kmet"],
        "RB": ["D'Andre Swift", "Khalil Herbert"],
        "Secondary": ["Jaylon Johnson", "Kevin Byard III", "Jaquan Brisker", "Tyrique Stevenson"],
        "Rush": ["DeMarcus Walker", "Tremaine Edmunds", "TJ Edwards", "Jack Sanborn", "Montez Sweat"]
    },
    "CIN": {
        "QB": "Joe Burrow",
        "WR": ["Ja'Marr Chase", "Tee Higgins", "Jermaine Burton", "Mike Gesicki"],
        "RB": ["Zack Moss", "Chase Brown"],
        "Secondary": ["Cam Taylor-Britt", "Geno Stone", "Vonn Bell", "DJ Turner II"],
        "Rush": ["Sam Hubbard", "Logan Wilson", "Germaine Pratt", "Trey Hendrickson", "BJ Hill"]
    },
    "CLE": {
        "QB": "Deshaun Watson",
        "WR": ["Amari Cooper", "Jerry Jeudy", "Elijah Moore", "David Njoku"],
        "RB": ["Nick Chubb", "Jerome Ford"],
        "Secondary": ["Denzel Ward", "Juan Thornhill", "Grant Delpit", "Greg Newsome II"],
        "Rush": ["Za'Darius Smith", "Devin Bush", "Jeremiah Owusu-Koramoah", "Jordan Hicks", "Myles Garrett"]
    },
    "DAL": {
        "QB": "Dak Prescott",
        "WR": ["CeeDee Lamb", "Brandin Cooks", "Jalen Tolbert", "Jake Ferguson"],
        "RB": ["Ezekiel Elliot", "Rico Dowdle"],
        "Secondary": ["DaRon Bland", "Donovan Wilson", "Malik Hooker", "Trevon Diggs"],
        "Rush": ["DeMarcus Lawrence", "Damone Clark", "Eric Kendricks", "Micah Parsons"]
    },
    "DEN": {
        "QB": "Bo Nix",
        "WR": ["Courtland Sutton", "Josh Reynolds", "Marvin Mims Jr.", "Adam Trautman"],
        "RB": ["Javonte Williams", "Samaje Perine"],
        "Secondary": ["Levi Wallace", "Brandon Jones", "Caden Sterns", "Pat Surtain II"],
        "Rush": ["Zach Allen", "Alex Singleton", "Cody Barton", "Johnathon Cooper", "DJ Jones"]
    },
    "DET": {
        "QB": "Jared Goff",
        "WR": ["Amon-Ra St. Brown", "Jameson Williams", "Kalif Raymond", "Sam LaPorta"],
        "RB": ["David Montgomery", "Jahmyr Gibbs"],
        "Secondary": ["Terrion Arnold", "Carlton Davis III", "Brian Branch", "Kerby Joseph"],
        "Rush": ["Aiden Hutchinson", "Jack Campbell", "Alex Anzalone", "Derrick Barnes", "DJ Reader"]
    },
    "GB": {
        "QB": "Jordan Love",
        "WR": ["Christian Watson", "Romeo Doubs", "Jayden Reed", "Luke Musgrave"],
        "RB": ["Josh Jacobs", "AJ Dillon"],
        "Secondary": ["Jaire Alexander", "Xavier McKinney", "Javon Bullard", "Eric Stokes"],
        "Rush": ["Preston Smith", "Quay Walker", "Edgerrin Cooper", "Isiah McDuffie", "Kenny Clark"]
    },
    "HOU": {
        "QB": "CJ Stroud",
        "WR": ["Stefon Diggs", "Nico Collins", "Tank Dell", "Dalton Schultz"],
        "RB": ["Joe Mixon", "Dameon Pierce"],
        "Secondary": ["Jeff Okudah", "Jalen Pitre", "Jimmie Ward", "Derek Stingley Jr."],
        "Rush": ["Will Anderson Jr.", "Denico Autry", "Christian Harris", "Derek Barnett", "Danielle Hunter"]
    },
    "IND": {
        "QB": "Anthony Richardson",
        "WR": ["Michael Pittman Jr.", "Josh Downs", "Adonai Mitchell", "Jelani Woods"],
        "RB": ["Jonathon Taylor", "Trey Sermon"],
        "Secondary": ["Jaylin Simpson", "Nick Cross", "Julian Blackmon", "Kenny Moore II"],
        "Rush": ["Kwity Paye", "EJ Speed", "Zaire Franklin", "Samson Ebukam", "DeForest Buckner"]
    },
    "JAX": {
        "QB": "Trevor Lawrence",
        "WR": ["Christian Kirk", "Gabe Davis", "Brian Thomas Jr.", "Evan Engram"],
        "RB": ["Travis Etienne Jr.", "Tank Bigsby"],
        "Secondary": ["Ronald Darby", "Terrell Edmunds", "Andre Cisco", "Tyson Campbell"],
        "Rush": ["Arik Armstead", "Josh Allen", "Travon Walker", "Devin Lloyd", "DaVon Hamilton"]
    },
    "KC": {
        "QB": "Patrick Mahomes",
        "WR": ["Rashee Rice", "Marquise Brown", "Xavier Worthy", "Travis Kelce"],
        "RB": ["Isiah Pacheco", "Clyde Edwards-Helaire"],
        "Secondary": ["Trent McDuffie", "Bryan Cook", "Justin Reid", "Jaylen Watson"],
        "Rush": ["George Karlaftis", "Mike Danna", "Nick Bolton", "Derrick Nnadi", "Chris Jones"]
    },
    "LV": {
        "QB": "Aiden O'Connell",
        "WR": ["Davante Adams", "Jakobi Mayers", "Michael Gallup", "Brock Bowers"],
        "RB": ["Zamir White", "Alexander Mattison"],
        "Secondary": ["Jack Jones", "Marcus Epps", "Tre'von Moehrig", "Nate Hobbs"],
        "Rush": ["Maxx Crosby", "Chrstian Wilkins", "Ropert Spillane", "Divine Deablo", "John Jenkins"]
    },
    "LAC": {
        "QB": "Justin Herbert",
        "WR": ["Joshua Palmer", "Quentin Johnston", "Ladd McConkey", "Will Dissly"],
        "RB": ["Gus Edwards", "JK Dobbins"],
        "Secondary": ["Asante Samuel Jr.", "Alohi Gilman", "Derwin James Jr.", "Kristian Fulton"],
        "Rush": ["Poona Ford", "Junior Colson", "Denzel Perryman", "Khalil Mack", "Joey Bosa"]
    },
    "LAR": {
        "QB": "Matthew Stafford",
        "WR": ["Cooper Kupp", "Puka Nacua", "Demarcus Robinson", "Tyler Higbee"],
        "RB": ["Kyren Williams", "Blake Corum"],
        "Secondary": ["Tre'Davious White", "Russ Yeast", "Kamren Curl", "Darious Williams"],
        "Rush": ["Braden Fiske", "Jared Verse", "Byron Young", "Troy Reeder", "Kobie Turner"]
    },
    "MIA": {
        "QB": "Tua Tagovailoa",
        "WR": ["Tyreek Hill", "Jaylen Waddle", "Odell Beckham Jr.", "Jonnu Smith"],
        "RB": ["Raheem Mostert", "De'Von Achane"],
        "Secondary": ["Kendall Fuller", "Jevon Holland", "Jordan Poyer", "Jalen Ramsey"],
        "Rush": ["Zach Sieler", "Neville Gallimore", "Calais Campbell", "Jaelen Phillips", "Bradley Chubb"]
    },
    "MIN": {
        "QB": "JJ McCarthy",
        "WR": ["Justin Jefferson", "Jordan Addison", "Brandon Powell", "TJ Hockenson"],
        "RB": ["Aaron Jones", "Ty Chandler"],
        "Secondary": ["Akayleb Evans", "Camryn Bynum", "Harrison Smith", "Byron Murphy Jr."],
        "Rush": ["Jerry Tillery", "Blake Cashman", "Andrew Van Ginkel", "Kamu Gruiger-Hill", "Harrison Phillips"]
    },
    "NE": {
        "QB": "Drake Maye",
        "WR": ["Kendrick Bourne", "DeMario Douglas", "JuJu Smith-Schuster", "Hunter Henry"],
        "RB": ["Rhamondre Stevenson", "Antonio Gibson"],
        "Secondary": ["Jonathan Jones", "Jabrill Peppers", "Kyle Dugger", "Christian Gonzalez"],
        "Rush": ["Keion White", "Matthew Judon", "Ja'Whuan Bentley", "Josh Uche", "Christian Barmore"]
    },
    "NO": {
        "QB": "Derek Carr",
        "WR": ["Chris Olave", "Rashid Shaheed", "Cedrick Wilson Jr.", "Juwan Johnson"],
        "RB": ["Alvin Kamara", "Jamaal Williams"],
        "Secondary": ["Kool-Aid McKinstry", "Tyrann Mathieu", "Will Harris", "Marshon Lattimore"],
        "Rush": ["Cameron Jordan", "Nathan Shepherd", "Chase Young", "Demario Davis", "Willie Gay"]
    },
    "NYG": {
        "QB": "Daniel Jones",
        "WR": ["Malik Nabers", "Darius Slayton", "Allen Robinson II", "Darren Waller"],
        "RB": ["Devin Singletary", "Eric Gray"],
        "Secondary": ["Cor'Dale Flott", "Jalen Mills", "Jason Pinnock", "Deontae Banks"],
        "Rush": ["DJ Davidson", "Dexter Lawrence II", "Brian Burns", "Kayvon Thibodeaux", "Isiah Simmons"]
    },
    "NYJ": {
        "QB": "Aaron Rodgers",
        "WR": ["Garrett Wilson", "Mike Williams", "Allen Lazard", "Tyler Conklin"],
        "RB": ["Breece Hall", "Braelon Allen"],
        "Secondary": ["Sauce Gardner", "Chuck Clark", "Tony Adams", "DJ Reed"],
        "Rush": ["Jermaine Johnson", "CJ Mosley", "Haason Reddick", "Quincy Williams", "Quinnen Williams"]
    },
    "PHI": {
        "QB": "Jalen Hurts",
        "WR": ["AJ Brown", "DeVonta Smith", "Parris Campbell", "Dallas Goedert"],
        "RB": ["Saquon Barkley", "Kenneth Gainwell"],
        "Secondary": ["Quinyon Mitchell", "Cooper DeJean", "CJ Gardner-Johnson", "Darius Slay Jr."],
        "Rush": ["Jordan Davis", "Nakobe Dean", "Devin White", "Nolan Smith", "Jalen Carter"]
    },
    "PIT": {
        "QB": "Russell Wilson",
        "WR": ["George Pickens", "Van Jefferson", "Roman Wilson", "Pat Freiermuth"],
        "RB": ["Najee Harris", "Jaylen Warren"],
        "Secondary": ["Cam Sutton", "Minkah Fitzpatrick", "DeShon Elliott", "Donte Jackson"],
        "Rush": ["Larry Ogunjobi", "TJ Watt", "Patrick Queen", "Alex Highsmith", "Cameron Heyward"]
    },
    "SF": {
        "QB": "Brock Purdy",
        "WR": ["Deebo Samuel", "Brandon Aiyuk", "Jauan Jennings", "George Kittle"],
        "RB": ["Christian McCaffrey", "Elijah Mitchell"],
        "Secondary": ["Charvarius Ward", "Talanoa Hufanga", "Ji'Ayir Brown", "Deommodore Lenoir"],
        "Rush": ["Leonard Floyd", "Dre Greenlaw", "Fred Warner", "De'Vondre Campbell", "Nick Bosa"]
    },
    "SEA": {
        "QB": "Geno Smith",
        "WR": ["DK Metcalf", "Tyler Lockett", "Jaxon Smith-Njigba", "Noah Fant"],
        "RB": ["Kenneth Walker III", "Zach Charbonnet"],
        "Secondary": ["Devon Witherspoon", "Julian Love", "Rayshawn Jenkins", "Riq Woolen"],
        "Rush": ["Byron Murphy II", "Jerome Baker", "Uchenna Nwosu", "Tyrel Dodson", "Leonard Williams"]
    },
    "TB": {
        "QB": "Baker Mayfield",
        "WR": ["Mike Evans", "Chris Godwin", "Trey Palmer", "Cade Otton"],
        "RB": ["Rachaad White", "Chase Edmonds"],
        "Secondary": ["Jamel Dean", "Antoine Winfield Jr.", "Jordan Whitehead", "Zyon McCollum"],
        "Rush": ["Vita Vea", "KJ Britt", "Lavonte David", "Joe Tryon-Shoyinka", "Logan Hall"]
    },
    "TEN": {
        "QB": "Will Levis",
        "WR": ["Calvin Ridley", "DeAndre Hopkins", "Tyler Boyd", "Josh Whyle"],
        "RB": ["Tony Pollard", "Tyjae Spears"],
        "Secondary": ["Chidobe Awuzie", "Elijah Molden", "Amani Hooker", "L'Jarius Sneed"],
        "Rush": ["Sebastian Joseph-Day", "Harold Landry III", "Kenneth Murray Jr.", "Arden Key", "Jeffrey Simmons"]
    },
    "WAS": {
        "QB": "Jayden Daniels",
        "WR": ["Terry McLaurin", "Jahan Dotson", "Luke McCaffrey", "Zach Ertz"],
        "RB": ["Austin Ekeler", "Brian Robinson Jr."],
        "Secondary": ["Emmanuel Forbes Jr.", "Percy Butler", "Jeremy Chinn", "Mike Sainristil"],
        "Rush": ["Dante Fowler Jr.", "Bobby Wagner", "Jamin Davis", "Daron Payne", "Jonathan Allen"]
    }
}

def choose_player(team, position): #Generates players for each team; QB, WR, and RB
    if(position == "QB"):
        return (teams[team][position])
    else:
        return random.choice(teams[team][position])