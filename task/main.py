""" Machine learning of proteins """

import pandas as pd
from string import ascii_letters
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score



def reading():
    """read file into dataframe"""

    df = pd.read_csv("TRAINING_SET.csv", names = ["sequence", "score"])
     #read into dataframe
    x_train = df["sequence"][:]
    y_train = df["score"][:]
    return x_train, y_train


"""
def map_protein_to_numbers(protein):
    letters = list(ascii_letters)
    numbers = list(range(len(ascii_letters)))
    map_dict = dict(zip(letters, numbers))
    result = []
    for letter in protein:
        result.append(map_dict[letter.lower()])
    return result

x_train_mapped =[]
for sequence in x_train:
    x_train_mapped.append(map_protein_to_numbers(sequence))

"""

x_train, y_train = reading()

### DIFFERENT APPROACH
"""
Aliphatic - A,G, I, L, P, V 
Aromatic - F  , W  , Y  
Acidic - D  , E  
Basic - R  , H  , K
"""

# Features are how many aliphatic, aromatic and acidic and basic are in sequence

def feature_selector(protein):
    """extract features from protein sequence: counts how many of each amino acid type protein has."""
    """returns an array with number of amino acids in protein from specific group in a form [Aliphatic, Aromatic, Acidic, Basic, Other]"""

    grouped = [("a", "g", "i","l", "p", "v"),("f", "w", "y"),("d", "e"),("r", "h", "k"), ("n", "c", "q", "m", "s", "t")]
    features_array = [0,0,0,0,0]

    for index in range(5):
        for letter in list(protein.lower()):
            if letter in grouped[index]:
                features_array[index] += 1
    return features_array

x_train_groupped = []

for sequence in x_train:
    x_train_groupped.append(feature_selector(sequence))

##ALL READ SO NOW SPLITTING THE DATA

X_train, X_test, y_train, y_test = train_test_split(x_train_groupped, y_train, test_size=0.33, random_state=42)
print(len(X_train), len(X_test))

##Choosing the classifier (should be SVG)

clf = svm.SVC()

##classifying on train

clf.fit(X_train, y_train)

## testing on test

y_predicted = clf.predict(X_test)

##results 

print(accuracy_score(y_test, y_predicted))

