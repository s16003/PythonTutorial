from . level2 import Animate

class Animals(Animate):
    def breathe(self):
        print('breathing')

    def move(self):
        print('moving')

    def eat_food(self):
        print('eat_food')

class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding young')

class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print('eating leaves')

class cat(Mammals):
    pass

class Human(Mammals):
    def __init__(self, name):
        self.name = name
    def self_introduction(self):
        print("Hi, I'm", self.name, '.')