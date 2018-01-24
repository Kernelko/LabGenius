""" Machine learning of proteins """

import pandas as pd
from string import ascii_letters

def training():
    "training function"

    df = pd.read_csv("TRAINING_SET.csv") #read into dataframe
    x_train = df.iloc[0,:] 
    y_train = df.iloc[:,0]
    return x_train[1:10]

def mapping(protein):
    letters = list(ascii_letters)
    numbers = list(range(len(ascii_letters)))
    map_dict = dict(zip(letters, numbers))
    result = []
    for letter in protein:
        result.append(map_dict[letter.lower()])
    return result

cos = training()
mapping(cos)
