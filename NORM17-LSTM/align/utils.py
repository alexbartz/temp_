#!/usr/bin/python
import re
import pie_fr_tokenizer

pie_tokeniser = pie_fr_tokenizer.FrMemorizingTokenizer()

def basic_tokenise(string):
    # separate punctuation
    for char in r',.;?!:)(-—–—―‒"':
        string = re.sub('(?<! )' + re.escape(char), ' ' + char, string)
    for char in '\'"’':
        string = re.sub(char + '(?! )' , char + ' ', string)
    return string.strip()

def tokenise(string):
    return '\n'.join([' '.join(sent) for sent in pie_tokeniser.sentence_tokenizer(string.strip())])

