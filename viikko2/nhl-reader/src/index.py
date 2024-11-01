import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")

    fins = []

    for player_dict in response:
        if player_dict['nationality'] == 'FIN':
            player = Player(player_dict)
            fins.append(player)

    for player in fins:
        print(f"{player.name} team {player.team} goals {player.goals} assists {player.assists}")

if __name__ == "__main__":
    main()