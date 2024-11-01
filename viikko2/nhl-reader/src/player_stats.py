from player import Player

class PlayerStats:
    def __init__(self, stats):
        self.players = stats.get_players()

    def top_scorers_by_nationality(self, nationality):
        list = []

        for player_dict in self.players:
            if player_dict['nationality'] == nationality:
                player = Player(player_dict)
                list.append(player)

        return list