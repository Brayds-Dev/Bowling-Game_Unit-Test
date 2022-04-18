import unittest  # Import the testing framework
import BowlingGame


class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def testOneStrike(self):
        print("Test case #1\n Testing game with one strike....\n")
        self.game.rolls(10)
        self.game.rolls(4)
        self.game.rolls(3)
        self.rollMany(0, 16)
        assert self.game.score() == 24

    def testOneSpare(self):
        print("Test case #2\n Testing game with one spare....\n")
        self.game.rolls(5)
        self.game.rolls(5)
        self.game.rolls(3)
        self.rollMany(0, 17)
        assert self.game.score() == 16

    def testAllOnes(self):
        print("Test case #3\n Testing game with each bowl hitting one pin....\n")
        self.rollMany(1, 20)
        assert self.game.score() == 20

    def testGutterGame(self):
        print("Test case #4\n Testing a gutter ball game....\n")
        for i in range(0, 20):
            self.game.rolls(0)
        assert self.game.score() == 0

    def testPerfectGame(self):
        print("Test case #5\n Testing a perfect game....\n")
        self.rollMany(10,12)
        assert self.game.score() == 300

    def testSpareGame(self):
        print("Test case #6\n Testing a game with all spares....\n")
        self.rollMany(5, 21)
        assert self.game.score() == 150

    def rollMany(self, pins, rolls):
        for i in range(rolls):
            self.game.rolls(pins)
