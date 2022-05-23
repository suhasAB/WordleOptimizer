#!/usr/bin/env python
# coding: utf-8

# # Wordle

# ## Solving method

# In[18]:


import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from tqdm.notebook import tqdm
from collections import defaultdict
import ipywidgets as widgets
from ipywidgets import interactive_output, fixed


# In[19]:


with open('./data/processed/wordle-answers-alphabetical.txt', 'r') as file:
    possible_answers = file.read().splitlines() 
   
with open('./data/processed/wordle-allowed-guesses.txt', 'r') as file:
    words_allowed_guesses = file.read().splitlines() 
words_allowed_guesses = words_allowed_guesses + possible_answers

print("Number of possible answer words:", len(possible_answers))
print("Number of accepted guess words:", len(words_allowed_guesses))


# In[20]:


letters = [letter for letter in "azertyuiopqsdfghjklmwxcvbn"]
letter_imgs = {letter: mpimg.imread(f"letters/{letter}.png") for letter in letters}

def display_word(word):
    if word == "": return
    letters = [letter_imgs[letter] for letter in word]
    plt.figure()
    plt.imshow(np.concatenate(letters, axis=1))
    plt.axis('off')
    plt.show()


# In[21]:


display_word("hello")


# In[22]:


def compare_words(query_word, answer_word):
    res = []
    pos_not_found = []
    letters_not_found = []
    for (i, letter1), letter2 in zip(enumerate(query_word), answer_word):
        if letter1 == letter2:
            res.append('2')
        else:
            res.append('0')
            pos_not_found.append(i)
            letters_not_found.append(letter2)
    for i in pos_not_found:
        if query_word[i] in letters_not_found:
            res[i] = "1"
            letters_not_found.remove(query_word[i])
    return "".join(res)


# In[23]:


compare_words("raise", "gorge")


# In[24]:


compare_words("crane","crane")


# In[25]:


def filter_words(possible_words, word, comparison_string):
    new_possible_words = []
    for w in possible_words:
        if compare_words(word, w) == comparison_string:
            new_possible_words.append(w)
    return new_possible_words


# In[26]:


print(filter_words(possible_answers, "raise", "10002"))


# $ score(word) = \sum_{letter  \in  word}\frac{1}{rank(letter)} $

# In[27]:


letters_by_frequency = "eariotnslcudpmhgbfywkvxzjq"
letters_scores = {letter: 1/(i+1) for i, letter in enumerate(letters_by_frequency)}
    
def score_RelativeFreq_ofWord(word):
    score = 0
    for letter in set(word):
        score += letters_scores[letter]
    return score


# In[28]:


print("raise:", score_RelativeFreq_ofWord("raise"))
print("bumpy:", score_RelativeFreq_ofWord("bumpy"))


# In[30]:


def solver_RelativeFrequency_method(comparison_string, word, possible_words):
    possible_words = filter_words(possible_words, word, comparison_string)
    if len(possible_words) == 0:
        print("No possible word in vocabulary.")
        return "", []
    else:
        words_sorted = sorted(possible_words, key=score_RelativeFreq_ofWord, reverse=True)
        word = words_sorted[0]
        return word, possible_words


# ## Improved solving method by combining Entropy with Relative Frequency

# ![Score](entropyBasedScore.png)

# In[31]:


def score_EntropyRelFreqCombo_OfWord(query_word, possible_words):
    nb_words = len(possible_words)
    comparison_dict = defaultdict(int)
    for word in possible_words:
        comparison_dict[compare_words(query_word, word)] += 1
    return sum(word_count / nb_words * word_count for word_count in comparison_dict.values())


# In[32]:


print(score_EntropyRelFreqCombo_OfWord("crane",possible_answers))


# In[33]:


def best_starting_word(possible_guesses, possible_answers, topn=20):
    word_scores = []
    for word in tqdm(possible_guesses):
        word_scores.append((word, score_EntropyRelFreqCombo_OfWord(word, possible_answers)))
    word_scores = sorted(word_scores, key=lambda x: x[1])
    for i in range(topn):
        print(f"{word_scores[i][0]} : {word_scores[i][1]}")
        


# In[34]:


best_starting_word(words_allowed_guesses, possible_answers,topn=20)


# In[35]:


best_20_starting_words=["roate","raise","raile","soare","arise","irate","orate","ariel","arose","raine","artel","taler","ratel","aesir","arles","realo","alter","saner","later","snare"]


# In[36]:


def solver_EntropyRelFreqCombo_method(comparison_string, word, possible_words):
    possible_words = filter_words(possible_words, word, comparison_string)
    if len(possible_words) == 0:
        print("No possible word in vocabulary.")
        return "", []
    else:
        words_sorted = sorted(possible_words, key=lambda x: score_EntropyRelFreqCombo_OfWord(x, possible_words))
        word = words_sorted[0]
        return word, possible_words
    
    
def solver_AdvancedEntropyRelFreqCombo_method(comparison_string, word, possible_words):
    possible_words = filter_words(possible_words, word, comparison_string)
    if len(possible_words) == 0:
        print("No possible word in vocabulary.")
        return "", []
    else:
        if len(possible_words) <= 3:
            words_sorted = sorted(possible_words, key=lambda x: score_EntropyRelFreqCombo_OfWord(x, possible_words))
        else:
            words_sorted = sorted(words_allowed_guesses, key=lambda x: score_EntropyRelFreqCombo_OfWord(x, possible_words))
        word = words_sorted[0]
        return word, possible_words


# ## Evalutating solutions

# In[37]:


def test_solution(answer_word, solver_method_type, starting_word="tares"):
    word = starting_word
    possible_words = possible_answers
    attempts = 1
    while attempts < 20:
        if word == answer_word:
            return attempts
        attempts += 1
        comparison_string = compare_words(word, answer_word)
        word, possible_words = solver_method_type(comparison_string, word, possible_words)
    return attempts

def evaluate_solver(possible_words, solver_method_type, starting_word="mount"):
    solves = []
    for word in tqdm(possible_answers):
        solves.append((word, test_solution(word, solver_method_type, starting_word=starting_word)))
    mean_attempts = sum([solve[1] for solve in solves])/len(solves)
    print(f"Mean number of attempts: {mean_attempts} accross {len(solves)} games") 
    failed = [solve[0] for solve in solves if solve[1] > 6]
    print(f"Failed words (more than 6 attempts): {len(failed)}")
    print(", ".join(failed))


# In[38]:


evaluate_solver(possible_answers, solver_EntropyRelFreqCombo_method, starting_word="raise")


# In[39]:


print("Evaluating Entropy+Relative Frequency method for 10 different starting words")
for word in best_20_starting_words[:10]:
    print("Starting word:- ",word)
    evaluate_solver(possible_answers,solver_EntropyRelFreqCombo_method,starting_word=word)
    print("------------------------------------------------------------------------------")


# In[40]:


evaluate_solver(possible_answers, solver_EntropyRelFreqCombo_method, starting_word="tares")


# In[41]:


evaluate_solver(possible_answers, solver_EntropyRelFreqCombo_method, starting_word="crane")


# In[42]:


test_solution("alone",solver_EntropyRelFreqCombo_method,starting_word="crane")


# In[46]:


test_solution("alone",solver_AdvancedEntropyRelFreqCombo_method,starting_word="crane")


# In[47]:


evaluate_solver(possible_answers,solver_AdvancedEntropyRelFreqCombo_method,starting_word="roate")


# In[3]:


get_ipython().system('jupyter nbconvert 02-Entropy+RelativeFrequencyMethod-SuhasAnand.ipynb --to python')


# In[ ]:




