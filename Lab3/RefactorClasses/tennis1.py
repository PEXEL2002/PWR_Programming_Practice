class TennisGame1:
    """
        Tennis Game Class 1
        This class is responsible for keeping track of the score of a tennis game.
    """
    def __init__(self, player1_name, player2_name):
        self.__player1_name = player1_name
        self.__player2_name = player2_name
        self.__player1_points = 0
        self.__player2points = 0
        self.__score_name = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }
        self.__score_draw = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }
        self.__advantage_tag = {
            1: "Advantage player1",
            -1: "Advantage player2",
            2: "Win for player1",
            -2: "Win for player2"
        }
    def won_point(self, player_name):
        if player_name == self.__player1_name:
            self.__player1_points += 1
        else:
            self.__player2points += 1

    def score(self):
        result = ""
        if self.__player1_points == self.__player2points:
            result = self.__score_draw.get(self.__player1_points, 'Deuce')
        elif self.__player1_points >= 4 or self.__player2points >= 4:
            minus_result = self.__player1_points - self.__player2points
            if minus_result < -2:
                minus_result = -2
            elif minus_result > 2:
                minus_result = 2
            result = self.__advantage_tag.get(minus_result)
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.__player1_points
                else:
                    result += "-"
                    temp_score = self.__player2points
                result += self.__score_name[temp_score]
        return result
