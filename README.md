# Japanese-NLP-Analyses

Built a simple web app deployed onto Streamlit.io that does simple jp text analysis.
This is just a passion project meant to teach me how to 1) deploy apps 2) word tokenization on individual japanese sentences
3) frequency analysis 4) quick conversion of japanese sentences.


The first demo app (demo.py) is a frequency analysis project that parses through every sentence, bins them into its respective type (noun, verb, i/na-adj),
and then displays the 5 most frequent appearances and their count. 

The second demo app (demo2.py) outputs all present tense, past-tense sentences, and changes all past tense to present-tense sentences. 



# Sources:

## MeCab / MeCab とは？


Mecab は京都大学情報学研究科−日本電信電話株式会社コミュニケーション科学基礎研究所 共同研究ユニットプロジェクトを通じて開発されたオープンソース 形態素解析エンジンです.
MeCab is an open source Japanese morphological analysis engine developed by a joint partnership with Kyoto University Graduate School of Informatics and NTT.
For these app I tagged the default MeCab dictionary. 

## Kairozu.github.io for a clear cut Japanese Tokenization Tutorial.

