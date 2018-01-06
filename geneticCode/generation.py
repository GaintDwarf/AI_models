import random
import genome
import utilites

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


class Generation:

    def __init__(self):
        self.population = []
        self.mating_pool = []
        self.generation = 0
        self.fitness_mean = -1

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
        for gen in self.population:
            gen.set_fitness(fitness_func(gen.gen_sequence))

        self.fitness_mean = utilites.mean(self.population)

    def set_mating_pool(self):
        """
        the function sets the mating pool
        :return: None
        """
        for gen in self.population:
            for i in xrange(gen.fitness):
                self.mating_pool.append(gen)

    def create_next_generation(self, cross_func):
        """
        the function creates the next generation
        :param cross_func: the crossing function
        :type cross_func: function(list, list)
        :return: next generation
        :rtype: Generation
        """
        next_gen = Generation()
        next_gen.generation = 1 + self.generation
        mating_pool_size = len(self.mating_pool)
        for i in xrange(len(self.population)):
            parent1 = self.mating_pool[random.randint(mating_pool_size)]
            parent2 = self.mating_pool[random.randint(mating_pool_size)]
            next_gen.add_to_population(parent1.cross_with(parent2, cross_func))
        return next_gen


"""
-._    _.--'"`'--._    _.--'"`'--._    _.--'"`'--._    _   
    '-:`.'|`|"':-.  '-:`.'|`|"':-.  '-:`.'|`|"':-.  '.` : '.   
  '.  '.  | |  | |'.  '.  | |  | |'.  '.  | |  | |'.  '.:   '. 
  : '.  '.| |  | |  '.  '.| |  | |  '.  '.| |  | |  '.  '.  : 
  '   '.  `.:_ | :_.' '.  `.:_ | :_.' '.  `.:_ | :_.' '.  `.' 
         `-..,..-'       `-..,..-'       `-..,..-'       `    
"""
