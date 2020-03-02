import numpy as np
import random

# fitness function
# finds the fitness value for each chromosome and adds it to the totalFitness array
# parameter - chromo --> The chromosomes in the population
# return value - percentFit -->
def fitness(chromes):
    totalFitness = []   # Contains the fitness values of each chromosome
    # loop through each chromosome, evaluate the fitness of each, add to fitness array
    for chromosome in chromes:
        print(chromosome)
        # find out the vertical and diagonal fitness values
        vertFit = vertical(chromosome)
        print("The returned fitness value for vertical: " + str(vertFit))
        diaFit = diagonal(chromosome)
        print("The returned fitness value for diagonal: " + str(diaFit))

        # finding the total fitness value and adding to the totalFitness array 
        chromoFit = vertFit + diaFit
        totalFitness.append(chromoFit)

        # reinitializing vertFit, diaFit and chromoFit to zero in order to be used for next iteration
        vertFit=0
        diaFit=0
        chromoFit=0


    print("The chromosone fitness are: "+ str(totalFitness))
    Sum= sum(totalFitness)
    print("The sum total of fitness are: "+ str(Sum))
    percentFit=[]
    for i in totalFitness:
        percentFit.append(round(((i/Sum)), 4))
    return  percentFit

# roulette fuction 
def roulette(chromosomeFit):
    print("\nReturn Pair")
    pair=[]
    cumulaarray = []
    cumulative = 0
    for i in chromosomeFit:
        cumulative = cumulative + i
        cumulative = round(cumulative, 4)
        cumulaarray.append(cumulative)
    #print(str(cumulaarray))

    rndnumberSelect = random.randint(0, 101)
    rndnumberSelect = rndnumberSelect / 100
    #print(rndnumberSelect)

    index = 0
    for i in cumulaarray:
        if i >= rndnumberSelect:
            parentOne = index
            parenttwo = parentOne
            break
        index = index + 1

    print("first selected chromosome is: " + str(parentOne))
    pair.append(parentOne)

    while (parentOne == parentOne):
        rndnumberSelect2 = random.randint(0, 101)
        rndnumberSelect2 = rndnumberSelect2 / 100
        #print(rndnumberSelect2)

        index2 = 0
        for i in cumulaarray:
            if i >= rndnumberSelect2:
                parenttwo = index2
                break
            index2 = index2 + 1

        if (parenttwo != parentOne):
            break

    print("second selected chromosome is: " + str(parenttwo))
    pair.append(parenttwo)
    print(str(pair))

    return pair

# vertial function
# verify there are no queens vertically
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

    numOfNoRepeat= 8-numOfRepeat
    # return vertical fitness value
    return numOfNoRepeat

# diagonal function
# verify the diagonal fitness
def diagonal(chromosome):
    fitness = 0
    for i in range(len(chromosome)):
        # loop though every gene > the current gene
        for j in range(i + 1, len(chromosome)):
            # find slope each
            slopeX = abs(i - j)
            slopeY = abs(chromosome[i] - chromosome[j])

            # if the two slopes match, the two queens are on each other's diagonal paths
            if (slopeY == slopeX):
                fitness = fitness + 1

    fitness=28-fitness
    return (fitness)


# crossover operation
# half of the genes from each parent crossover will switch with each other
def crossover(parent1, parent2):
    
    # selecting the index where the parents need to switch genes
    crossPoint = random.randint(1,7)
    
    # creating child chromosomes that have half of each of the parents genes
    childOne = np.append(parent1[:crossPoint], parent2[crossPoint:len(parent2)])
    childTwo = np.append(parent2[:crossPoint], parent1[crossPoint:len(parent1)])

    print("crosspoint: " + str(crossPoint))
    print("childOne: " + str(childOne))  # Delete this line later -> it's just for testing purposes
    print("childTwo: " + str(childTwo))  # Delete this line later -> it's just for testing purposes

    # Not too sure how to return the children though


# mutation operation
def mutation(chromosome):
    print("Mutation is performed here")
    #numbers of chromes to change
    mutaStrength=random.randrange(1, 9)
    print(mutaStrength)
    mutaInd=np.random.choice(8, mutaStrength, replace=False)
    mutaInd.sort()
    print(mutaInd)

    for i in mutaInd:
        chromosome[i]=random.randrange(0, 8)

    print(str(chromosome))


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

    # test section-try what you need here!
    print("parent1: " + str(chromosomes[0]))
    print("parent2: " + str(chromosomes[1]))
    print("parent3: " + str(chromosomes[2]))
    print("parent4: " + str(chromosomes[3]))
    print("parent5: " + str(chromosomes[4]))
    print("parent6: " + str(chromosomes[5]))
    print("parent7: " + str(chromosomes[6]))
    print("parent8: " + str(chromosomes[7]))

    crossover(chromosomes[0],chromosomes[1])

    t= fitness(chromosomes)
    print("complete fitness for all is:" + str(t))
    print("selected pair is"+str(roulette(t)))
    #mutation(chromosomes[0])


