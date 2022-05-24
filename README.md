# Project Title: Wordle Optimizer
## Problem Statement:
Analysing Wordle Game Strategies using Information Theory concepts and optimising predictions to reduce Average number of guesses.

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


<details>
     <summary> Click to see more details from previous deliverable</summary>
     What data you’ll use and where you’ll get it?  <br>
     - Scraping for all possible words on Sources tab of website (https://www.nytimes.com/games/wordle/index.html) <br>
     - Dataset involves upto 13,000 Valid English words with 5 letters each. <br>
     - Curated list of 2315 words published by Game Developer's partner.
     
</details> 

## 1.Abstract:
Wordle is an online word guessing game,originally created by Software Engineer Josh Wardle and currently published by The New York Times Company since 2022.wherein a new 5 letter word is set by the game each day and it is supposed to be guessed by players within 6 tries. User gets feedback about the closeness of his/her guess by 3 color indicators. Green on a block suggests the letter exists in the target word and is in the exact position the player has guessed, Yellow indicates the letter exists in the target word, but not in the position the player has guessed. Grey indicates the letter doesn't exist in the target word. Using these clues,Players are supposed to make better guesses in the remaining guesses to get to the target word in the minimum number of guesses.
We plan on analysing the game by exploring the trends and patterns in the 5 letter dataset,using Information theory concepts such as Entropy to deduce information gained from each guess and the best possible strategies to guess given the entropy calculated from the previous guesses. The goal is to come up with guesses having maximum entropy, i.e providing the most information so that we can use that information to make better guesses.This reduces the number of possible words in each turn. We also plan on exploring strategy of combining Entropy with Probability of Relative word Frequency of the possible words for guesses at each stage. The model should be able to come up with minimal and Informative guesses before reaching the target word.

### We plan to use this preprocessed data to come up with 3 strategies to minimize the number of guesses.

### 1.1 Entropy based strategy(Reducing Possible words in each guess based on Entropy)  
For every possible word W, there are 3 ^ 5(5 letter in wordle and three for gray, yellow and green) possible patterns after guessing that word.
Each pattern p will result in a reduction of the possible candidate solutions to Sp, and the probability of obtaining this pattern is Sp / S where
S is the original possible candidate solutions.  
So we calculate the entropy for a specific possible guess using:  
#### H(w) = - ∑(p* log p) where p = Sp / S  
![Entropy H(X)](https://miro.medium.com/max/622/1*0wBPOiYyyPV8m4BiAkBbMQ.jpeg)
We can then guess word which has maximum entropy.
     
### 1.2 Entropy combined with Relative Frequency (To Optimize number of guesses considering Probability of Relative Frequency and Entropy)
### 1.3 Naive Approach based on Regular Expression.





## 2. Experiments and Analysis:


### 2.1. Extracting,Preprocessing and Curating Dataset:
In this method, primary aim is to get a list of all possible wordle answers i.e. 5 letter English words along with  other curated and Most frequent subsets. We used web scraping on the wordle website’s source JavaScript code to extract the list of all possible answers(5 letter words). There were around 12972 words in the list, and it is saved in multiple formats (json, text, csv )for further processing. 
We also found a curated list of 2315 words which were hand selected the game founder’s wife. 
We found a dataset from [Google books](http://norvig.com/google-books-common-words.txt) which maps the most common words in English language to it’s Frequency in Google books and other Online platforms. We filtered this dataset with just 5 letter words and arranged them in decreasing order of Frequency of words. We also normalized the frequency by dividing all frequencies with the maximum frequency to calculate and saved them in a new column called relative frequency.


### 2.2. Heatmap for letter vs position in word:

We tried to analyse the frequency of each letter at position from 1 to 5 in 5 letter all-words list and curated word list given by wordle creators.
We calculated the total count at each position of letter and then calculated normalized frequency which would be from 0 to 1. Then we plot heatmap between alphabets and the position with color codes showing the frequency of letter. 

![Heatmap frequency vs position](https://github.com/suhasAB/WordleOptimizer/blob/main/paper/images/heatmap-curated-words-freq-of-letter-per-pos.png)

Through this heatmap we can understand, that in curated word list, at pos 1, s has the most no. of words. similarly at pos 5, e and y has most words. so trying a word starting with s and ending with e or y can be a good first guess to remove the possible words after the first guess. Thus improving our chance to get maximum entropy gain.  This visualization is done on curated words list of 2315 words as opposed to total 12,972 possible guesses in Wordle. We chose to focus only on the possible winning answers for the analysis because our goal is to find the best guesses for human player. While some might think, we are biasing toward only those words that can win, we have counter argument that all possible correct answer words are known beforehand, so using them is valid and good strategy toward reaching final answer.


### 2.3. Frequency of Individual Characters as a Whole and in Different Wordle Slots

Broadly considering I plotted two visualizations. First is calculating the frequency of individual character, second is frequencies of characters in every slot of Wordle game. We considered three datasets to do this.

**Datasets**
  1) Valid Guesses
  This is a list of 13,000 words from the source code dataset.
  
  2) World Curated
  It is a curated list of words around 2,000 words that appear to be most frequent suggested by cofounder’s spouse. 
  
  3) Valid Solutions
  Contains a list of all words that have appeared each day as a solution.


![fre_each-char](https://github.com/suhasAB/WordleOptimizer/blob/main/paper/images/freq_each_updated1.png)

**1) Calculating Individual Character Frequency**

  I tried to analyze the frequency of different characters from all alphabets from A to Z. 
  
  a) Viable Wordle Guess
  Plotting the frequency of each character from the source dataset.
  
  b) Viable Wordle Solutions
  Analyzing each character frequency from the curated dataset list.
  
  c) Previous Wordle Solutions
  Similarly calculating the frequency of individual character based on previous wordle solutions.


**2) Calculating Frequency of Characters in all the Five Slots**

This is calculating the frequency of each character in different slots and also the combines frequency from the five slots.
Similar to the calculations we did in the step 1), we are doing it for 3 datasets.

![freq_slot-char](https://github.com/suhasAB/WordleOptimizer/blob/main/paper/images/freq_each_slot_updated1.png)

The whole idea is to optimize or reduce the number of tries or steps in playing game may be 3 or even less than that. To understand which dataset or even combined datasets to use, or on what frequency we should try to solve using entropy; we need to understand efficient possible ways of data sourcing.
Combining frequencies from different datasets of each character will help us to assign a priority or weightage to individual alphabet.



### 2.4. Frequency map for most common words found in books:

In this method, the aim was to find the most frequent five letter words which are used in the books and are also present in wordle words. So, I got the data for the frequency of google books common words. As this data contains word lengths of other than five, I put a check to add only five letter words to the list. I mapped the words in the wordle list and curated words list to the list of five-letter words with frequency. Then I plotted the horizontal bar graph with curated words on the y-axis over frequency on the x-axis. 

![Heatmap frequency vs position](https://github.com/suhasAB/WordleOptimizer/blob/main/paper/images/Frequency_Map.jpeg)

The above bar graph shows the top 20 most frequently used words. We are anticipating that using the word for our first guess based on the relative frequency of the word with entropy combined is a good strategy to reduce the number of possible words for the next guess.

## 3. Comparisions of Different Information Theory based Approaches

### 3.1 Regex approach

### 3.2 Relative Frequency based approach

### 3.3 Entropy based approach
The entropy is a good parameter to choose guess word as it splits our dictionary of possible words in a more consistent manner.  
For every possible word W, there are 3 ^ 5(5 letter in wordle and three for gray, yellow and green) possible patterns after guessing that word.
Each pattern p will result in a reduction of the possible candidate solutions to Sp, and the probability of obtaining this pattern is Sp / S where S is the original possible candidate solutions.  
So we calculate the entropy for a specific possible guess using:  
#### H(w) = - ∑(p* log p) where p = Sp / S
We can then guess word which has maximum entropy. 

We create wordPatternMap for each word. each word will have 243 patterns and next possible set of words for that pattern.
<img width="699" alt="Screen Shot 2022-05-23 at 4 29 58 PM" src="https://user-images.githubusercontent.com/55319952/169920383-8f97fc5d-41d5-4834-9f81-cb1a87e10e8e.png">

Then we use the entropy calculation for each possible word before the next guess and choose maximum entopy word as next guess.
<img width="699" alt="Screen Shot 2022-05-23 at 4 27 31 PM" src="https://user-images.githubusercontent.com/55319952/169920218-fa6e9262-8da1-497c-92b5-e9405b2d4e4d.png">

Then we try to simulate solving NYTimes wordle problem interactively by feeding best entropy word as guess word in wordle and putting feedback of grey, yellow and green letter in form of 0,1,2 in our notebook.
<img width="1383" alt="Solving-wordle-live-with-entropy-approach" src="https://user-images.githubusercontent.com/55319952/169921212-ead3845f-2970-4659-b579-71d72593fe03.png">

Next, we try to visualize guess count result from using 1000 trial sequence.

<p float="left">
  <img src="https://user-images.githubusercontent.com/55319952/169921362-ca3146ef-85ed-4ccd-97b0-26ea5ab1d94d.png" width="500" />
  <img src="https://user-images.githubusercontent.com/55319952/169921377-632a8324-c9e9-4e24-bf55-e77eba269447.png" width="500" /> 
<!--   <img src="/img3.png" width="100" /> -->
</p>
<!-- ![barh-for-no-of-guess-for-every-trial](https://user-images.githubusercontent.com/55319952/169921362-ca3146ef-85ed-4ccd-97b0-26ea5ab1d94d.png)
![pie-chart-to-show-guess-count-percentage](https://user-images.githubusercontent.com/55319952/169921377-632a8324-c9e9-4e24-bf55-e77eba269447.png)
-->

Results we found:  <br>
Average Guess Count = 3.7  <br>
Failure Rate(Guess count more than 6) = 1.1 %  <br>
Success Rate = 98.1 %<br>


### 3.3 Combination of Entropy and Relative Frequency:


## 4.Conclusion

- Regex Approach uses pattern matching to come up with guesses.

- Relative Frequency Approach employs choosing the best word possible for a given pattern after each guess.

- Entropy Based Approach tries to reduce the number of possible words after each guess.

- Combination of Entropy with Relative Frequency employs both Information gain and best word selection based on number of possible words remaining.

