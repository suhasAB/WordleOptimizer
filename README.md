# WordleOptimizer
## Problem Statement: Analysing Wordle Game Strategies using Information Theory(Entropy based) and optimising predictions using supervised learning.

## Team Members:
- Abhishek Reddy
- Ayush Gupta
- Suhas Anand Balagar
- Milan Mohan Joshi

## Dataset: Scraping for all possible words on Sources tab of website https://www.nytimes.com/games/wordle/index.html
Dataset involves upto 10,000 Valid English words with 5 letters each.

## Problem Statement: Analysing Wordle Game Strategies using Information Theory(Entropy based) and optimising predictions using supervised learning.

## About Wordle game:
Wordle is an online word guessing game,wherein a new 5 letter word is set by the game each day and it is supposed to be guessed by players within 6 tries. User gets feedback about the closeness of his/her guess by 3 color indicators. Green on a block suggests the letter exists in the target word and is in the exact position the player has guessed, Yellow indicates the letter exists in the target word,but not in the position the player has guessed. Grey indicates the letter doesn't exist in the target word. Using these clues,Players are supposed to make better guesses in the remaining guesses to get to the target word in the minimum number of guesses.
Equation of Entropy can be calculated using the formula:
![Entropy H(X)](https://miro.medium.com/max/622/1*0wBPOiYyyPV8m4BiAkBbMQ.jpeg)

## Proposed Project Work Summary: 
We plan on analysing the game by exploring the trends and patterns in the 5 letter dataset,using Information theory concepts such as Entropy to deduce information gained from each guess and the best possible strategies to guess given the entropy calculated from the previous guesses. The goal is to come up with guesses having maximum entropy, i.e providing the most information so that we can use that information to make better guesses. We also plan on using supervised learning models to predict the possible words for guesses at each stage,based on entropy calculations at each guess. The model should be able to come up with minimal and Informative guesses before reaching the target word.
