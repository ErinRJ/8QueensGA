import numpy as np


# fitness function
def fitness(number, chromes):
    totalFitness = np.empty((number), int)

    # loop through each chromosome, evaluate the fitness of each, add to fitness array
    for chromosome in chromes:
        print(chromosome)
        vertFit = vertical(chromosome)
        diaFit = diagonal()

        # total = vertFit + diaFit
        # totalFitness.append(total, axis=0)

    print("fitness() should return an array of fitness values")

def roulette(chromes, fitness):
    print("Pair up chromosomes, return array of pairs")

# verify there are no queens vertically
# SOLUTION: By checking if the numbers have not been repeated, if it has been repeated there are queens in the same column
# parameter - chromosome: the one chromosome from the total population
def vertical(chromosome):
    numOfRepeat = 0 # the total number of genes that were repeated
    count = 0 # used to count the number of genes within that choromsome

    # Goes through 0-7 and checks if the gene has been created more than once
    for i in range(len(chromosome)):
        for genes in chromosome:
            # check if this gene == another gene
            if genes == i:
                count = count + 1

        # if a value was repeated more than once it is added to the numOfRepeat
        if count > 1:
            numOfRepeat = numOfRepeat + count
            print("numOfRepeat: " + str(numOfRepeat) + "\n")
        count = 0

    print("numOfRepeat: " + str(numOfRepeat))

    # return vertical fitness value
    return numOfRepeat;
    # if (numOfRepeat == 0):
    #     return 5
    # elif (numOfRepeat < 5 and numOfRepeat > 0):
    #     return 3
    # else:
    #     return 0


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

    # surround the following function call in a while loop which breaks once a solution is found
    find_solution(n, genes, chromosomes)

    # test section - try what you need here!
    

