"""
Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
"""

def score(dice):
    result = 0
    my_dict = {}
    test_set = set(dice)
    if len(dice) > 0:
        for i in test_set:
            my_dict[i] = dice.count(i)

    for key, value in my_dict.items():
        if value == 3:
            if key == 1: result = result + 1000
            elif key == 5: result = result + 500
        if value >= 3:
            if key == 2: result = result + 200
            if key == 3: result = result + 300
            if key == 4: result = result + 400
            if key == 6: result = result + 600
        if key == 1:
            if (1 <= value < 3): result = result + 100 * value
            elif value == 5: result = result + 1200
            elif value == 4: result = result + 1100
        if key == 5:
            if (1 <= value < 3): result = result + 50 * value
            elif value == 4: result = result + 550
            elif value == 5: result = result + 600

    return result