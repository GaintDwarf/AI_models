import random


def gen_initiator():
    outcome = random.randint(0, 26)
    if outcome == 26:
        return " "
    return chr(outcome+97)


if __name__ == '__main__':
    counter = 0
    out = "to be or not to be"
    temp = ""
    while temp != out:

        temp = "".join([gen_initiator() for i in xrange(len(out))])
        if counter % 250 == 0 or temp == out:
            print "{:,}\t: {}".format(counter, temp)
        counter += 1

    raw_input("Success :o")
