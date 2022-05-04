# 1. Project Title: Wordle Optimizer

## Professor: 
Carlos Rojas

## Term: 
Spring 2022

## Team Number: 
9

## Team Members:
- Abhishek Reddy (https://github.com/abhishekri)
- Ayush Gupta (https://github.com/aygupta9800)
- Suhas Anand Balagar (https://github.com/suhasAB)
- Milan Mohan Joshi (https://github.com/Milan-Joshi)

## 2. What data you’ll use and where you’ll get it?
- Scraping for all possible words on Sources tab of website (https://www.nytimes.com/games/wordle/index.html)
- Dataset involves upto 13,000 Valid English words with 5 letters each.

## 3. Description of the problem you’ll solve or the question you’ll investigate.
## Problem Statement:
Analysing Wordle Game Strategies using Information Theory (Entropy based) and optimising predictions.

## About Wordle game:
Wordle is an online word guessing game,originally created by Software Engineer Josh Wardle and currently published by The New York Times Company since 2022.wherein a new 5 letter word is set by the game each day and it is supposed to be guessed by players within 6 tries. User gets feedback about the closeness of his/her guess by 3 color indicators. Green on a block suggests the letter exists in the target word and is in the exact position the player has guessed, Yellow indicates the letter exists in the target word, but not in the position the player has guessed. Grey indicates the letter doesn't exist in the target word. Using these clues,Players are supposed to make better guesses in the remaining guesses to get to the target word in the minimum number of guesses.
Entropy provides a measure of the average amount of information needed to represent an event drawn from a probability distribution for a random variable.Entropy depends on probability. Probability Distribution in this case refers to the possibility of picking correct letters in Valid 5 Letter Words and Entropy of a guess would be the Net Entropy of all 5 letters in the guess.

Equation of Entropy can be calculated using the formula:

![Entropy H(X)](https://miro.medium.com/max/622/1*0wBPOiYyyPV8m4BiAkBbMQ.jpeg)

## 4. Proposed Project Work Summary
We plan on analysing the game by exploring the trends and patterns in the 5 letter dataset,using Information theory concepts such as Entropy to deduce information gained from each guess and the best possible strategies to guess given the entropy calculated from the previous guesses. The goal is to come up with guesses having maximum entropy, i.e providing the most information so that we can use that information to make better guesses.This reduces the number of possible words in each turn. We also plan on exploring strategy og combining Entropy with Probability of Relative word Frequency of the possible words for guesses at each stage. The model should be able to come up with minimal and Informative guesses before reaching the target word.

## 5. Introduction

## 6. Methods:

### 6.1. Heatmap for letter vs position in word:

We tried to analyse the frequency of each letter at position from 1 to 5 in 5 letter all-words list and curated word list given by wordle creators.
We calculated the total count at each position of letter and then calculated normalized frequency which would be from 0 to 1. Then we plot heatmap between alphabets and the position with color codes showing the frequency of letter. 

![Heatmap frequency vs position](https://github.com/suhasAB/WordleOptimizer/blob/main/paper/images/heatmap-curated-words-freq-of-letter-per-pos.png)

Through this heatmap we can understand, that in curated word list, at pos 1, s has the most no. of words. similarly at pos 5, e and y has most words. so trying a word starting with s and ending with e or y can be a good first guess to remove the possible words after the first guess. Thus improving our chance to get maximum entropy gain.  This visualization is done on curated words list of 2315 words as opposed to total 12,972 possible guesses in Wordle. We chose to focus only on the possible winning answers for the analysis because our goal is to find the best guesses for human player. While some might think, we are biasing toward only those words that can win, we have counter argument that all possible correct answer words are known beforehand, so using them is valid and good strategy toward reaching final answer.

### 6.3. Frequency map for most common words found in books:

In this method, the aim was to find the most frequent five letter words which are used in the books and are also present in wordle words. So, I got the data for the frequency of google books common words. As this data contains word lengths of other than five, I put a check to add only five letter words to the list. I mapped the words in the wordle list and curated words list to the list of five-letter words with frequency. Then I plotted the horizontal bar graph with curated words on the y-axis over frequency on the x-axis. 

![Heatmap frequency vs position](https://github.com/suhasAB/WordleOptimizer/blob/main/paper/images/Frequency_Map.jpeg)

The above bar graph shows the top 20 most frequently used words. We are anticipating that using the word for our first guess based on the relative frequency of the word with entropy combined is a good strategy to reduce the number of possible words for the next guess.


