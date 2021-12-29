# A Text Classification model built using Tensorflow
This is a NLP text classification based project. Here an LSTM model has been built using Tensorflow which aims at classifying news articles as fake or genuine using the title and content data of the article. The dataset contains 20800 news samples distributed between fake and real.

# Model
* Singleclass classification model
* Framework: Tensorflow version 2.7.0
* Architecture: LSTM RNN


* Dataset used - https://www.kaggle.com/c/fake-news/data

### Accuracy: 99.55%
![Graph](https://user-images.githubusercontent.com/76942680/147688840-53a2f9ff-ac69-4c34-bc1c-58b816ad7989.png)

### Validation accuracy: 94.64%


# How to train:
Use the code in "model_file.ipynb" file and load it into google colab. Then run the model by adjusting the number of epochs to train for required accuracy.

# How to use:
Follow the code in 'predictor.py' file to load the model and use it for predictions.
