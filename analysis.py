import MeCab
from collections import Counter                             # for counting most common elements

# tag mecab-ipadic-neologd dictionary
mct = MeCab.Tagger("-O chasen -d andre/mecab-ipadic-neologd/") #Fix this, error is that the path file not found

# simple recreation of previous MeCab command line tests; parse and tokenize sentence
print(mct.parse('今日は。私はアンドレです。'))

read_text = open('.txt', 'r').read()              # Read .txt file, japanese text.  

# split text into sentences on '。' character, and then replace the ending '。' on all sentences
text_lines = read_text.split('。')
text_lines = [x + '。' for x in text_lines if len(x) > 0]

nouns = []                                                  # create empty lists for nouns, verbs, adjectives
verbs = []
adjectives = []

for sentence in text_lines:                                   # loop through each sentence in gh_lines
    jparse_bug = mct.parse(sentence)
    jparse = mct.parseToNode(sentence)

    while jparse:
        mct_split = jparse.feature.split(',')               # split features up by commas
        if mct_split[0] == '名詞':
            nouns.append(jparse.surface)                    
        elif mct_split[0] == '動詞':
            verbs.append(jparse.surface)                   
        elif mct_split[0] == '形容詞':
            adjectives.append(jparse.surface)               
        jparse = jparse.next                                # move on to the next word-token

noun_counts = str(Counter(nouns).most_common(5))            
verb_counts = str(Counter(verbs).most_common(5))            
adjective_counts = str(Counter(adjectives).most_common(5))  

print(noun_counts)                                          
print(adjective_counts)                                     
print(verb_counts)                                          