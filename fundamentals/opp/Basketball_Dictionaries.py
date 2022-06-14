players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "Small Forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "Small Forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philidelphia 76ers"
    },
    {
        "name": "Carlos Osornio",
        "age": 30,
        "position": "PG",
        "team": "LA Lakers"
    }
]

kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "Small Forward",
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "Small Forward",
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets"
}

# Challenge 1: Update the constructor to accept a dictionary (player) as an argument and set the attributes using the dictionary
class Player:
    def __init__(self, data):
        self.name = data["name"]
        self.age = data["age"]
        self.position = data["position"]
        self.team = data["team"]

# Ninja Bonus: Add an @class method called get_team(cls, team_list) that, given a list of dictionaries populates and returns a new list of Player objects.
    @classmethod
    def get_team(cls, team_list):
        team = []
        for player in team_list:
            team.append(player)
        return team

print(Player.get_team(players))

jason_tatum = Player(players[1])
print(jason_tatum.name)

# Complete challenge 2: Create 3 instances of the Player class using the given dictionaries
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)
print(player_kevin.age)
print(player_jason.team)
print(player_kyrie.name)

#Complete challenge 3: Populate a new list with Player instances from the list of players.

new_team = []
for player in players:
    new_team.append(player)
print(new_team)

