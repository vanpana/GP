from src.Chromosome import Chromosome


class Controller:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def run(self):
        # Read data from file
        with open(self.filename, "r") as file:
            for line in file:
                self.data.append(line.strip("\n").split(","))

        # Generate the terminal indexes
        terminals = [i for i in range(1, len(self.data[0]) - 2)]

        # Generate a chromosome
        chromosome = Chromosome(terminals)

        print(chromosome)