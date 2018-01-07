import random
from geneticCode import generation
from geneticCode import genome

__author__ = "Segev Gershon"
__date__ = "6/1/2017"
__version__ = "1"

sample_size = 1000
search_for = "to be or not to be"
mutation_rate = 1


def gen_initiator():
    outcome = random.randint(0, 26)
    if outcome == 26:
        return " "
    return chr(outcome+97)


def initiate_genome():
    gen_sequence = [gen_initiator() for i in xrange(len(search_for))]
    return genome.Genome(gen_sequence)


def initiate_population():
    zero_generation = generation.Generation(mutation_rate)
    for i in xrange(sample_size):
        zero_generation.add_to_population(initiate_genome())
    return zero_generation


def fitness_func(gen_sequence):
    return len([1 for i in xrange(len(search_for)) if search_for[i] ==
               gen_sequence[i]]) / float(len(search_for))


def cross_func(gen_sequence1, gen_sequence2):
    mid = len(search_for) / 2
    return gen_sequence1[:mid] + gen_sequence2[mid:]


def main():
    current_generation = initiate_population()
    while search_for not in current_generation.population:
        current_generation.generation_fitness(fitness_func)
        current_generation.set_mating_pool()

        print "The mean of generation number {} is : {}% \n and the closest " \
              "sequence was ::: {} ::: with score of : {}%" \
              "".format(current_generation.generation,
                        int(current_generation.fitness_mean * 100),
                        "".join(current_generation.best_genome.gen_sequence),
                        int(current_generation.best_genome.fitness * 100))

        current_generation = current_generation.create_next_generation(
            cross_func, gen_initiator)

    current_generation.generation_fitness(fitness_func)

    print "\n\n\nfinale results:"
    print "===================================================================="
    print "The mean of the last generation (no. {}) was : {}% \n and the " \
          "closest sequence was ::: {} ::: with score of : {}%" \
          "".format(current_generation.generation,
                    int(current_generation.fitness_mean * 100),
                    "".join(current_generation.best_genome.gen_sequence),
                    int(current_generation.best_genome.fitness * 100))

    raw_input("\n\n\nclick any key to quit...")


if __name__ == '__main__':
    main()
