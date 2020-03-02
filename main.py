import sys

import numpy as np
import random
import decimal


# fitness function
# finds the fitness value for each chromosome and adds it to the totalFitness array
# parameter - chromo --> The chromosomes in the population
# return value - percentFit -->
def fitness(chromes):
    totalFitness = []  # Contains the fitness values of each chromosome
    # loop through each chromosome, evaluate the fitness of each, add to fitness array
    for chromosome in chromes:
        # print("Chromosomes from fitness function: ")
        # print(chromosome)
        # find out the vertical and diagonal fitness values
        vertFit = vertical(chromosome)
        diaFit = diagonal(chromosome)

        # finding the total fitness value and adding to the totalFitness array 
        chromoFit = vertFit + diaFit
        totalFitness.append(chromoFit)

        # exit condition
        if(chromoFit == 36):
            sys.exit("Solution has been found: " + str(chromosome))


        # reinitializing vertFit, diaFit and chromoFit to zero in order to be used for next iteration
        vertFit = 0
        diaFit = 0
        chromoFit = 0

    addedValues = sum(totalFitness)
    percentFit = []
    for i in totalFitness:
        percentFit.append(round(((i / addedValues)), 4))
    return percentFit


# roulette fuction
def roulette(chromosomeFit):
    pair = []           # the indices of the two parents that are choosen
    wheelValues = []    # the precentages in the wheel  
    cumulativeFit = 0   # the total fitness value

    # Step 1: Assigning precentages for each fitness value - for whatever reason the sum (i.e. cumulativeFit) does not give the correct value
    
    # Finding total fitness values
    cumulativeFit = sum(chromosomeFit)
    
    #print("cumulativeFit: + " + str(cumulativeFit))
    # Finding the precentage of each value compared to the total
    for element in chromosomeFit:
        wheelValues.append(round((element/cumulativeFit),4))

    #print("chomosomeFit  : " + str(chromosomeFit))
   # print("cumulative fit: " + str(wheelValues))

    # Step 2: Generate a random number
    runLoop = True          # used to run the loop until another index is found
    ParentOneIndex = -1     # indicates the index for one parent (it's essentially used to make sure the 2nd parent is not the same as the first)

    while(runLoop):
        randomInt = random.randint(1,100)
        #print ("random number: " + str(randomInt))

        # Step 3: Go around the wheel until you get to the random number
        start = 0       # the start of the slice in the roulette wheel for a percentage (i.e. the beginning of the slice pie)
        end = 0         # the end of the slice in the roulette wheel for a percentage (i.e. the end of the slice pie)
        index = 0       # indicates the element in the roulette wheel (i.e. the specific slice)
        for element in wheelValues:
            
            end = round((element*100 + end),2) 
            #print("start: " + str(start) + "     end: " + str(end))
            
            # if the random number is between the start and end add it to the pair array after completing the next if statement
            if (start <= randomInt and end >= randomInt):
                # if parentOne has not been selected add the index to the pair array and break from for loop
                if (ParentOneIndex == -1):
                    pair.append(index)
                    ParentOneIndex = index
                    break
                # if parentOne has an index and it's not the same as the selected index add it to the pair array and break from loop
                elif (index != parentOneIndex):
                   # print("parentOne: " + str(parentOneIndex))
                    pair.append(index)
                    runLoop = False
                    break
            index = index + 1
            start = end
       # print("index: " + str(index))

        parentOneIndex = index

    # return the index of the parents that were selected
    return pair


# verify the vertical fitness
# By checking if the numbers have not been repeated, if it has been repeated there are queens in the same column
# parameter - chromosome: the one chromosome from the total population
# return value - numOfNoRepeat: the number of times values have not been repeated (i.e. vertical fitness value)
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

    numOfNoRepeat = 8 - numOfRepeat
    # return vertical fitness value
    return numOfNoRepeat


# verify the diagonal fitness
def diagonal(chromosome):
    fitness = 0
    for i in range(len(chromosome)):
        # loop though every gene > the current gene
        for j in range(i + 1, len(chromosome)):
            # find slope of each
            slopeX = abs(i - j)
            slopeY = abs(chromosome[i] - chromosome[j])

            # if the two slopes match, the two queens are on each other's diagonal paths
            if (slopeY == slopeX):
                fitness = fitness + 1

    fitness = 28 - fitness
    return (fitness)


# crossover operation
# half of the genes from each parent crossover will switch with each other
def crossover(parent1, parent2):
    # print("\n -------Crossover is performed here-------")

    # selecting the index where the parents need to switch genes
    crossPoint = random.randint(1, 7)

    # creating child chromosomes that have half of each of the parents genes
    childOne = np.append(parent1[:crossPoint], parent2[crossPoint:len(parent2)])
    childTwo = np.append(parent2[:crossPoint], parent1[crossPoint:len(parent1)])

    # print("crosspoint: " + str(crossPoint))
    # print("ParentOne: " + str(parent1) + "childOne: " + str(childOne))  # Delete this line later -> it's just for testing purposes
    # print("ParentTwo: " + str(parent2) + "childTwo: " + str(childTwo))  # Delete this line later -> it's just for testing purposes

    # format the children for return
    children = np.array([childOne, childTwo])
    # print("-------------End of Crossover-------------\n")
    return children


# mutation operation
def mutation(chromosome):
    # print("\n -------------Mutation is performed here-------------")

    # randomly pick a gene to mutate from the chromosome
    mutated_gene = random.randrange(0, 7)
    # print("Gene to be mutated: " + str(mutated_gene))
    # print("The original chromosome: " + str(chromosome))

    # change its value to a random column
    chromosome[mutated_gene] = random.randint(0, 7)
    # print("The mutated chromosome: " + str(chromosome))
    # print("-------------End of Mutation-------------\n")

    return chromosome


def find_solution(population_size, g, chromes, cross_prob, mut_prob):
    # evaluate chromosome fitness
    fitness_array = fitness(chromes)
    print("fitness_array: " + str(fitness_array))

    # if all queens in one chromosome do not interfere with each other --> SOLUTION IS FOUND
    # print("\n% Fitness for each chromosome: " + str(fitness_array))

    # make array of new generation
    new_generation = np.random.randint(8, size=(population_size, g))

    row = 0
    # make five pairs from the original chromosomes & fitness values (using Roulette Wheel)
    for i in range(0, int(population_size / 2)):
        selected = roulette(fitness_array)
        print("selected: " + str(selected))
        # add the selected values to the new_generation array
        new_generation[row] = chromes[selected[0]]
        row = row + 1
        new_generation[row] = chromes[selected[1]]
        row = row + 1

    # print("====== THE SELECTED GENERATION ======")
    # print(str(new_generation))

    # randomly generate a number (0 to 1), if this is less than cross_prob, do crossover
    for i in range(0, population_size, 2):
        rand = random.uniform(0, 1)
        if (rand < cross_prob):
            children = crossover(new_generation[i], new_generation[i + 1])
            # replace the children of the new generation with the crossed-over version
            new_generation[i] = children[0]
            new_generation[i + 1] = children[1]
    # print("========= CROSSOVERED GENERATION =========")
    # print(new_generation)

    # randomly generate a number (0 to 1), if this is less than mut_prob, do mutation
    for i in range(0, population_size):
        rand = random.uniform(0, 1)
        if (rand < mut_prob):
            mutated_chromosome = mutation(new_generation[i])
            new_generation[i] = mutated_chromosome
    # print("========= MUTATED GENERATION =========")
    # print(new_generation)

    return new_generation


if __name__ == '__main__':
    # each chromosome is comprised of eight genes, each of which corresponding to a column number
    # number of chromosomes
    n = 10
    # number of genes in each chromosome
    genes = 8

    # crossover probability
    pc = 0.7
    # mutation probability
    pm = 0.2

    # randomly generate n chromosomes, organize in an array
    chromosomes = np.random.randint(8, size=(n, genes))

    # surround the following function call in a while loop which breaks once a solution is found
    gen = 0
    while(True):
        print("Generation: " + str(gen))
        new_gen = find_solution(n, genes, chromosomes, pc, pm)
        chromosomes = new_gen
        gen = gen + 1

    #fitness_array = fitness(chromosomes)
    #selected = roulette(fitness_array)





