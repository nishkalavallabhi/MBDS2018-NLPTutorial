"""
Purpose: Illustrate doing linguistic analyses in Python with Spacy.
"""

"""
Refer to these for additional examples:
https://spacy.io/usage/models
https://spacy.io/usage/linguistic-features
https://spacy.io/usage/processing-pipelines
https://spacy.io/usage/examples
"""

import spacy
from spacy import displacy
from nltk.tokenize import sent_tokenize

#Tokenization
def justtokenize(content, nlp):
    sentences = nlp(content, disable=['parser', 'tagger', 'ner'])
    for sentence in sentences:
        print(sentence)

#Sentence splitting
def sentences(spacified):
    for sent in spacified.sents:
        print(sent)

#Using a POS tagger
def tagger(spacified):
    for token in spacified:
        print(token.text, token.lemma_, token.pos_)

#Display a parse tree
def showparsetree(sentence):
    displacy.serve(sentence, style='dep')

#Print noun chunks
def nounchunks(content,nlp):
    sentences = sent_tokenize(content)
    for sentence in sentences:
        print(sentence.strip())
        spacified = nlp(sentence.strip())
        for nc in spacified.noun_chunks:
            print(nc)
        print("")

#Print entities
def entities(content,nlp):
    sentences = sent_tokenize(content)
    for sentence in sentences:
        print(sentence.strip())
        spacified = nlp(sentence.strip())
        for entity in spacified.ents:
            print(entity.text, entity.label_,sep="\t")
        print("")


def main():
    nlp = spacy.load('en_core_web_sm')
    content = open("../data/text1.txt").read()
    doc = nlp(content) #This is where all linguistic analysis happens - tokenizing, tagging, ner
    #tagger(doc)
    #sentences(doc)
    #justtokenize(content,nlp)
    #showparsetree(nlp("This is a small sentence to show how a dependency tree looks like."))
    #nounchunks(content,nlp)
    entities(content,nlp)


if __name__== "__main__":
    main()

