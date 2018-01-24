### Brief explanation of the steps I took to complete this task

My approach in steps:

1)I have read the data into pandas dataframe to easily access the columns I need.
2) I extracted the features of the sequences : at first I tried to map letters to numbers, but it makes no sense cause these letters are amino acids in proteins and we can use it to get more information from sequence. My approach is to count how many of each amino acid type are in a given sequence. I groupped them into 5 groups: aliphatic, aromatic, acidic, basic and other (the ones that don't belong to any group). 

Aliphatic - alanine,glycine, isoleucine, leucine, proline, valine 
Aromatic - phenylalanine  , tryptophan  , tyrosine  
Acidic - aspartic acid  , glutamic acid  
Basic - arginine  , histidine  , lysine

I have written a function that returns an array of how many amino acids of each group are in the given sequence and used it in training the model.

3)Splitting data
To evaluate the quality of the model we have to check how it works when we know the scores.
That is why I split the dataset into test and train groups and check how well the model classified on test set. 

3) Choosing the model
Here I chosed SVC but I did not have enough time to think of it more, there are many options here.  

6) Model evaluation 
Checking the accuracy to find out how well the model predicts

7) Predicting unknown values.


