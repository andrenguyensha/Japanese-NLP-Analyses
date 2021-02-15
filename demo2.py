import streamlit as st
from collections import Counter 
import re
import MeCab

# tag mecab dictionary
mct = MeCab.Tagger('-r /dev/null -d /usr/local/lib/mecab/dic/dicrc') 

"""
Input the text that you'd like to analyze. 
"""

text = st.text_area("input", "はじめました。私はアンドレでした。")                

# split text into sentences on '。' character, and then replace the ending '。' on all sentences
lines = text.split('。')
lines = [x + '。' for x in lines if len(x) > 0]

past = set()                                                        

for sentence in lines:                                           # loop through sentences in lines
    jparse_bug = mct.parse(sentence)
    jparse = mct.parseToNode(sentence)

    while jparse:                                                   
        if jparse.posid == 25:                                      
            if jparse.surface == 'た':
                past.add(sentence)                                  # if 'た' was found, add to past-tense
        jparse = jparse.next                                        # move to the next word-token

present = set(lines) - past                                      # remove lines in past from lines


new_present = []                                                    # empty list for past-tense-to-present

# change all of the sentences in past-tense, to present-tense
for past_sentence in list(past):
    # change negative-past to negative, and postive-past to present
    now_present = re.sub('ませんでした', 'ません', past_sentence)
    now_present = re.sub('した', 'す', past_sentence)
    new_present.append(now_present)                                 # add to list new_present sentences


st.write("All past tense sentences as present tense", new_present)