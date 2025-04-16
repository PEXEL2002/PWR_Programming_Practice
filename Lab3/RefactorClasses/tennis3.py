class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.__player1_name = player1_name
        self.__player2_name = player2_name
        self.__player1_points = 0
        self.__player2_points = 0

    def won_point(self, plyer):
        if plyer == self.__player1_name:
            self.__player1_points += 1
        else:
            self.__player2_points += 1

    def score(self):
        if (self.__player1_points < 4 and self.__player2_points < 4) and (self.__player1_points + self.__player2_points < 6):
            piont_print = ["Love", "Fifteen", "Thirty", "Forty"]
            result = piont_print[self.__player1_points]
            return result + "-All" if (self.__player1_points == self.__player2_points) else result + "-" + piont_print[self.__player2_points]
        else:
            if self.__player1_points == self.__player2_points:
                return "Deuce"
            result = self.__player1_name if self.__player1_points > self.__player2_points else self.__player2_name
            return (
                "Advantage " + result
                if (abs((self.__player1_points - self.__player2_points)) == 1)
                else "Win for " + result
            )
