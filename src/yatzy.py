from src.pips import Pips


class Yatzy:
    # Constants
    FIFTY = 50
    ZERO = 0

    @staticmethod
    def chance(*dice):
        return sum(dice)

    @staticmethod
    def yatzy(dice):
        if all(die == dice[0] for die in dice):
            return Yatzy.FIFTY
        return Yatzy.ZERO

    def reapeted_number_sum(dice, number):
        return sum(die for die in dice if die == number)

    @staticmethod
    def ones(*dice):
        return Yatzy.reapeted_number_sum(dice, Pips.ONE.value)

    @staticmethod
    def twos(*dice):
        return Yatzy.reapeted_number_sum(dice, Pips.TWO.value)

    @staticmethod
    def threes(*dice):
        return Yatzy.reapeted_number_sum(dice, Pips.THREE.value)

    @classmethod
    def fours(cls, *dice):
        return cls.reapeted_number_sum(dice, Pips.FOUR.value)

    @classmethod
    def fives(cls, *dice):
        return cls.reapeted_number_sum(dice, Pips.FIVE.value)

    @classmethod
    def sixes(cls, *dice):
        return cls.reapeted_number_sum(dice, Pips.SIX.value)

    @classmethod
    def score_pair(cls, *dice):
        TWO = Pips.TWO.value
        for number in Pips.reversedValues():
            if dice.count(number) >= TWO:
                return number * TWO
        return 0

    @classmethod
    def two_pair(cls, *dice):
        TWO = Pips.TWO.value
        total = 0
        pairs_counter = 0
        for number in Pips.reversedValues():
            if dice.count(number) >= TWO:
                total += number * 2
                pairs_counter += 1
        if pairs_counter < 2:
            return 0
        return total

    @staticmethod
    def four_of_a_kind(*dice):
        FOUR = Pips.FOUR.value
        return next(
            (number * FOUR for number in Pips.values() if dice.count(number) >= FOUR), 0
        )

    @staticmethod
    def three_of_a_kind(*dice):
        THREE = Pips.THREE.value
        return next(
            (number * THREE for number in Pips.values() if dice.count(number) >= THREE),
            0,
        )

    @staticmethod
    def smallStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (
            tallies[0] == 1
            and tallies[1] == 1
            and tallies[2] == 1
            and tallies[3] == 1
            and tallies[4] == 1
        ):
            return 15
        return 0

    @staticmethod
    def largeStraight(*dice):
        dice_not_reapeted = set(dice)
        dice_sorted = sorted(list(dice_not_reapeted))
        return (
            20
            if all(dice_sorted) in Pips.minus(Pips.SIX) and len(dice_sorted) == 5
            else Yatzy.ZERO
        )

    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        for i in range(6):
            if tallies[i] == 2:
                _2 = True
                _2_at = i + 1

        for i in range(6):
            if tallies[i] == 3:
                _3 = True
                _3_at = i + 1

        if _2 and _3:
            return _2_at * 2 + _3_at * 3
        else:
            return 0


if __name__ == "__main__":
    Yatzy.largeStraight(6, 2, 3, 4, 5)
