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
