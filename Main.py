import unittest  # Import the testing framework
import BowlingGame  # Import the BowlingGame class


class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def test_one_strike(self):
        """
        A method to test a game with one strike
        :return:
        """
        print("Test case #1\n Testing game with one strike....\n")
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.roll_many(0, 17)
        assert self.game.score() == 24

    def test_one_spare(self):
        print("Test case #2\n Testing game with one spare....\n")
        self.game.rolls(5)
        self.game.rolls(5)
        self.game.rolls(3)
        self.roll_many(0, 17)
        assert self.game.score() == 16

    def test_all_ones(self):
        print("Test case #3\n Testing game with each bowl hitting one pin....\n")
        self.roll_many(1, 20)
        assert self.game.score() == 20

    def test_gutter_game(self):
        print("Test case #4\n Testing a gutter ball game....\n")
        for i in range(0, 20):
            self.game.rolls(0)
        assert self.game.score() == 0

    def test_perfect_game(self):
        print("Test case #5\n Testing a perfect game....\n")
        self.roll_many(10, 12)
        assert self.game.score() == 300

    def test_spare_game(self):
        print("Test case #6\n Testing a game with all spares....\n")
        self.roll_many(5, 21)
        assert self.game.score() == 150

    def roll_many(self, pins, rolls):
        for i in range(rolls):
            self.game.roll(pins)
