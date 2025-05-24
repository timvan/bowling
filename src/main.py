class Game:
    def __init__(self, score_sheet: str):
        self.score_sheet = score_sheet.split(" ")
        self.frames: list[Frame] = []

        self.calculate_score()

    def calculate_score(self):
        for f in self.score_sheet:
            self.frames.append(Frame())
            for roll in f:
                for frame in self.frames:
                    frame.take_roll(roll)

    def score(self):
        return sum([f.score for f in self.frames])

    def __repr__(self):
        return str([f.score for f in self.frames])


class Frame:
    def __init__(self):
        self._rolls = []
        self._roll_values = []
        self.completed = False

    def take_roll(self, roll: str):
        if self.completed:
            return

        self._rolls.append(roll)
        self._roll_values.append(self._roll_to_value(roll))

        if self.is_spare or self.is_strike:
            if len(self._rolls) == 3:
                self.completed = True
        else:
            if len(self._rolls) == 2:
                self.completed = True

    @property
    def is_spare(self):
        return "/" in self._rolls

    @property
    def is_strike(self):
        return "X" in self._rolls

    def _roll_to_value(self, roll: str):
        if roll == "-":
            return 0
        if roll.isnumeric():
            return int(roll)
        if roll == "/":
            return 10 - self._roll_values[-1]
        if roll == "X":
            return 10

    @property
    def score(self):
        return sum(self._roll_values)

    def __repr__(self):
        return str(self._rolls)


def score(score_sheet: str):
    game = Game(score_sheet)
    return game.score()
