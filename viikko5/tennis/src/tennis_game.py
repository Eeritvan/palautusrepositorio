class TennisGame:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]
    DEUCE_THRESHOLD = 3
    ADVANTAGE_THRESHOLD = 4
    WIN_DIFFERENCE = 2

    def __init__(self, player1_name, player2_name):
        self.p1_name = player1_name
        self.p2_name = player2_name
        self.p1_score = 0
        self.p2_score = 0

    def won_point(self, player_name):
        if player_name == self.p1_name:
            self.p1_score += 1
        else:
            self.p2_score += 1

    def get_score_name(self, player):
        return self.SCORE_NAMES[player]

    def get_tied_score(self):
        if self.p1_score < self.DEUCE_THRESHOLD:
            score_name = self.get_score_name(self.p1_score)
            return f"{score_name}-All"
        return "Deuce"

    def get_advantage_score(self):
        score_difference = self.p1_score - self. p2_score
        if score_difference == 1:
            return "Advantage player1"
        elif score_difference == -1:
            return "Advantage player2"
        elif score_difference >= self.WIN_DIFFERENCE:
            return "Win for player1"
        return "Win for player2"

    def get_running_score(self):
        score1_name = self.get_score_name(self.p1_score)
        score2_name = self.get_score_name(self.p2_score)
        return f"{score1_name}-{score2_name}"

    def get_score(self):
        if self.p1_score == self.p2_score:
            return self.get_tied_score()

        elif self.p1_score >= self.ADVANTAGE_THRESHOLD or self.p2_score >= self.ADVANTAGE_THRESHOLD:
            return self.get_advantage_score()
        
        return self.get_running_score()
