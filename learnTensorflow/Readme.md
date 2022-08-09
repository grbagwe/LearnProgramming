# learn tensorflow
 This repository is based on the tensorflow tutorial from the youtube source in freecodecamp.org
 Check colab.research.google.com to run the codes in an online python notebook which is free by Google.

## Tensorflow
 Tensorflow is a framerwork to build neural network (NN) models that used to solve the tasks. These tasks can be broadly classified as:
 * Image classification
 * Data clustering
 * Regression
 * Reinforcement learning
 * Natural language processing

 The aim is to covert the task into supervised and unsupervised learning. In supervised learning the we have information is of the input (independent features: X) as well as the dependent output labels (dependent features: Y). The aim is to find a function (f), such that Y = f(X). The function is parameterized by $\theta and we find the optimal parameters.

# Tensorflow graphs and sessions
 The graph states the computation without executing the computation. If we define the sum in the graph it knows that it is the sum for two variables without calculating the graph.
 Session is where we actually compute the graphs we defined. It starts with the lowest independent variables and calculates the dependent variables thereafter.
 
