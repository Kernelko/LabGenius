### Task explained

This is a classification task: train a model based on results, predict some values.

things to do :
1) read the data
readed into pandas, cause it's easiest way to do it
we have two columns, protein sequence and score it gets

2) prepare the data
feature selection
sequence part is string, it's hard to do anything with it (it can be nlp, but it's not possible here since learning grammars for that would take ages)
so we have to map letters to numbers so it's possible to sklearn do soemthing with it.
It's not a perfect solution since letters actually mean something, maybe i will group it somehow later

lets try with acidic, basic, polar, non-polar

Aliphatic - alanine,glycine, isoleucine, leucine, proline, valine 
Aromatic - phenylalanine  , tryptophan  , tyrosine  
Acidic - aspartic acid  , glutamic acid  
Basic - arginine  , histidine  , lysine


3) split data into test and train 

to evaluate the quality of the model we have to check how it works when we know the scores.
That is why I split the dataset into test and train 
I am doing cross validation - this way I will repeat training on different splits of my dataset 

3) choose the model

Here I chosed support vector machine but it could be any other model

4) learn the model

5) evaluate  model

6) predict unknown values

