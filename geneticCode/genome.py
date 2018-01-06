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
        return len([1 for i in xrange(len(other.gen_sequence))
                    if self.gen_sequence[i] == other.gen_sequence[i]]) - \
               len(other.gen_sequence)

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


"""
-._    _.--'"`'--._    _.--'"`'--._    _.--'"`'--._    _   
    '-:`.'|`|"':-.  '-:`.'|`|"':-.  '-:`.'|`|"':-.  '.` : '.   
  '.  '.  | |  | |'.  '.  | |  | |'.  '.  | |  | |'.  '.:   '. 
  : '.  '.| |  | |  '.  '.| |  | |  '.  '.| |  | |  '.  '.  : 
  '   '.  `.:_ | :_.' '.  `.:_ | :_.' '.  `.:_ | :_.' '.  `.' 
         `-..,..-'       `-..,..-'       `-..,..-'       `    
"""
