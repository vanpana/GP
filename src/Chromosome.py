import copy
from random import *

from src.Node import Node


class Chromosome:
    MAX_DEPTH = 8
    functions = ['+', '-', '*', '/']

    def __init__(self, terminals, d=MAX_DEPTH):
        self.terminals = copy.deepcopy(terminals)
        self.max_depth = d
        self.fitness = 0
        self.size = 0
        self.node_values = []
        self.start_node = self.full_expression(0, self.terminals)

    def full_expression(self, depth, terminals):
        if depth < self.max_depth:
            operator = randint(0, len(self.functions) - 1)
            return Node(self.functions[operator], self.full_expression(depth + 1, terminals),
                        self.full_expression(depth + 1, terminals))
        else:
            value = terminals.pop(randint(0, len(terminals) - 1))
            self.node_values.append(value)
            return Node(value)

    def evaluate(self, root, values):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return values[root.value]

        left_sum = self.evaluate(root.left, values)
        right_sum = self.evaluate(root.right, values)

        if root.value == '+':
            return left_sum + right_sum

        elif root.value == '-':
            return left_sum - right_sum

        elif root.value == '*':
            return left_sum * right_sum

        elif root.value == '/':
            if right_sum == 0:
                return 0
            else:
                return left_sum / right_sum

    def fitness_func(self, values):
        return values[-1] - self.evaluate(self.start_node, values)

    def __str__(self):
        return str(self.start_node)
