import os
import pandas as pd
import re
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import one_hot
from nltk.stem.porter import PorterStemmer


ps = PorterStemmer()

df_train = pd.read_csv(os.path.join('test.csv'))
index = 4

x = pd.DataFrame([[df_train['title'][index], df_train['text'][index]]], columns= ['title', 'text'])

corpus_title = []
corpus_text = []

for i in range(0, len(x)):

    # Replacing all characters other than the letters([^a-zA-Z]) with spaces in title and text of each iteration
    title = re.sub('[^a-zA-Z]', ' ', x['title'][i])
    text = re.sub('[^a-zA-Z]', ' ', x['text'][i])

    # Converting into lower case
    title = title.lower()
    text = text.lower()
    title = [ps.stem(word) for word in title]
    text = [ps.stem(word) for word in text]

    # To join all the individual words into a sentence by joining them with spaces
    title= ' '.join(title)
    text= ' '.join(text)


    corpus_title.append(title)
    corpus_text.append(text)
    
# Combiing the words and title into a single entity
corpus = []
for i in range(0, len(corpus_title)):
    corpus.append(corpus_title[i]+ '          '+ corpus_text[i])

voc_size = 30000
# Large length as we've both title and text
max_len = 3000

# Converting into one hot representation
one_hot_rep = [one_hot(lines, voc_size) for lines in corpus]

# Adding padding to later pass to embedding layers
embed_inp = pad_sequences(one_hot_rep, max_len, padding='pre')


from tensorflow.keras.models import load_model
model = load_model(os.path.join('Models', 'Model.h5'))

prediction = model.predict(embed_inp)

if prediction > 0.5:
    print("\nThis is fake news!!")
else:
    print("\nThis news is genuine")