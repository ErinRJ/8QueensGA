import numpy as np


# fitness function
def fitness(number, chromes):
    totalFitness = np.empty((number), int)

    # loop through each chromosome, evaluate the fitness of each, add to fitness array
    for chromosome in chromes:
        vertFit = vertical()
        horiFit = horizontal()
        diaFit = diagonal()

        total = vertFit + horiFit + diaFit
        totalFitness.append(total, axis=0)

    print("fitness() should return an array of fitness values")

def roulette(chromes, fitness):
    print("Pair up chromosomes, return array of pairs")

# verify there are no queens vertically
def vertical():
    print("Vertical fitness test performed here")


# verify there are no queens horizontally
def horizontal():
    print("Horizontal fitness test performed here")


# verify there are no queens diagonally
def diagonal():
    print("Diagonal fitness test performed here")


# crossover operation
def crossover():
    print("Crossover is performed here")


# mutation operation
def mutation():
    print("Mutation is performed here")


def find_solution(number, g, chromes):

    # evaluate chromosome fitness
    fitnessArray = fitness(number, chromes)

    # if all queens in one chromosome do not interfere with each other --> SOLUTION IS FOUND

    # using the fitness values gathered, perform roulette-wheel
    # roulette()

    # perform crossover (if needed)
    # crossover()

    # perform mutation (if needed)
    # mutation()




if __name__ == '__main__':
    # each chromosome is comprised of eight genes, each of which corresponding to a column number
    # number of chromosomes
    n = 10
    # number of genes in each chromosome
    genes = 8

    # crossover probability
    pc = 0.7
    # mutation probability
    pm = 0.001

    # randomly generate n chromosomes, organize in an array
    chromosomes = np.random.randint(8, size=(n, genes))
    print(chromosomes)

    # surround the following function call in a while loop which breaks once a solution is found
    find_solution(n, genes, chromosomes)

