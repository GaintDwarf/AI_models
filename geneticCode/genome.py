import random

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


class Genome:

    def __init__(self, gen_sequence):
        self.gen_sequence = gen_sequence
        self.fitness = -1

    def __cmp__(self, other):
        iterate_on = other
        if other is Genome:
            iterate_on = other.gen_sequence
        return len([1 for i in xrange(len(iterate_on))
                    if self.gen_sequence[i] == iterate_on[i]]) - len(iterate_on)

    def __add__(self, other):
        return self.fitness + other.fitness

    def set_fitness(self, fitness):
        """
        the function sets the fitness of the genome
        :param fitness: the fitness to set to
        :type fitness: float
        :return: None
        """
        self.fitness = fitness

    def cross_with(self, mate, cross_func):
        """
        the function mixes the current genome with its mate
        :param mate: the mate to mix with
        :type mate: Genome
        :param cross_func: the crossing function
        :type cross_func: function(list, list)
        :return: new mixed genome
        """
        return Genome(cross_func(self.gen_sequence, mate.gen_sequence))

    def mutate(self, mutation_rate, get_gen):
        """
        the function mutate an offspring
        :param get_gen: the function which initiate gens
        :type get_gen: function()
        :param mutation_rate: the mutation rate in percentage
        :type mutation_rate: int
        :return: None
        """
        for i in xrange(len(self.gen_sequence)):
            if random.randint(1, 100) <= mutation_rate:
                mutation = get_gen()
                self.gen_sequence[i] = mutation


"""
-._    _.--'"`'--._    _.--'"`'--._    _.--'"`'--._    _   
    '-:`.'|`|"':-.  '-:`.'|`|"':-.  '-:`.'|`|"':-.  '.` : '.   
  '.  '.  | |  | |'.  '.  | |  | |'.  '.  | |  | |'.  '.:   '. 
  : '.  '.| |  | |  '.  '.| |  | |  '.  '.| |  | |  '.  '.  : 
  '   '.  `.:_ | :_.' '.  `.:_ | :_.' '.  `.:_ | :_.' '.  `.' 
         `-..,..-'       `-..,..-'       `-..,..-'       `    
"""
