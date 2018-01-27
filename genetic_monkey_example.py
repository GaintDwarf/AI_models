import random
from GeneticCode import generation
from GeneticCode import genome

__author__ = "Segev Gershon"
__date__ = "6/1/2017"
__version__ = "1"

sample_size = 200
search_for = "doodle"
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
    return (len([1 for i in xrange(len(search_for)) if search_for[i] ==
                 gen_sequence[i]]) / float(len(search_for))) ** 2 + 0.01


def cross_func(gen_sequence1, gen_sequence2):
    return [gen_sequence1[i] if i % 2 == 0 and i < len(gen_sequence1)/2 else
            gen_sequence2[i] if i % 2 == 1 else gen_sequence1[i]  for i in
            xrange(len(gen_sequence1))]


def main():
    with open("generations.txt", "wb") as log:
        current_generation = initiate_population()
        while search_for not in current_generation.population:
            current_generation.generation_fitness(fitness_func)
            current_generation.set_mating_pool()

            print "The mean of generation number {} is : {}% " \
                  "\n and the closest " \
                  "sequence was ::: {} ::: with score of : {}%" \
                  "".format(current_generation.generation,
                            int(current_generation.fitness_mean * 100),
                            "".join(current_generation.best_genome.gen_sequence),
                            int(current_generation.best_genome.fitness * 100))

            log.write(
                "\n==========================================================\n" 
                "The mean of generation number {} is : {}% " 
                "\n and the closest " 
                "sequence was ::: {} ::: with score of : {}%\n" 
                "".format(current_generation.generation,
                          int(current_generation.fitness_mean * 100),
                          "".join(current_generation.best_genome.gen_sequence),
                          int(current_generation.best_genome.fitness * 100)))
            log.write("   ".join(["".join(i.gen_sequence) for i in
                                 current_generation.population]))

            current_generation = current_generation.create_next_generation(
                cross_func, gen_initiator)

        current_generation.generation_fitness(fitness_func)

        log.write(
            "\n=============================================================\n"
            "The mean of generation number {} is : {}% "
            "\n and the closest "
            "sequence was ::: {} ::: with score of : {}%\n"
            "".format(current_generation.generation,
                      int(current_generation.fitness_mean * 100),
                      "".join(current_generation.best_genome.gen_sequence),
                      int(current_generation.best_genome.fitness * 100)))
        log.write(
            "   ".join(["".join(i.gen_sequence) for i in
                        current_generation.population]))

        print "\n\n\nfinale results:"
        print "================================================================"
        print "The mean of the last generation (no. {:,}) was : {}% \n\tThe " \
              "closest sequence was ::: {} ::: with score of : {}% \n" \
              "[total genomes bred:{:,}]" \
              "".format(current_generation.generation,
                        int(current_generation.fitness_mean * 100),
                        "".join(current_generation.best_genome.gen_sequence),
                        int(current_generation.best_genome.fitness * 100),
                        current_generation.generation * sample_size)

    raw_input("\n\n\n")


if __name__ == '__main__':
    main()
