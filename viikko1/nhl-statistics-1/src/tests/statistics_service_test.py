import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_player(self):
        search = self.stats.search('Semenko')
        self.assertEqual(str(search), str(Player('Semenko', 'EDM', 4, 12)))

    def test_no_player_found(self):
        self.assertEqual(self.stats.search('...'), None)

    def test_search_team(self):
        EDMplayers = [str(i) for i in self.stats.team('EDM')]
        result = ['Semenko EDM 4 + 12 = 16',
                  'Kurri EDM 37 + 53 = 90',
                  'Gretzky EDM 35 + 89 = 124']
        
        self.assertEqual(EDMplayers, result)

    def test_top_player_by_points(self):
        Top2Players = [str(i) for i in self.stats.top(1)]
        result = ['Gretzky EDM 35 + 89 = 124',
                  'Lemieux PIT 45 + 54 = 99']
        
        self.assertEqual(Top2Players, result)

    def test_top_player_by_goals(self):
        Top2Players = [str(i) for i in self.stats.top(1, SortBy.GOALS)]
        result = ['Lemieux PIT 45 + 54 = 99',
                  'Yzerman DET 42 + 56 = 98']
        
        self.assertEqual(Top2Players, result)

    def test_top_player_by_assists(self):
        Top2Players = [str(i) for i in self.stats.top(1, SortBy.ASSISTS)]
        result = ['Gretzky EDM 35 + 89 = 124',
                  'Yzerman DET 42 + 56 = 98']
        
        self.assertEqual(Top2Players, result)