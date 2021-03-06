#!/usr/local/bin/python
# Program:  Word Sentence Generator
################################################################################################
# Program Description:
#   This program reads in a training corpus - using it to create an n-gram
#   model.  The program then uses this n-gram model to generate sentences.
#   Sentences are generated by calculating the probability of a word 
#   given the n-1 words before it, and  normalizing the probabilities of the
#   possible words. The program picks a random word by producing a random
#   number between 0 and 1 and then picking the appropriate word, until and
#   end of sentence marker is generated.
################################################################################################

import re
import random
import sys
from nltk.probability import ConditionalFreqDist

def ngram_generator(m, n, corpus_in):
    corpus = word_by_word(corpus_in)
    cfdist = ConditionalFreqDist();
    # calculate conditional frequencies using corpus
    queue = ["<start>" for i in range(m-1)] #initialize queue

    for word in corpus:
        # ignore special corpus markers
        if word.startswith('*') or word == '0': continue
        queue.append(word)
        if len(queue) == m:
            context = ' '.join(queue[0:-1])
            token = queue[-1]
            cfdist[context].inc(token)

            if str(token) == '.': # end of sentence
                queue = ["<start>" for i in range(m-1)]
            else:    
                queue.pop(0)

    #generate n random sentences
    for curSent in range(n):
        print "Sentence %d: " % (curSent + 1),
        contextQueue = ["<start>" for i in range(m-1)];
        
        while 1:
            # choose the next token, biased by conditional frequency
            context = ' '.join(contextQueue)
            randValue = random.random()
            curTotal = 0.0
            samples = cfdist[context].samples()
            samples.sort()
            for token in samples:
                curTotal += cfdist[context].freq(token)
                if curTotal > randValue:
                    break
            
            print str(token),
            contextQueue.append(token)
            contextQueue.pop(0)

            if str(token) == '.' or str(token) == '?' or str(token) == '!':
                print "\n"
                break


raw = "In another positive sign, the unemployment rate seemed to be dropping at a faster rate than the number of new jobs would imply. This is perhaps because new businesses and the newly self-employed are less likely to be counted in the Labor Department’s survey of businesses, from which the job numbers are drawn, than in its survey of households, from which the unemployment rate is calculated. Economists continued to warn of potential dangers ahead, including disaster in the euro zone, increased tensions with Iran leading to higher gas prices, and the expiration of the Bush tax cuts. Congress may yet decline to continue extensions of the payroll tax break and unemployment benefits that have bolstered consumer spending. Money, in the form of loans, is still hard to come by, and home prices have continued to fall. There is also a sense of having been here before, since hopes were similarly buoyed by good news last year at this time. Those hopes, Mr. Schomer pointed out, were soon dashed by the earthquake in Japan. I m a little bit concerned that Iran could be this year’s Japan,he said."

def load_corpus(corpusFile):
    return VerySimpleCorpus(corpusFile)


class VerySimpleCorpus:
        "A very very simple corpus class"
        def __init__(self, corpusFile):
            self.corpusFile = corpusFile

        def words(self):        
            f = open(self.corpusFile, 'rU')

            for line in f:
                if re.match(r'^\s*$', line):
                    continue #skip blank lines
                line = re.sub('([,;:.!?])', r' \1 ', line) #insert space around some punctuation
                line = re.sub('[("\'"-)]', '', line) #strip out other punctuation
                line = line.rstrip(); 

                for word in re.split(r'\s+', line):
                    yield word
            return


def word_by_word(generator):
    for item in generator:
        if type(item) == list:
            for word in item:
                yield word
        else:
            yield item
    return
