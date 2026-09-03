# T101 RAJDEEP M PARAB
import numpy as np
class NeuralNetwork():
    def __init__(self):
        # Seeding for random number generation
        np.random.seed()
        # Converting weights to a 3 by 1 matrix
        self.synaptic_weights = 2 * np.random.random((3, 1)) - 1
    # Sigmoid activation function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    # Derivative of sigmoid function
    def sigmoid_derivative(self, x):
        return x * (1 - x)
    # Training the neural network
    def train(self, training_inputs, training_outputs,
              training_iterations):
        for iteration in range(training_iterations):
            # Getting output from the neuron
            output = self.think(training_inputs)
            # Calculating error
            error = training_outputs - output
            # Adjusting weights
            adjustments = np.dot(
                training_inputs.T,
                error * self.sigmoid_derivative(output)
            )
            self.synaptic_weights += adjustments
    # Prediction function
    def think(self, inputs):
        # Converting inputs to float
        inputs = inputs.astype(float)
        # Passing inputs through sigmoid function
        output = self.sigmoid(
            np.dot(inputs, self.synaptic_weights)
        )
        return output
if __name__ == "__main__":
    # Initializing the neural network
    neural_network = NeuralNetwork()
    print("Beginning randomly generated weights: ")
    print(neural_network.synaptic_weights)
    # Training data
    # 3 inputs:
    # Aptitude, Interview, Communication
    training_inputs = np.array([
        [0, 0, 0],
        [1, 1, 1],
        [1, 0, 1],
        [0, 1, 0]
    ])
    # Training outputs
    # 0 = Not Selected
    # 1 = Selected
    training_outputs = np.array([
        [0, 1, 1, 0]
    ]).T

    # Training the model
    neural_network.train(
        training_inputs,
        training_outputs,
        15000
    )
    print("Ending weights after training: ")
    print(neural_network.synaptic_weights)
    # Taking new applicant inputs
    user_input_one = str(input("Aptitude Score (0 or 1): "))
    user_input_two = str(input("Interview Score (0 or 1): "))
    user_input_three = str(input("Communication Score (0 or 1): "))
    print(
        "Considering new applicant: ",
        user_input_one,
        user_input_two,
        user_input_three
    )
    print("New output data: ")
    print(
        neural_network.think(
            np.array([
                user_input_one,
                user_input_two,
                user_input_three
            ])
        )
    )
