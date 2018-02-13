import random


def read_file(filename):
    """Parses a text file.
    """
    f = open(filename, 'r')
    f = f.readlines()
    #f.close()
    return f


def get_candidates(f):
    #f = read_file(f)

    candidates = ''
    while candidates == '' or candidates == '\n':
        for index, line in enumerate(f):

            #generate random numbers less than index + n
            uno = random.randrange(index + 2)
            dos = random.randrange(index + 22)
            #probably not the only way to do this

            if uno == dos:
                candidates += line

    #candidates = candidates.split() #split text into chunks -- other ways to do this?

    #print "initial candidate lines:\n", candidates
    return candidates


def split_text_into_chunks(candidates):
    candidates = candidates.split()
    return candidates
