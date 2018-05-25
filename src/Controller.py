from random import randint

from numpy import mean

from src.Chromosome import Chromosome


class Controller:
    def __init__(self, chromosome_number, generations, filename):
        self.filename = filename
        self.generations = generations
        self.data = self.load_data()
        self.chromosomes = [None for _ in range(chromosome_number)]
        self.generate_chromosomes()
        self.averages = []

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

        # Generate the chromosomes
        for index in range(len(self.chromosomes)):
            self.chromosomes[index] = Chromosome(terminals)

    def run(self):
        while self.generations:
            chromo_fitness = [[] for _ in range(len(self.chromosomes))]

            # Calculate the fitness for every chromosome for each data case
            counter = 0
            for chromo in self.chromosomes:
                for data_line in self.data:
                    chromo_fitness[counter].append(chromo.fitness_func(data_line))
                counter += 1

            # Calculate average fitness
            chromo_fitness = [mean(x) for x in chromo_fitness]

            # Append average fitness
            self.averages.append(mean(chromo_fitness))

            # Tuple the chromosome with its average and position
            chromo_fitness = [(self.chromosomes[i], chromo_fitness[i], i) for i in range(len(self.chromosomes))]

            # Get the number of random tuples
            no_tuples = randint(2, len(chromo_fitness))

            # Pick the tuples from the list
            picked = []
            for i in range(no_tuples):
                picked.append(chromo_fitness.pop(randint(0, len(chromo_fitness) - 1)))

            # Sort by fitness
            picked = sorted(picked, key=lambda tup: tup[1])

            # Pick the best two
            parent1 = picked[0]
            parent2 = picked[1]

            # Cross them over and mutate the child
            child = Chromosome.crossover(parent1[0], parent2[0]).mutate()

            # Calculate child fitness
            child_fitness = []
            for data_line in self.data:
                child_fitness.append(child.fitness_func(data_line))
            child_fitness = mean(child_fitness)

            # Check child fitness with parent's fitness
            if parent1[1] > parent2[1] and parent1[1] > child_fitness:
                self.chromosomes[parent1[2]] = child

            if parent2[1] > parent1[1] and parent2[1] > child_fitness:
                self.chromosomes[parent2[2]] = child

            print(self.generations, child_fitness)
            self.generations -= 1
