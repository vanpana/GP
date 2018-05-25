import copy
from random import *

from src.Node import Node


class Chromosome:
    MAX_DEPTH = 5
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

        if left_sum is None:
            left_sum = 0

        if right_sum is None:
            right_sum = 0

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

    @staticmethod
    def get_random_from_depth(chromosome, depth):
        this_level = [chromosome.start_node]
        current_depth = 0
        while this_level:
            next_level = []

            # If the current depth has been reached, replace the node
            if current_depth == depth:
                return this_level[randint(0, len(this_level) - 1)]

            # Build the next levels
            for n in this_level:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            this_level = next_level
            current_depth += 1

    @staticmethod
    def crossover(p1, p2):
        parent1 = copy.deepcopy(p1)
        parent2 = copy.deepcopy(p2)

        # Get the depth to replace
        depth = randint(0, parent1.max_depth)

        # Get node to be replaced in first parent
        old_node = Chromosome.get_random_from_depth(parent1, depth)

        # Get a random node to replace from second parent
        new_node = Chromosome.get_random_from_depth(parent2, depth)

        # Replace left or right
        if random() < 0.5:
            old_node.left = new_node
        else:
            old_node.right = new_node

        return parent1

    def mutate(self, p=0.1):
        if random() < p:
            depth = randint(0, self.max_depth)
            node = self.get_random_from_depth(self, depth)

            if depth == self.max_depth:
                node.value = self.terminals[randint(0, len(self.terminals) - 2)]
            else:
                node.value = self.functions[randint(0, len(self.functions) - 1)]
        return self

    def __str__(self):
        return str(self.start_node)
