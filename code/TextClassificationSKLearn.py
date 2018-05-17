#Learning a sentiment classifier from text.

from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer, TfidfVectorizer

# classifiers
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score,cross_val_predict,StratifiedKFold

import string,os
from nltk import word_tokenize
from nltk.stem.snowball import PorterStemmer

import pickle
from sklearn.externals import joblib

#Stemming. Optional.
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

#Remove punctuation, and perform stemming - again, optional. Just a choice I made.
#You can build a classifier without doing these - it will work, may be not as efficiently.
def removepunct_tokenize_stem(text):
    text = "".join([ch for ch in text if ch not in string.punctuation]) #Remove punctuation
    tokens = word_tokenize(text)
    stemmer = PorterStemmer()
    final = stem_tokens(tokens, stemmer)
    return final

#Read the training file and do the required pre-processing
def getData(file_path):
    #col1: Move cat. #last col: Text
    fh = open(file_path)
    texts = []
    cats = []
    fh.readline() #Header
    for line in fh:
        temp = line.split(",")
        text = " ".join(temp[1:])
        texts.append(" ".join(removepunct_tokenize_stem(text)))
        cats.append(temp[0])
    fh.close()
    return texts,cats

#Learns a classifier with the specified features in CountVectorizer, and shows the accuracy of the model
def classify_data(texts,cats):
    vectorizer =  CountVectorizer(analyzer = "word", tokenizer = None, preprocessor = None, stop_words = None, ngram_range=(1,2), min_df=10)
   # classifier =  LinearSVC(max_iter=500,C=0.1,class_weight="balanced")
    classifier = LogisticRegression(max_iter=100,class_weight="balanced",random_state=1234)
    train_vector = vectorizer.fit_transform(texts).toarray()
    k_fold = StratifiedKFold(10)
    #text_clf = Pipeline([('vect', vectorizer), ('clf', classifier)])
    cross_val = cross_val_score(classifier, train_vector, cats, cv=k_fold, n_jobs=1)
    print(vectorizer.get_feature_names()) #Prints names of features.
    print("Done with model building: ")
    print(cross_val)
    print(sum(cross_val)/len(cross_val))

#Same as above, but also saves the model so that we can use it again.
def save_model(texts,cats,model_file):
    vectorizer =  CountVectorizer(analyzer = "word", tokenizer = None, preprocessor = None, stop_words = None, ngram_range=(1,2), min_df=10)
   # classifier =  LinearSVC(max_iter=500)
    classifier = LogisticRegression(max_iter=100,class_weight="balanced",random_state=1234)
    pipeline = Pipeline([('vectorizer', vectorizer), ('pac', classifier)])
    pipeline.fit(texts,cats)
    joblib.dump(pipeline, model_file)
    print("Model saved as: ", model_file)


def main():
    training_file = "../data/movie-pang02.csv"
    training_data, training_labels = getData(training_file)
    print("Training vector created")
    classify_data(training_data,training_labels)
    save_model(training_data,training_labels,"../generatedfiles/sentimentmodel.pkl")

if __name__== "__main__":
    main()
