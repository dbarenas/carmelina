from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import WordPunctTokenizer
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy
from nltk.probability import ELEProbDist
import sys,nltk
import numpy
import urllib2
#import gnuplot

print ":"*50
print "Preproceso"
ftxt = open(sys.argv[1], 'rU')
#fstop = open(sys.argv[2], 'rU')
#stopwords = fstop.read().split()
#fstop.close()
'''Preproceso '''
lista=[]
for line in ftxt.readlines():
        wordlist=line.split(',')
        p = wordlist[1].find('+')
        n = wordlist[1].find('-')
        if p > 1 and n > 1:
                sent = "negative"
        if p > 1 and n < 1:
                sent = "positive"
        if p < 1 and n > 1:
                sent = "negative"

        if len(wordlist) > 2:
                r=wordlist[2].replace('"','')
                re=r.replace('\n','')
                lista.append((re,sent))

print ":"*50

'''Corpus 2  '''
listare = []
for (words, sentiment) in lista:
  words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
  listare.append((words_filtered, sentiment))
#print "total corpus"
#print listare

'''aqui generamos el train set '''
test_lista = []
for i in range(len(lista)/2,len(lista)):
        test_lista.append(lista[i])
test_listare = []
for (words, sentiment) in test_lista:
  words_filterede = [e.lower() for e in words.split() if len(e) >= 3]
  test_listare.append((words_filterede, sentiment))
#print "test tweets"
#print test_listare

'''Tokenizar '''
def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words

''' La frecuencia '''
def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

#print "Freq Dist"
wl= get_words_in_tweets(listare)
#print nltk.FreqDist.plot(nltk.FreqDist(wl))
#print nltk.FreqDist(wl)

word_features = get_word_features(get_words_in_tweets(listare))

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
      features['contains(%s)' % word] = (word in document_words)
    return features

''' Clasificando sobre el corpus de aprendizaje'''
training_set = nltk.classify.apply_features(extract_features, test_listare)

#print " ** training "
#print training_set

classifier = nltk.NaiveBayesClassifier.train(training_set)

def train(labeled_featuresets, estimator=ELEProbDist):
    # Create the P(label) distribution
    label_probdist = estimator(label_freqdist)
    # Create the P(fval|label, fname) distribution
    feature_probdist = {}
    return NaiveBayesClassifier(label_probdist, feature_probdist)

#print "Most informative features"
#print classifier.show_most_informative_features(32)

print "-"*50
tweet = 'Multiple users on one machine never seemed to behave like youd expect'
print tweet
print "___/^"
#print extract_features(tweet.split())
print classifier.classify(extract_features(tweet.split()))
print "-"*50

print listare[0]


for texte in listare:
        classifier.classify(extract_features(texte[0]))

acc = accuracy(classifier, training_set) * 100
print 'accuracy: %.2f%%' % acc

