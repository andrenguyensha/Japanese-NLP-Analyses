# Japanese-NLP-Analyses
WIP 


me and michael build web app that does simple jp text analysis.
project meant to teach me how to 1) use docker/aws/heroku 2) word tokenization on individual japanese sentences
3) frequency analysis 4) quick conversion of japanese sentences.



Take 日本語 .txt file, outputs all present tense, past-tense sentences, and changes all past tense to present-tense.


Further application: Scrape .json, .html files, perform transform. 


# Sources:

## MeCab / MeCab とは？
Mecab は京都大学情報学研究科−日本電信電話株式会社コミュニケーション科学基礎研究所 共同研究ユニットプロジェクトを通じて開発されたオープンソース 形態素解析エンジンです.
MeCab is an open source Japanese morphological analysis engine developed by a joint partnership with Kyoto University Graduate School of Informatics and NTT.

## NEologd / NEologd とは？  　
多数のWeb上の言語資源から得た新語を追加することでカスタマイズした MeCab 用のシステム辞書です。NEologd is a system dictionary for MeCab customized by adding new words from several web language resources. 
https://github.com/neologd/mecab-ipadic-neologd 

## Kairozu.github.io for Japanese Tokenization Tutorial 

## Fugashi 
@inproceedings{mccann-2020-fugashi,
    title = "fugashi, a Tool for Tokenizing {J}apanese in Python",
    author = "McCann, Paul",
    booktitle = "Proceedings of Second Workshop for NLP Open Source Software (NLP-OSS)",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.nlposs-1.7",
    pages = "44--51",
    abstract = "Recent years have seen an increase in the number of large-scale multilingual NLP projects. However, even in such projects, languages with special processing requirements are often excluded. One such language is Japanese. Japanese is written without spaces, tokenization is non-trivial, and while high quality open source tokenizers exist they can be hard to use and lack English documentation. This paper introduces fugashi, a MeCab wrapper for Python, and gives an introduction to tokenizing Japanese.",
}　


macOS の場合:
To install NEologd and MeCab:

brew install mecab mecab-ipadic
pip3 install 'fugashi[unidic]'
