from random import *

from src.Node import Node


class Chromosome:
    MAX_DEPTH = 5
    functions = ['+', '-', '*']

    def __init__(self, terminals, d=MAX_DEPTH):
        self.terminals = terminals
        self.max_depth = d
        self.fitness = 0
        self.size = 0
        self.start_node = self.full_expression(0, terminals)

    def full_expression(self, depth, terminals):
        if depth < self.max_depth:
            operator = randint(0, len(self.functions) - 1)
            return Node(operator, self.full_expression(depth + 1, terminals), self.full_expression(depth + 1, terminals))
        else:
            return Node(terminals.pop(randint(0, len(terminals) - 1)))