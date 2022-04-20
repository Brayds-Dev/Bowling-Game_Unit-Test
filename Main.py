import unittest  # Import the testing framework
import BowlingGame  # Import the BowlingGame class


class TestBowlingGame(unittest.TestCase):
    """
    A class used to test instances of the bowling game class

    ....

    Methods
    -------
    setUp
        Method to initialise an instance of the bowling game

    test_one_strike
        A method to test a game with one strike

    test_one_spare
        A method ti test a game with one spare

    test_all_ones
        A method to test a game where only 1 is scored on each roll

    test_gutter_game
        A method to test a game where no pins are scored

    test_perfect game
        A method to test a perfect score game (all strikes)

    test_spare_game
        A method to test a game filled with spares
    """

    def setUp(self):
        """
        Hook method to set up the test instance before exercising it
        :return:
        """
        self.game = BowlingGame.BowlingGame()

    def test_one_strike(self):
        """
        A method to test a game with one strike with a test case assertion
        :return:
        """
        print("Test case #1\n Testing game with one strike....")
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.roll_many(0, 17)
        assert self.game.score() == 24

    def test_one_spare(self):
        """
        A method to test a game with one spare followed by a test case assertion
        :return:
        """
        print("Test case #2\n Testing game with one spare....")
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.roll_many(0, 17)
        assert self.game.score() == 16

    def test_all_ones(self):
        """
        A method to test a game where all rolls hit one pin followed by a test case assertion
        :return:
        """
        print("Test case #3\n Testing game with each roll hitting one pin....")
        self.roll_many(1, 20)
        assert self.game.score() == 20

    def test_gutter_game(self):
        """
        A method to test a game where no pins are scored followed by a test case assertion
        :return:
        """
        print("Test case #4\n Testing a gutter ball game....")
        for i in range(0, 20):
            self.game.roll(0)
        assert self.game.score() == 0

    def test_perfect_game(self):
        """
        A method to test a game where all rolls score a strike followed by a test assertion
        :return:
        """
        print("Test case #5\n Testing a perfect game....")
        self.roll_many(10, 12)
        assert self.game.score() == 300

    def test_spare_game(self):
        """
        A method to test a game where all rolls score a spare followed by a test assertion
        :return:
        """
        print("Test case #6\n Testing a game with all spares....")
        self.roll_many(5, 21)
        assert self.game.score() == 150

    def roll_many(self, pins, rolls):
        """
        A method to add multiple rolls with a given score to the game
        :param pins:
        :param rolls:
        :return:
        """
        for i in range(rolls):
            self.game.roll(pins)
