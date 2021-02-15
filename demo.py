import streamlit as st
from collections import Counter 
import re
import MeCab

# tag mecab dictionary
mct = MeCab.Tagger('-r /dev/null -d /usr/local/lib/mecab/dic/dicrc') 

"""
Input the text that you'd like to analyze. 
"""
text = st.text_area("input", "はじめまして。私はアンドレです。よろしくお願いします。")

text_lines = text.split('。')
text_lines = [x + '。' for x in text_lines if len(x) > 0]

nouns = []                                                  # create empty lists for nouns, verbs, i-adjectives, and na-adjectives
verbs = []
i_adjectives = []
na_adjectives = []

for sentence in text_lines:                                   # For every sentence, loop through each sentence in lines
    jparse_bug = mct.parse(sentence)
    jparse = mct.parseToNode(sentence)

    while jparse:
        mct_split = jparse.feature.split(',')               # split features up by commas
        if mct_split[0] == '名詞':
            nouns.append(jparse.surface)                    
        elif mct_split[0] == '動詞':
            verbs.append(jparse.surface)                   
        elif mct_split[0] == '形容詞':
            i_adjectives.append(jparse.surface) 
        elif mct_split[0] == '形容動詞':
            na_adjectives.append(jparse.surface)              
        jparse = jparse.next                                # move on to the next word-token

noun_counts = str(Counter(nouns).most_common(5))            
verb_counts = str(Counter(verbs).most_common(5))            
i_adjective_counts = str(Counter(i_adjectives).most_common(5))  
na_adjective_counts = str(Counter(na_adjectives).most_common(5))


st.write("Noun Counts", noun_counts) #print 5 most common types and their counts. 
st.write("Verb Counts", verb_counts)
st.write("i-Adjective Counts", i_adjective_counts)
st.write("na-Adjective Counts", na_adjective_counts)