#Sentence splitting, Tokenization and POS tagging with NLTK.
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.tag import pos_tag

content = open("../data/text1.txt").read()
sentences = sent_tokenize(content) #Sentence splitting
for sentence in sentences:
    #Splitting a sentence into words
    words_in_this_sentence = word_tokenize(sentence.strip())
    print(sentence.strip()) #Why?
    print(pos_tag(words_in_this_sentence))
    print()




