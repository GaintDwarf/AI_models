import random
import utilites
import genome

__author__ = "Segev Gershon"
__date__ = "6/1/2017"
__version__ = "1"

"""
-._    _.--'"`'--._    _.--'"`'--._    _.--'"`'--._    _   
    '-:`.'|`|"':-.  '-:`.'|`|"':-.  '-:`.'|`|"':-.  '.` : '.   
  '.  '.  | |  | |'.  '.  | |  | |'.  '.  | |  | |'.  '.:   '. 
  : '.  '.| |  | |  '.  '.| |  | |  '.  '.| |  | |  '.  '.  : 
  '   '.  `.:_ | :_.' '.  `.:_ | :_.' '.  `.:_ | :_.' '.  `.' 
         `-..,..-'       `-..,..-'       `-..,..-'       `    
"""


class Generation(object):

    def __init__(self, mutation_rate=1):
        """
        the building method of the generation
        :param mutation_rate: a number between 0 and 100 which will represent
        the mutation rate parentage
        :type mutation_rate: int
        """
        super(Generation, self).__init__()
        self.population = []
        self.mating_pool = []
        self.generation = 0
        self.fitness_mean = -1
        self.mutation_rate = mutation_rate
        self.best_genome = genome.Genome([])

    def add_to_population(self, item):
        """
        the function adds the new genome to the population
        :param item: the new genome to add
        :type item: Genome
        :return: None
        """
        self.population.append(item)

    def generation_fitness(self, fitness_func):
        """
        the function matches the fitness to every individual in population
        :param fitness_func: the function which calculate the fitness of a
        genome
        :type fitness_func: function(list)
        :return: None
        """
        self.best_genome = self.population[0]
        for gen_sec in self.population:
            gen_sec.set_fitness(fitness_func(gen_sec.gen_sequence))
            if self.best_genome.fitness < gen_sec.fitness:
                self.best_genome = gen_sec

        self.fitness_mean = utilites.mean([i.fitness for i in self.population])

    def set_mating_pool(self):
        """
        the function sets the mating pool
        :return: None
        """
        for gen_sec in self.population:
            for i in xrange(int(gen_sec.fitness * 100)):
                self.mating_pool.append(gen_sec)

    def create_next_generation(self, cross_func, get_gen):
        """
        the function creates the next generation
        :param cross_func: the crossing function
        :type cross_func: function(list, list)
        :param get_gen: the function which initiate gens
        :type get_gen: function()
        :return: next generation
        :rtype: Generation
        """
        next_gen = Generation(self.mutation_rate)
        next_gen.generation = 1 + self.generation
        mating_pool_size = len(self.mating_pool)
        for i in xrange(len(self.population)):
            parent1 = self.mating_pool[random.randint(0, mating_pool_size - 1)]
            parent2 = self.mating_pool[random.randint(0, mating_pool_size - 1)]
            offspring = parent1.cross_with(parent2, cross_func)
            offspring.mutate(self.mutation_rate, get_gen)
            next_gen.add_to_population(offspring)
        return next_gen

    def act_on_generation(self, fitness_func, cross_func, get_gen):
        """
        the function act on generation and does all the staff
        that need to be done
        :param fitness_func: the function which calculate the fitness of a
        genome
        :type fitness_func: function(list)
        :param cross_func: the crossing function
        :type cross_func: function(list, list)
        :param get_gen: the function which initiate gens
        :type get_gen: function()
        :return: the new generation
        """
        self.generation_fitness(fitness_func)
        self.set_mating_pool()
        return self.create_next_generation(cross_func, get_gen)


"""
-._    _.--'"`'--._    _.--'"`'--._    _.--'"`'--._    _   
    '-:`.'|`|"':-.  '-:`.'|`|"':-.  '-:`.'|`|"':-.  '.` : '.   
  '.  '.  | |  | |'.  '.  | |  | |'.  '.  | |  | |'.  '.:   '. 
  : '.  '.| |  | |  '.  '.| |  | |  '.  '.| |  | |  '.  '.  : 
  '   '.  `.:_ | :_.' '.  `.:_ | :_.' '.  `.:_ | :_.' '.  `.' 
         `-..,..-'       `-..,..-'       `-..,..-'       `    
"""
