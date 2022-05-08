#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import itertools
import os
from tqdm import tqdm
from collections import defaultdict, Counter
import pickle
import random
from scipy.stats import entropy
import matplotlib.pyplot as plt


# In[2]:


# Let grey is represented by 0, yellow by 1 and green by 2
# what could be possible input info of 5 letter word in wordle
allPatterns = list(itertools.product([0,1,2], repeat=5))
print(len(allPatterns))
# Total 3 power 5 that is 243 possible combination


# In[3]:


#  Extracting all and curated word list from data folder
# with open(r'words.txt', encoding='utf-8') as f:
#     rawwordlelist = f.read()
# rawwordlelist = rawwordlelist.split(",")
# allWordList = []
# for word in rawwordlelist:
#     word = word.strip('"')
#     allWordList.append(word)
# print(len(allWordList))

allWordList = list(pd.read_csv('./data/processed/valid_guesses.csv')['word'])
curatedWordList = list(pd.read_csv('./data/processed/valid_solutions.csv')['word'])
allWordList += curatedWordList
print("all valid guess words Len",len(allWordList))
print("curated word list Len:", len(curatedWordList))


# In[4]:


# First 2315 words of our list are most frequent wordle answers. so lets extract it too.
# curatedWordList = allWordList[:2315]
# print(len(curatedWordList))


# In[5]:


# Sanity check whether all words are of 5 length or not
errorMsg = 'All words are not of 5 letter each'
assert len({len(x) for x in allWordList}) == 1 and len(allWordList[0]) == 5, errorMsg


# In[6]:


def convertWordToPattern(guessWord, realAnswer):
    """
    lets suppose if ans is midst and we guessed digit then we return (1, 2, 0, 1, 2)
    """
    pattern = [0, 0, 0 ,0 ,0]
    for i, x in enumerate(guessWord):
        pattern[i] = int(x in realAnswer)
    for i, (x1, x2) in enumerate(zip(guessWord, realAnswer)):
        if x1 == x2:
            pattern[i] = 2
    
    return tuple(pattern)

# lets test it
print(convertWordToPattern('digit', 'midst'))
    


# In[7]:


def createPatternMap(wordList):
    """
    For every word in the wordlist with every possible pattern information we get from wordle game, 
    lets create a list of possible set of words.
    """
    wordPatternMap = defaultdict(lambda: defaultdict(set))
    for word in tqdm(wordList):
        for realAnswer in wordList:
            pattern = convertWordToPattern(word, wordList)
            wordPatternMap[word][pattern].add(realAnswer)
    return dict(wordPatternMap)


# In[8]:


if 'wordPatternMap.p' not in os.listdir('./data/processed'):
#     Lets cache this patterns map so that we dont need to create it everytime
    wordPatternMap = createPatternMap(curatedWordList)
    pickle.dump(wordPatternMap, open('./data/processed/wordPatternMap.p', 'wb+'))
else:
    # loading patterns map from the cache file
    wordPatternMap = pickle.load(open('./data/processed/wordPatternMap.p', 'rb'))


# In[9]:


def calculateEntropies(possibleWords, wordPatternMap):
#     wordList,
    """
    Calculating the entropy for every word in our words list , taking into account the remaining possible words
    """
    entropiesMap = {}
    for word in tqdm(possibleWords):
        counts = []
        for pattern in allPatterns:
            matches = wordPatternMap[word][tuple(pattern)]
            matches = matches.intersection(possibleWords)
            counts.append(len(matches))
        entropiesMap[word] = entropy(counts)
    return entropiesMap


# In[ ]:





# In[10]:


# Lets begin a trial
# Lets play wordle with nytimes by giving guess word and its pattern output as result

# Assumption: If there is duplicate letter, pattern will show 1 for duplicate letter which
# is in wrong position and not 0

def playNyTimesWordleWithUserInput():
#     realAnswer = random.choice(curatedWordList)
#     print("====RealAnswer to reach is ", realAnswer)
    possibleWords = set(curatedWordList)

    for i in range(6):
    #     print("====possiblewordss", possibleWords)
        entropies = calculateEntropies( possibleWords, wordPatternMap)
        print("set of possible words includes like:")
        print([sample_word[0] for sample_word in sorted(entropies.items(), key=lambda sample_word: -sample_word[1])[:10]])

    #   Pick max entropy word
        guessWord = random.choice([x[0] for x in sorted(entropies.items(), key=lambda x: -x[1])[:10]])
        print('Our suggestion for guess based on Entropy: ', guessWord)
        
        print("=====Now tell which Word you want to Put in Wordle as your guess:  eg: midst")
        guessWord = input()
        print('===Now Enter the pattern info return by wordle: eg: 01221 where 0=grey,1=yellow, 2=green color')
        guessWordPatternOutput = tuple(map(int, tuple(input())))

#         guessWordPatternOutput = [0, 0, 0, 0, 0]
#         for i, l1 in enumerate(guessWord):
#             guessWordPatternOutput[i] = int(l1 in realAnswer)

#         for i, (l1, l2) in enumerate(zip(guessWord, realAnswer)):
#             if l1 == l2:
#                 guessWordPatternOutput[i] = 2

        print('you guessed: \"', guessWord, '\"wordle pattern you provided:', guessWordPatternOutput)
        if guessWordPatternOutput == (2,2,2,2,2):
            print(f'WIN! in {i+1} guesses')
            print()
            print()
            print()
            break
    #     print("wordPatternMap", wordPatternMap[guessWord])
        words = wordPatternMap[guessWord][tuple(guessWordPatternOutput)]
    #     print("====words", words)
        possibleWords = possibleWords.intersection(words)
playNyTimesWordleWithUserInput()
    


# In[17]:


# Statistical Analysis for number of trails
countSum = 0
totalTrial = 0
guessCountToWin = list()
for noOfTrial in range(200):
    sm = 0
    realAnswer = random.choice(curatedWordList)
    print("====RealAnswer to reach is ", realAnswer)
    possibleWords = set(curatedWordList)

    for _ in range(10):
        entropies = calculateEntropies( possibleWords, wordPatternMap)
        print("set of possible words includes like:")
        print([sample_word[0] for sample_word in sorted(entropies.items(), key=lambda sample_word: -sample_word[1])[:10]])

    #   Pick max entropy word
        guessWord = random.choice([x[0] for x in sorted(entropies.items(), key=lambda x: -x[1])[:10]])
        print('Our suggestion for guess based on Entropy: ', guessWord)
        
        sm += 1
        guessWordPatternOutput = [0, 0, 0, 0, 0]
        for i, l1 in enumerate(guessWord):
            guessWordPatternOutput[i] = int(l1 in realAnswer)

        for i, (l1, l2) in enumerate(zip(guessWord, realAnswer)):
            if l1 == l2:
                guessWordPatternOutput[i] = 2

        print('guessWordPatternOutput:', guessWordPatternOutput)
        if guessWord == realAnswer:
            guessCountToWin.append(sm)
            countSum += sm
            print('You Won! :',  len(guessCountToWin), ' times')
            print()
            print()
            print()
            break
    #     print("wordPatternMap", wordPatternMap[guessWord])
        words = wordPatternMap[guessWord][tuple(guessWordPatternOutput)]
    #     print("====words", words)
        possibleWords = possibleWords.intersection(words)


# In[18]:


print("=====avgGuessCount", countSum / len(guessCountToWin))
print("totalTrial", len(guessCountToWin))
print("guess array", guessCountToWin)


# In[23]:


plt.close("all")
df = pd.DataFrame(guessCountToWin)
df.plot.barh()


# In[25]:


print("Number of times we are not able to guess in 6 guess out of 200 trials, which is the limit in NY wordle game:")
print(len(list(filter(lambda x: x> 6, guessCountToWin))))


# In[33]:


tryCountMap = Counter(guessCountToWin)
print(tryCountMap)
series = pd.Series(tryCountMap, index=[1,2,3,4,5,6,7,8], name="Guess Count")
series.plot.pie(autopct='%1.1f%%',figsize=(15, 15))


# In[ ]:


get_ipython().system('jupyter nbconvert 2-entropyayushgupta*.ipynb --to python')

