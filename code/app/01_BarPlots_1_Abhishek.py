#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[12]:


dframe_correct_guess = pd.read_csv("/data/processed/valid_guesses.csv")

dframe_correct_solutions = pd.read_csv("data/processed/valid_solutions.csv")

dframe_answers_text = pd.read_csv("data/proceed/wordle.txt", header=None)

dframe_answers = pd.DataFrame(dframe_answers_text)


# In[13]:


print("Total No.Of Correct Wordle Guesses:", len(dframe_correct_guess), "\nTotal No.Of Correct Wordle Solutions:",len(dframe_correct_solutions), "\nNo.Of Past Wordle Solutions:",len(dframe_answers))


# In[14]:


df_vg = dframe_correct_guess['word'].str.split('',n=5,expand=True)
del(df_vg[0])
df_vs = dframe_correct_solutions['word'].str.split('',n=5,expand=True)
del(df_vs[0])
df_pw = dframe_answers[0].str.split('',n=5,expand=True)
del(df_pw[0])


# In[15]:


dframe_vg_number = df_vg.apply(pd.Series.value_counts)

dframe_vg_number[6] = dframe_vg_number.sum(1)
dframe_vg_number = dframe_vg_number.fillna(0)

dframe_vs_number = df_vs.apply(pd.Series.value_counts)
dframe_vs_number[6] = dframe_vs_number.sum(1)
dframe_vs_number = dframe_vs_number.fillna(0)

dframe_pw_number = df_pw.apply(pd.Series.value_counts)
dframe_pw_number[6] = dframe_pw_number.sum(1)
dframe_pw_number = dframe_pw_number.fillna(0)

dframe_vg_number


# In[16]:


dframe_vg_frequency = dframe_vg_number
dframe_vs_frequency = dframe_vs_number
dframe_pw_frequency = dframe_pw_number

def calcFrac(df_freq, df_count):    
    for i in range(1, 7):
        df_freq[i] = df_count[i]/sum(df_count[i])*100
    df_freq.reset_index(inplace=True)
    df_freq['index'] = df_freq['index'].str.upper()
calcFrac(dframe_vg_frequency, dframe_vg_number)
calcFrac(dframe_vs_frequency, dframe_vs_number)
calcFrac(dframe_pw_frequency, dframe_pw_number)

dframe_vs_frequency


# #### Importing the dataset and view it. Each word is split up into 5 different columns so each column is a slot in a 5 letter word.

# def countUnique(dfUnique):
#     return pd.DataFrame(zip(*np.unique(dfUnique.to_numpy().flatten(),return_counts=True)), columns = ['letter', 'count'])
# 
# df_vg_unique = countUnique(df_vg)
# df_vs_unique = countUnique(df_vs)
# df_pw_unique = countUnique(df_pw)
# 
# df_vg_slots = {}
# df_vs_slots = {}
# df_pw_slots = {}
# 
# for i in range(1, 6):
#     df_vg_slots['slot%s'%i] = countUnique(df_vg[[i]])
#     df_vs_slots['slot%s'%i] = countUnique(df_vs[[i]])
#     df_pw_slots['slot%s'%i] = countUnique(df_pw[[i]])

# In[36]:


plt.figure(figsize=(25,5), dpi=80)
wd = 0.3
X_letter = np.arange(len(dframe_vg_frequency))

# green + blue
plt.bar(X_letter-wd, dframe_vg_frequency[6], width=wd, color = '#FF4500')

#plt.bar(X_letter-wd, dframe_vg_frequency[6], width=wd)

# blue
plt.bar(X_letter, dframe_vs_frequency[6], width=wd, color = '#98FB98')

# yellow
plt.bar(X_letter+wd, dframe_pw_frequency[6], width=wd, color = '#20B2AA')

plt.xticks(X_letter, dframe_vg_frequency['index'])
plt.title('Frequency of Letters')
plt.xlabel('Letter')
plt.ylabel('Frequency [%]')
plt.legend(['Viable Wordle Guesses', 'Viable Wordle Solutions', 'Previous Wordle Solutions'], title='Data Sources')
plt.grid()
plt.show()


# In[18]:


fig, ax = plt.subplots(6,1)
fig.set_figheight(20)
fig.set_figwidth(20)
fig.tight_layout(pad=5)

wd = 0.3
X_letter = np.arange(len(dframe_vg_frequency))

titles = ['Slot 1 Frequencies','Slot 2 Frequencies','Slot 3 Frequencies','Slot 4 Frequencies','Slot 5 Frequencies','Total Frequencies']

for i in range(0,6):
    ax[i].bar(X_letter-wd, dframe_vg_frequency[i+1], width=wd)
    ax[i].bar(X_letter, dframe_vs_frequency[i+1], width=wd)
    ax[i].bar(X_letter+wd, dframe_pw_frequency[i+1], width=wd)
    ax[i].set_xticks(X_letter, dframe_vg_frequency['index'])
    ax[i].set_xlabel('Letter',fontsize=13)
    ax[i].set_ylabel('Frequency [%]',fontsize=13)
    ax[i].tick_params(labelsize=13)
    ax[i].grid()
    ax[i].legend(['Legal Words', 'Viable Wordle Solutions', 'Previous Wordle Solutions'], title='Data Sources')
    ax[i].set_title(titles[i])


# In[ ]:




