
## Dogs vs. Cats
In this competition, you'll write an algorithm to classify whether images contain either a dog or a cat.  This is easy for humans, dogs, and cats. Your computer will find it a bit more difficult. Find the data [here](https://www.kaggle.com/c/dogs-vs-cats/data). 


![](https://storage.googleapis.com/kaggle-competitions/kaggle/3362/media/woof_meow.jpg)

Deep Blue beat Kasparov at chess in 1997.  
Watson beat the brightest trivia minds at Jeopardy in 2011.  
Can you tell Fido from Mittens in 2013?  


This repository provides you source code to train a deep convolutional neuron network on Kaggle's Dog & Cat dataset. We're not focus on choosing the best CNN network, we just design a network which gives acceptable accuracy. The trained model is then used by a Flask application which allows user to upload an image of dog or cat and have the model predict the image's label.
