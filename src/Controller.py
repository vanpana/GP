from random import randint

from numpy import mean

from src.Chromosome import Chromosome


class Controller:
    def __init__(self, chromosome_number, filename):
        self.filename = filename
        self.data = self.load_data()
        self.chromosomes = [None for _ in range(chromosome_number)]
        self.generate_chromosomes()

    def load_data(self):
        data = []
        # Read data from file
        with open(self.filename, "r") as file:
            for line in file:
                data.append([float(x) for x in line.strip("\n").split(",")])

        return data

    # noinspection PyTypeChecker
    def generate_chromosomes(self):
        # Generate the terminal indexes
        terminals = [i for i in range(1, len(self.data[0]) - 2)]

        sum = 0
        fitness = []

        # Generate the chromosomes
        for index in range(len(self.chromosomes)):
            self.chromosomes[index] = Chromosome(terminals)
            data = self.data[randint(0, len(self.data) - 1)]
            sum += self.chromosomes[index].evaluate(self.chromosomes[index].start_node, data)
            fitness.append(self.chromosomes[index].fitness_func(data))

        print(self.chromosomes[0])
        print(sum / len(self.chromosomes))

        maxfit = max(fitness)
        fitness = [(x * 100) / maxfit for x in fitness]
        print(mean(fitness))
        # print(fit / len(self.chromosomes))
