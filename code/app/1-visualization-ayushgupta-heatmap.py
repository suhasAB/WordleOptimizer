#!/usr/bin/env python
# coding: utf-8

# In[24]:


import matplotlib.pyplot as plt
plt.rcParams['svg.fonttype'] = 'none'
import seaborn as sns
import pandas as pd
import numpy as np


# In[25]:


with open(r'words.txt', encoding='utf-8') as f:
    rawwordlelist = f.read()
rawwordlelist = rawwordlelist.split(",")
wordList = []
for word in rawwordlelist:
    word = word.strip('"')
    wordList.append(word)
print(wordList)


# In[26]:


len(wordList)


# In[27]:


# First 2315 words of our list are most frequent wordle answers. so lets extract it too.
curatedWordList = wordList[:2315]
print(curatedWordList)


# In[28]:


letters = 'abcdefghijklmnopqrstuvwxyz'

def createLetterPosMap(word_list):
    # lpMap = letter Pos Map
    lpMap = {i: {letter: 0 for letter in letters} for i in range(5)}
    for pos in range(5):
        for word in word_list:
            lpMap[pos][word[pos]] += 1
    # normalize each count by dividing by len(word_list)
    for i in lpMap:
        for pos in lpMap[i]:
            lpMap[i][pos] = lpMap[i][pos]/len(word_list)
    return lpMap
lpMap = createLetterPosMap(wordList)
curatedLpMap = createLetterPosMap(curatedWordList)
print(lpMap)


# In[29]:


plt.style.use('seaborn-white')
def createHeatmap(lpMap, robust=False):
    df = pd.DataFrame(lpMap)
    h = sns.heatmap(df, 
                    cmap='rocket',
                    robust=robust,

                   )
    plt.gcf().set_size_inches((6, 12))
    return h


# In[ ]:





# In[30]:


createHeatmap(lpMap)
plt.ylabel('Letter', fontsize=18)
plt.xlabel("Letter freq per position", fontsize=18)


# In[31]:


createHeatmap(curatedLpMap)
plt.ylabel('Letter', fontsize=18)
plt.xlabel("Letter freq per position", fontsize=18)


# In[32]:


# In[ ]:




