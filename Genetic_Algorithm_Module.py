############################## This is genetic algorithm module that has all functions#####################
import numpy


#this function calculates the fitness of all chromosomes
def calculate_fitness(pop, dist_matrix):
    arr = (pop.shape[0], len(dist_matrix))
    distance = numpy.zeros(arr, dtype=int)
    arr1 = (pop.shape[0], len(dist_matrix)+1)
    pop1 = numpy.zeros(arr1, dtype=int)
    for row in range(pop.shape[0]):
        pop1[row] = (numpy.append(pop[row], pop[row][0]))

    # creating a vector of solution where represent demand node covers,  0 is not covered
    for row in range((pop.shape[0])):
        for i in range(len(dist_matrix)):
            distance[row][i] = dist_matrix[(int(pop1[row][i])-1), ((pop1[row][i+1])-1)]

    # sum all distance to calculate fitness of chromosome
    fitness = numpy.sum(distance, axis=1)
    return fitness


#this function selects the parents for the mating process
def mating_pool(pop, fitness, num_parents):
    parents = numpy.empty((num_parents, pop.shape[1]))
    for parent_num in range(num_parents):
        min_fitness_idx = numpy.where(fitness == numpy.min(fitness))
        min_fitness_idx = min_fitness_idx[0][0]
        parents[parent_num, :] = pop[min_fitness_idx, :]
        # setting the picked parents value to maximum so that it is not picked again
        fitness[min_fitness_idx] = 1000000
    return parents



# thsi function does the crossover between selected parents
def crossover(parents, offspring_size):
    offspring = numpy.zeros(offspring_size, dtype=int)
    #print(offspring_size)
    #print(offspring)
    crossover_point = numpy.uint8(offspring_size[1]/2)
    #print(crossover_point)

    for k in range(offspring_size[0]):
        # index of parents 1 to merge with parent 2
        parent1_idx = k%parents.shape[0]
        #index of parent 2 to merge woth parent 1
        parent2_idx = (k+1)%parents.shape[0]
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
        j = 0

        for i in range(len(parents[parent2_idx])):
            if parents[parent2_idx, i] not in offspring[k]:
                offspring[k, (crossover_point+j)] = parents[parent2_idx, i]
                j+=1

    return offspring


# this function introduce the mutation
def mutation(offspring_crossover):
    for idx in range(offspring_crossover.shape[0]):
        offspring_crossover[idx][4], offspring_crossover[idx][10] = offspring_crossover[idx][10], offspring_crossover[idx][4]
        offspring_crossover[idx][1], offspring_crossover[idx][5] = offspring_crossover[idx][5], offspring_crossover[idx][1]
        offspring_crossover[idx][6], offspring_crossover[idx][9] = offspring_crossover[idx][9], offspring_crossover[idx][6]

    return offspring_crossover