class BowlingGame:
    """
    A class used to represent a bowling game

    ...

    Attributes
    ----------
    roll_index : int
    pins : int
    result : int

    Methods
    -------
    roll(pins)
        Adds the set number of pins to the rolls list

    score
        Adds up the score of the game using the game rules along with the type of score function
        Returns the final score result

    is_strike(roll_index)
        method to check if strike is scored

    is_spare(roll_index)
        method to check if a spare is scored

    strike_score(roll_index)
        method to add a strike score rule

    spare_score(roll_index)
        method to add a spare score rule

    frame_score(roll_index)
        method to add a normal scored frame
    """
    def __init__(self):
        """
        A constructor to initialise a new empty list for each game
        """
        self.rolls = []

    def roll(self, pins):
        """
        A method to add the number of pins to the new list
        :param pins:
        :return:
        """
        self.rolls.append(pins)

    def score(self):
        """
        A method to run through a full game and at each frame check what
        score is to be added
        :return: result
        """
        result = 0
        roll_index = 0

        for frameIndex in range(10):  # a loop that will run through 10 frames

            if self.is_strike(roll_index):
                result += self.strike_score(roll_index)
                roll_index += 1

            elif self.is_spare(roll_index):
                result += self.spare_score(roll_index)
                roll_index += 2
            else:
                result += self.frame_score(roll_index)
                roll_index += 2
        return result

    def is_strike(self, roll_index):
        """
        a method to check the given index == 10 therefore a strike
        :param roll_index:
        :return: true or false
        """
        return self.rolls[roll_index] == 10

    def is_spare(self, roll_index):
        """
        a method to check the given index + the next == 10 therefore a spare
        :param roll_index:
        :return: true or false
        """
        return self.rolls[roll_index] + self.rolls[roll_index+1] == 10

    def strike_score(self, roll_index):
        """
        a method that calculates a strikes total score based on the next two rolls
        :param roll_index:
        :return: int
        """
        return 10 + self.rolls[roll_index+1] + self.rolls[roll_index+2]

    def spare_score(self, roll_index):
        """
        a method that calculates a spare total score based on the roll after the spare
        :param roll_index:
        :return: int
        """
        return 10 + self.rolls[roll_index+2]

    def frame_score(self, roll_index):
        """
        a method to calculate a standard frame when neither a spare nor strike is scored
        the total of the two rolls to the frame
        :param roll_index:
        :return: int
        """
        return self.rolls[roll_index] + self.rolls[roll_index + 1]
