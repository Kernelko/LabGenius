
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import accuracy_score

def reading():
    """read file into dataframe"""

    df = pd.read_csv("TRAINING_SET.csv", names = ["sequence", "score"])
     #read into dataframe
    x_train = df["sequence"][:]
    y_train = df["score"][:]
    return x_train, y_train

x_train, y_train = reading()


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

##SPLITTING THE DATA

X_train, X_test, y_train, y_test = train_test_split(x_train_groupped, y_train, test_size=0.33, random_state=42)
print(len(X_train), len(X_test))

##Choosing the classifier 

clf = RandomForestClassifier()

##classifying on train set

clf.fit(X_train, y_train)

## testing on test

y_predicted = clf.predict(X_test)

##results 

print(accuracy_score(y_test, y_predicted))


#PREDICTION

df_problem= pd.read_csv("PROBLEM_SET.csv", names = ["sequence"])
x_train_problem = df_problem["sequence"][:]
x_train_problem_groupped = []

for sequence in x_train_problem:
    x_train_problem_groupped.append(feature_selector(sequence))

y_predicted_problem = clf.predict(x_train_problem_groupped)

df_problem["predicted_scores"] = y_predicted_problem

df_problem.to_csv("result.csv", columns = ["sequence", "predicted_scores"])