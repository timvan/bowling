class Game:
    def __init__(self, score_sheet: str):
        self.score_sheet: str = score_sheet.replace(" ", "")
        self._scores = []

    def _calculate_symbol_score(self, i: int):
        roll = self.score_sheet[i]
        score = 0

        if roll == "-":
            score = 0
        elif roll.isnumeric():
            score = int(roll)
        elif roll == "/":
            score = 10 - self._calculate_symbol_score(i - 1)
        elif roll == "X":
            score = 10
        else:
            raise
        return score

    def _calculate_multipliers(self, i: int):
        roll = self.score_sheet[i]
        multiplier = 0

        if roll == "/":
            multiplier = self._calculate_multiplier_score(i, 1)
        elif roll == "X":
            multiplier = self._calculate_multiplier_score(i, 2)
        return multiplier

    def _calculate_multiplier_score(self, i: int, n: int):
        roll = self.score_sheet[i]
        multiplier = 0

        remaining_rolls = len(self.score_sheet) - i

        for j in range(min(remaining_rolls, n)):
            multiplier += self._calculate_symbol_score(i + j + 1)

        return multiplier

    def score(self):
        self._scores = []
        for i in range(len(self.score_sheet)):
            base_score = self._calculate_symbol_score(i)
            multiplier_score = self._calculate_multipliers(i)
            roll_score = base_score + multiplier_score
            self._scores.append(roll_score)

        return sum(self._scores)


def score(score_sheet: str):
    game = Game(score_sheet)
    return game.score()
