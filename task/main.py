""" Machine learning of proteins """

import pandas as pd
from string import ascii_letters
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split



def reading():
    """read file into dataframe"""

    df = pd.read_csv("TRAINING_SET.csv", names = ["sequence", "score"])
     #read into dataframe
    x_train = df["sequence"][:]
    y_train = df["score"][:]
    return x_train, y_train

def map_protein_to_numbers(protein):
    letters = list(ascii_letters)
    numbers = list(range(len(ascii_letters)))
    map_dict = dict(zip(letters, numbers))
    result = []
    for letter in protein:
        result.append(map_dict[letter.lower()])
    return result

x_train, y_train = reading()

x_train_mapped =[]
for sequence in x_train:
    x_train_mapped.append(map_protein_to_numbers(sequence))

##ALL READ SO NOW SPLITTING THE DATA

X_train, X_test, y_train, y_test = train_test_split(x_train_mapped, y_train, test_size=0.33, random_state=42)
print(len(X_train), len(X_test))



"""
clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(x_train_mapped, y_train)
print(clf.feature_importances_)
"""


