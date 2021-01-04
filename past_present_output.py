import MeCab, re                                                   

mct = MeCab.Tagger('-r /dev/null -d /usr/local/lib/mecab/dic/dicrc') 
gh_text = open('grasshopper.txt', 'r').read()                       

# split text into sentences on '。' character, and then replace the ending '。' on all sentences
gh_lines = gh_text.split('。')
gh_lines = [x + '。' for x in gh_lines if len(x) > 0]

past = set()                                                        # create empty set for past-tense lines

for sentence in gh_lines:                                           # loop through sentences in gh_lines
    jparse_bug = mct.parse(sentence)
    jparse = mct.parseToNode(sentence)

    while jparse:                                                   
        if jparse.posid == 25:                                      
            if jparse.surface == 'た':
                past.add(sentence)                                  # if 'た' was found, add to past-tense
        jparse = jparse.next                                        # move to the next word-token

present = set(gh_lines) - past                                      # remove lines in past from gh_lines

print("Grasshopper and the Ant sentences in present-tense:")
[print(x) for x in present]                                         # "for every x in present, print x"
print("\nGrasshopper and the Ant sentences in past-tense:")
[print(x) for x in past]                                            # "for every x in past, print x"

new_present = []                                                    # empty list for past-tense-to-present

# change all of the sentences in past-tense, to present-tense
for past_sentence in list(past):
    # change negative-past to negative, and postive-past to present
    now_present = re.sub('ませんでした', 'ません', past_sentence)
    now_present = re.sub('した', 'す', past_sentence)
    now_present = re.sub('だった','だ', past_sentence)
    new_present.append(now_present)                                 # add to list new_present sentences

print("\nGrasshopper and the Ant sentences, past-to-present:")
[print(x) for x in new_present]                                     
