__author__ = 'Kevin Funkhouser and Omoju Miller'
# compare two list and see what they have in common
# we are not doing word match here, we are instead comparing the list
# to see if there are words that come from the same semantic frame
# compare the two list and see what ideas they
# have in common based on climbing up and down the word net hierarchy of terms
# Also we were going to use similarity of terms to see how close they are in meaning.


# The first thing is to clean up the list, never mind WordNet cleans them
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
import shlex
from models import Snippet

# Synset: a set of synonyms that share a common meaning.
# Build the ic

brown_ic = wordnet_ic.ic('ic-brown.dat')

a = ['']
b = ['']

def compare_Verb(list1, list2):
    #Both lists are  full of words
    # The first step is to create a list of synsets from each of the words
    # First try is simple iteration using only the NOUNS
    synLists1 = []
    synLists2 = []
    for word in list1:
        s = wn.synsets(word, pos=wn.VERB)
        synLists1.append(s)
    for word in list2:
        synLists2.append(wn.synsets(word, pos=wn.VERB))
        #For each of the words in the first list (the input)
    # find the closest match in the second list
    # Higher similarity score means closer match (1.0 = MAX)
    scores = []
    # The synsets for each word in the input list
    for synList in synLists1:
        bestFit = 0
        # Individual synset for each word of the input
        for syn1 in synList:
            # The synsets for each word in the reference
            for syns2 in synLists2:
                # Individual synset for each word of reference
                for syn2 in syns2:
                    #score = syn1.jcn_similarity(syn2, brown_ic) # Possibly change this ic
                    score = syn1.path_similarity(syn2) # Easiest possible similarity
                    # Check to see if this path is smaller
                    if score > bestFit:
                        bestFit = score
        scores.append(bestFit)
        #Now, with a list the size of list1 with the best fit for each
        # We need a way, to say this is the word that this matched at the highest level
    return reduce(lambda x, y: x + y, scores) / len(scores)

def compare_Noun(list1, list2):
    """

    :param list1: User supplied answer
    :param list2: Coded answer gotten from the Emcee
    :return:
    """
    print "The first list is ", list1
    print "The second list is ", list2
    #Both lists are  full of words
    # The first step is to create a list of synsets from each of the words
    # First try is simple iteration using only the NOUNS
    synLists1 = []
    synLists2 = []
    for word in list1:
        s = wn.synsets(word, pos=wn.NOUN)
        synLists1.append(s)
    for word in list2:
        synLists2.append(wn.synsets(word, pos=wn.NOUN))
        #For each of the words in the first list (the input)
    # find the closest match in the second list
    # Higher similarity score means closer match (1.0 = MAX)
    scores = []
    # The synsets for each word in the input list
    for synList in synLists1:
        bestFit = 0
        # Individual synset for each word of the input
        for syn1 in synList:
            # The synsets for each word in the reference
            for syns2 in synLists2:
                # Individual synset for each word of reference
                for syn2 in syns2:
                    #score = syn1.jcn_similarity(syn2, brown_ic) # Possibly change this ic
                    score = syn1.path_similarity(syn2) # Easiest possible similarity
                    # Check to see if this path is smaller
                    if score > bestFit:
                        bestFit = score
        scores.append(bestFit)
        #Now, with a list the size of list1 with the best fit for each
        # We need a way, to say this is the word that this matched at the highest level
    return reduce(lambda x, y: x + y, scores) / len(scores)

def clean_string(dirty_string):
    """

    :param dirty_string: a string that is in unicode format, e.g., u'dreams, goals, aspirations hope, fantasy, reality'
    :return: a list, ['dreams', 'goals', 'aspirations', 'hope', 'fantasy', 'reality']
    """
    s = dirty_string.encode("utf8")
    my_splitter = shlex.shlex(s, posix=True)
    my_splitter.whitespace += ','
    my_splitter.whitespace_split = True
    clean = list(my_splitter)
    return clean

def compare(a, b):
    s1 = compare_Noun(clean_string(a), clean_string(b))
    s2 = compare_Verb(clean_string(a), clean_string(b))
    print "This is s1", s1
    print s2
    answer = s1 + s2
    answer = answer / 2
    return answer


def main():
    return compare(a,b)
    # need to go through first 4 snippets and build a json file from the ouput
    # var mydataset = [{"snippetid": 1, "user_answer": "words words words", "score": 0.4, "decoded": "words words words"}]

if __name__ == "__main__":
    main()

#for snip in range(0, 4):
#   s = Snippet.objects.all()[snip]
#  print compare(s.user_answer, s.decoded)
# print "The end of one snippet comparison"

#In [2]: from hiphopathy.models import Snippet

#In [3]: import hiphopathy.list_cmp as cmp

#In [4]: s = Snippet.objects.all()[0]

#In [5]: cmp.compare(s.user_answer, s.decoded)