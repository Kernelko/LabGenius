""" Machine learning of proteins """

import pandas as pd
from string import ascii_letters

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




