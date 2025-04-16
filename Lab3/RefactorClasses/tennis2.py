class TennisGame2:
    def __init__(self, player1_name, player2_name):
        self.__player1_name = player1_name
        self.__player2_name = player2_name
        self.__player1_points = 0
        self.__player2_points = 0
        self.__score_names = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player_name):
        if player_name == self.__player1_name:
            self.__player1_points += 1
        else:
            self.__player2_points += 1

    def score(self):
        if self.__player1_points == self.__player2_points:
            if self.__player1_points < 3:
                return f"{self.__score_names[self.__player1_points]}-All"
            else:
                return "Deuce"

        if self.__player1_points >= 4 or self.__player2_points >= 4:
            diff = self.__player1_points - self.__player2_points
            if diff == 1:
                return "Advantage " + self.__player1_name
            elif diff == -1:
                return "Advantage " + self.__player2_name
            elif diff >= 2:
                return "Win for " + self.__player1_name
            elif diff <= -2:
                return "Win for " + self.__player2_name

        return f"{self.__score_names[self.__player1_points]}-{self.__score_names[self.__player2_points]}"
