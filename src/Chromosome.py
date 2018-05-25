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
        self.fitness = abs(values[-1] - self.evaluate(self.start_node, values))
        return self.fitness

    def crossover(self, new_node, depth, p=0.1):
        if random() < p:
            this_level = [self.start_node]
            current_depth = 0
            while this_level:
                next_level = []

                if current_depth == depth:
                    node = next_level[randint(0, len(next_level) - 1)]

                    if random() < 0.5:
                        node.left = new_node
                    else:
                        node.right = new_node

                    break
                for n in this_level:
                    if n.left:
                        next_level.append(n.left)
                    if n.right:
                        next_level.append(n.right)
                this_level = next_level
                current_depth += 1

    def traverse(self, root):
        this_level = [root]
        levels = []
        while this_level:
            nextlevel = list()
            levels.append(this_level)
            for n in this_level:
                if n.left:
                    nextlevel.append(n.left)
                if n.right:
                    nextlevel.append(n.right)
            this_level = nextlevel

        return levels

    def __str__(self):
        return str(self.start_node)
