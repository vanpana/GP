from random import randint

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

        # Generate the chromosomes
        for index in range(len(self.chromosomes)):
            self.chromosomes[index] = Chromosome(terminals)

        print(self.chromosomes[0])
        print(self.chromosomes[0].evaluate(self.chromosomes[0].start_node, self.data[randint(0, len(self.data) - 1)]))
