################################################################################################################
############ Python Script names "GeneticAlgorithm.py" must be loaded to execute Gentic Algorithm.######################


#Importing all necessary libraries
import numpy
import GA_Execution_Main
import pandas as pd
import random
import time
import matplotlib.pyplot as plt

#Calculating the start time of the algorithm
start_time = time.process_time()
history = []

#Importing the instances
dataset1 = pd.read_csv("TSP_Instance1.csv")
dataset = dataset1.to_numpy()
dist_matrix = dataset


#Storing all the weights of the nodes
solution = numpy.array(range(1, len(dataset)+1))
random.shuffle(solution)


#number of population in the algorithm
num_population = 500
population_array = (num_population, len(solution))

#initializing all populations with zero value
new_population = numpy.zeros(population_array)
# creating a initial feasible solution for all chromosomes
for chromosome in range(new_population.shape[0]):
    new_population[chromosome] = solution
    random.shuffle(new_population[chromosome])


#print(new_population)
# number of iteration to run
iteration = 100
# number of chromosomes with best fitness value to select
best_parents = 200

#seeting the global best value to 0 initially
global_best = 100000000000000000

#Genetic algorithm loop, starts here
for generation in range(iteration):
    print("Generation", generation)
    #sending population solution to calculate fitness value
    fitness = GA_Execution_Main.calculate_fitness(new_population, dist_matrix)
    print("Fitness values:", fitness)
    #setting the current best fitness value
    current_best = numpy.min(fitness)
    index = numpy.where(fitness == current_best)
    current_best_solution = new_population[index[0][0]]

    # checking if the current best is global best solution
    if current_best < global_best:
        global_best = current_best
        global_best_solution = current_best_solution
        global_best_solution = numpy.append(global_best_solution, global_best_solution[0])
        history.append(global_best)

    #sending chromosome in the mating pool. it will select specified number of chromosome in mating based on fitness
    parents = GA_Execution_Main.mating_pool(new_population, fitness,best_parents)
    #print(parents)
    #print("Best parents:", parents)

    # sending the selected parents to create offspring
    offspring_crossover = GA_Execution_Main.crossover(parents,offspring_size=(population_array[0] - parents.shape[0], len(dist_matrix)))
    #print(offspring_crossover)
    #print("Resulting offsprings:",offspring_crossover)

    #sending the offspring for the mutation process
    offspring_mutation = GA_Execution_Main.mutation(offspring_crossover)
    #print("Mutated Offspring", offspring_mutation)

    #mixing all offspring and prents into a new population
    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation



print("Generic Algorithm Completed")
#Calculate the end time of the algorithm
end_time = time.process_time()
print("Total calculation time:", end_time - start_time,'seconds')
print("Best objective function", global_best)
print("Best solution", global_best_solution)