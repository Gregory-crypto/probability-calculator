import copy
import random

class Hat:
    def __init__(self, **args):
        self.contents = []
        for i in args:
            for j in range(args[i]):
                self.contents.append(i)
        self.copy = copy.copy(self.contents)

    def draw(self, number):
        if number > len(self.contents):
            return self.contents
        drops = []
        for i in range(number):
            drops.append(self.contents.pop(random.randint(0, len(self.contents) - 1)))
        return drops


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    semi_success = 0
    success = 0
    sum = 0

    for i in range(num_experiments):
        hat.contents = copy.copy(hat.copy)
        experiment = hat.draw(num_balls_drawn)
        for k in expected_balls:
            sum += expected_balls[k]
            if experiment.count(k) >= expected_balls[k]:
                semi_success += 1
        if semi_success == len(expected_balls):
            success += 1
        semi_success = 0

    probability = success / num_experiments
    return probability