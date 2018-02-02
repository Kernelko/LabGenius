
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import accuracy_score
from string  import ascii_letters
from keras.models import Sequential  
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM


model = Sequential()
model.add(Dense(120, input_dim=10, activation='sigmoid'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

def reading():
    """read file into dataframe"""

    df = pd.read_csv("TRAINING_SET.csv", names = ["sequence", "score"])
     #read into dataframe
    x_train = df["sequence"][:]
    y_train = df["score"][:]
    return x_train, y_train

x_train, y_train = reading()

"""
# Features are how many aliphatic, aromatic and acidic and basic are in sequence
def feature_selector(protein):
    extract features from protein sequence: counts how many of each amino acid type protein has.
    returns an array with number of amino acids in protein from specific group in a form [Aliphatic, Aromatic, Acidic, Basic, Other]
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
"""

#INSTEAD OF GROUPING JUST MAP PROTEIN TO NUMBERS AND THEN LSTM
def map_protein_to_numbers(protein):
    letters = list(ascii_letters)
    numbers = list(range(len(ascii_letters)))
    map_dict = dict(zip(letters, numbers))
    result = []
    for letter in protein:
        result.append(map_dict[letter.lower()])
    return result

x_train_mapped = []
for sequence in x_train:
    x_train_mapped.append(map_protein_to_numbers(sequence))

##SPLITTING THE DATA

X_train, X_test, y_train, y_test = train_test_split(x_train_mapped, y_train, test_size=0.33, random_state=42)
print(len(X_train), len(X_test))

##classifying on train set

model.fit(np.array(X_train),np.array(y_train),
          epochs=20,
          batch_size=128)


## testing on test

y_predicted = model.predict(np.array(X_test))

##results 

print(accuracy_score(y_test, y_predicted))


#PREDICTION

#df_problem= pd.read_csv("PROBLEM_SET.csv", names = ["sequence"])
#x_train_problem = df_problem["sequence"][:]
#x_train_problem_groupped = []

#for sequence in x_train_problem:
#    x_train_problem_groupped.append(feature_selector(sequence))

#y_predicted_problem = clf.predict(x_train_problem_groupped)

#df_problem["predicted_scores"] = y_predicted_problem

#df_problem.to_csv("result.csv", columns = ["sequence", "predicted_scores"])
