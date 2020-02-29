import numpy as np



# fitness function
def fitness(number, chromes):
    totalFitness = np.empty((number), int)

    # loop through each chromosome, evaluate the fitness of each, add to fitness array
    for chromosome in chromes:
        print(chromosome)
        # find out the vertical and diagonal fitness values
        vertFit = vertical(chromosome)
        print("The returned fitness value for vertical: " + str(vertFit))
        diaFit = diagonal(chromosome)
        print("The returned fitness value for diagonal: " + str(diaFit))

        totalFit = vertFit + diaFit
        # totalFitness.append(total, axis=0)

    print("fitness() should return an array of fitness values")


def roulette(chromes, fitness):
    print("Pair up chromosomes, return array of pairs")


# verify there are no queens vertically
# SOLUTION: By checking if the numbers have not been repeated, if it has been repeated there are queens in the same column
# parameter - chromosome: the one chromosome from the total population
def vertical(chromosome):
    numOfRepeat = 0  # the total number of genes that were repeated
    count = 0  # used to count the number of genes within that choromsome

    # Goes through 0-7 and checks if the gene has been created more than once
    for i in range(len(chromosome)):
        for genes in chromosome:
            # check if this gene == another gene
            if genes == i:
                count = count + 1

        # if a value was repeated more than once it is added to the numOfRepeat
        if count > 1:
            numOfRepeat = numOfRepeat + count
        count = 0

    # return vertical fitness value
    return numOfRepeat


# verify the diagonal fitness
def diagonal(chromosome):
    fitness = 0
    for i in range(len(chromosome)):
        # loop though every gene > the current gene
        for j in range(i+1, len(chromosome)):
            # find slope each
            slopeX = abs(i - j)
            slopeY = abs(chromosome[i] - chromosome[j])

            #if the two slopes match, the two queens are on each other's diagonal paths
            if(slopeY == slopeX):
                fitness = fitness + 1
    return(fitness)


# crossover operation
# half of the genes from each parent crossover will switch with each other 
def crossover(parent1, parent2):

    # creating child chromosomes that have half of each of the parents genes
    childOne = np.append(parent1[:4], parent2[4:len(parent2)])
    childTwo = np.append(parent2[:4], parent1[4:len(parent1)])
    
    print("childOne: " + str(childOne))    # Delete this line later -> it's just for testing purposes
    print("childTwo: " + str(childTwo))    # Delete this line later -> it's just for testing purposes

    # Not too sure what to return here though
    


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
    # find_solution(n, genes, chromosomes)

    # test section - try what you need here!
    print("parent1: " + str(chromosomes[0]))
    print("parent2: " + str(chromosomes[1]))

    
    crossover(chromosomes[0],chromosomes[1])
