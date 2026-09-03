#T101 RAJDEEP M PARAB
# AIM: Implement Feed Forward Backpropagation Neural Network
# to predict employee promotion based on performance score and years of experience.
import numpy as np
# Input data:
# [Performance Score, Years of Experience]
X = np.array(([80, 5],
              [60, 2],
              [90, 7]), dtype=float)
# Target output:
# 1 = Promotion
# 0 = No Promotion
y = np.array(([1],
              [0],
              [1]), dtype=float)
# Normalize input data
X = X / np.amax(X, axis=0)
# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
# Derivative of sigmoid
def derivatives_sigmoid(x):
    return x * (1 - x)
# Parameters
epoch = 7000
lr = 0.1
inputlayer_neurons = 2
hiddenlayer_neurons = 3
output_neurons = 1

# Random weights and biases
wh = np.random.uniform(
    size=(inputlayer_neurons, hiddenlayer_neurons)
)
bh = np.random.uniform(
    size=(1, hiddenlayer_neurons)
)
wout = np.random.uniform(
    size=(hiddenlayer_neurons, output_neurons)
)
bout = np.random.uniform(
    size=(1, output_neurons)
)

# Backpropagation training
for i in range(epoch):
    # Hidden layer
    hinp1 = np.dot(X, wh)
    hinp = hinp1 + bh
    hlayer_act = sigmoid(hinp)
    # Output layer
    outinp1 = np.dot(hlayer_act, wout)
    outinp = outinp1 + bout
    output = sigmoid(outinp)
    # Error
    EO = y - output
    # Output layer gradient
    outgrad = derivatives_sigmoid(output)
    d_output = EO * outgrad
    # Hidden layer error
    EH = d_output.dot(wout.T)
    # Hidden layer gradient
    hiddengrad = derivatives_sigmoid(hlayer_act)
    d_hiddenlayer = EH * hiddengrad
    # Update weights and biases
    wout += hlayer_act.T.dot(d_output) * lr
    bout += np.sum(d_output, axis=0, keepdims=True) * lr
    wh += X.T.dot(d_hiddenlayer) * lr
    bh += np.sum(d_hiddenlayer, axis=0, keepdims=True) * lr

print("Employee Input Data:")
print(X)
print("\nActual Output:")
print(y)
print("\nPredicted Output:")
print(output)

# Easy-to-understand result
print("\nPrediction Result:")
for i in range(len(output)):
    probability = output[i][0] * 100

    if probability >= 50:
        print("Employee", i + 1,
              "-> Promotion Likely",
              "(", round(probability, 2), "% )")
    else:
        print("Employee", i + 1,
              "-> Promotion Not Likely",
              "(", round(probability, 2), "% )")
