
#Text classification example

import string,os,pprint
from nltk import word_tokenize
from nltk.stem.snowball import PorterStemmer

import pickle
from sklearn.externals import joblib

#This is perhaps not necessary for the example corpus I took - it seems like it is already pre-processed.
def removepunct_tokenize_stem(text):
    text = "".join([ch for ch in text if ch not in string.punctuation]) #Remove punctuation
    tokens = word_tokenize(text)
    stemmer = PorterStemmer()
    final = [stemmer.stem(item) for item in tokens]
    return final

#Takes a test data file, Shows probability for the prediction, distribution across all classes.
def makePredictionsTest(file_input,file_output,classifier):
    fh = open(file_input)
    fho = open(file_output,"w")
    for line in fh:
        temp = line.split(",")
        text = " ".join(temp[1:])
        cat = temp[0]
        converted = [" ".join(removepunct_tokenize_stem(text))]
        all_predictions = list(classifier.predict_proba(converted)[0])
        predict_prob = max(all_predictions)
        prediction = classifier.predict(converted)[0]
        print(text[1:50]+"...", cat, prediction)
        fho.write(cat + "\t" + prediction + "\t" + str(predict_prob) + "\t" + ",".join([str(prob) for prob in all_predictions]))
        fho.write("\n")
    fh.close()
    fho.close()

#Makes prediction for a single string.
def makePredictionsForAString(inputstr,classifier):
    converted = [" ".join(removepunct_tokenize_stem(inputstr))]
    print(converted)
    all_predictions = list(classifier.predict_proba(converted)[0])
    predict_prob = max(all_predictions)
    print(predict_prob)
    prediction = classifier.predict(converted)[0]
    print(inputstr[:50]+"...", prediction)

def main():
    model_file = "generatedfiles/sentimentmodel.pkl"
    test_file = "data/movie-pang02-Test.csv"
    classifier = joblib.load(model_file)
    count = 0
   # makePredictionsTest(test_file,"temp.csv",classifier)
    makePredictionsForAString("Superb! Brilliant! I really like this movie. It was a pleasant surprise to see this!", classifier)

if __name__ == "__main__":
    main()
