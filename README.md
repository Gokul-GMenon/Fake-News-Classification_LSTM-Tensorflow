# A Text Classification model built using Tensorflow
This is a NLP text classification based project. Here an LSTM model has been built using Tensorflow which aims at classifying news articles as fake or genuine using the title and content data of the article. The dataset contains 20800 news samples distributed between fake and real.

# Model
* Binary classification model
* Framework: Tensorflow version 2.7.0
* Architecture: LSTM RNN


* Dataset used - https://www.kaggle.com/c/fake-news/data


### Train accuracy: 99.29%
![Graph](https://user-images.githubusercontent.com/76942680/147737045-a8d61bb5-7061-4a51-aa0d-f1468ce294b1.png)


### Validation accuracy: 94.09%
![Graph2](https://user-images.githubusercontent.com/76942680/147737049-c2783cd6-a93c-4d16-a5c4-c622d66e6959.png)


# How to train:
Use the code in "model_file.ipynb" file and load it into google colab. Then run the model by adjusting the number of epochs to train for required accuracy.

# How to use:
Follow the code in 'predictor.py' file to load the model and use it for predictions.
