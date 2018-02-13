import random
import string


def select_chunk(candidates, order=1, level=False):

    text = [ ]

    start = random.randint(0, len(candidates) - order)
    chunk = candidates[start]

    if order == 1:
        pass
    else:
        for i in range(1, order):
            chunk = chunk + ' ' + candidates[start + i]
    text.append(chunk)
    #print "initial chunk: ", text
    return text


def check_for_possible_match(chunklist, line, order, n):
    candidate_str = ''
    if line[n] == chunklist[-1]:
        candidate_str += line[n+1]  # keep track of chunk following latest text-chunk
        if order == 1:
            pass
        else:
            for i in range(2, order+1):
                candidate_str += ' ' + line[n+i]
    return candidate_str


def gather_next_chunks(f, chunklist, order):
    candidates = []
    acceptable_characters = string.ascii_letters + string.digits + ' '

    for line in enumerate(f):
        if chunklist[-1] in line[1]:  # check for a possible match
            line = line[1].split()
            for n in range(0, len(line) - order):
                candidate_str = check_for_possible_match(chunklist, line, order, n)

                #have to process 'filter' type to 'str' type else TypeError
                candidate_str = ''.join(list(filter(lambda x: x in acceptable_characters, candidate_str)))

                candidates.append(candidate_str)

    return candidates


def edit_chunks(candidates):
    candidates_edited = []
    for i in candidates:
        if i != '':       # empty strings had been a problem
            candidates_edited.append(i)
    return candidates_edited


def pick_next_chunk(candidates, next_chunk):
    if candidates != []:
        r = random.randint(0, len(candidates) - 1)
        next_chunk = candidates[r]
    return next_chunk


def chunk_seq(f, text, order=3, length=50):
        """Generates a string of chuncks from an initial chunk.

        Input:
        f = lines in file
        text = list containing initial chunk
        order
        length

        Output:
        markov = a string, wordcount == length, of chunks
        """
        next_chunk = text[-1]
        chunklist = next_chunk.split()

        while len(text) * order < length:
            candidates = gather_next_chunks(f, chunklist, order) #1
            candidates_edited = edit_chunks(candidates)
            #print candidates_edited
            next_chunk = pick_next_chunk(candidates_edited, next_chunk)
            text.append(next_chunk)

        markov = ' '.join(text)
        return markov

