import math
import csv

width1= 10
lengthwidth = 10
height = 10

# network charateristics
input_nodes = 20
hidden_nodes = 20
output_nodes = 20
learning_rate = 0.01

# auxiliar functions
def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def sigmoid_derivative(x):
  return sigmoid(x) * (1 - sigmoid(x))

# loading data
training_file = 'training_dataset.csv'
testing_file = 'testing_dataset.csv'

training_data = csv.reader(training_file)
testing_data = csv.reader(testing_file)

# normalize data
for i in range(len(training_data)):
  training_data[i][0] = training_data[i][0] / width
  training_data[i][1] = training_data[i][1] / length
  training_data[i][2] = training_data[i][2] / width
  training_data[i][3] = training_data[i][3] / length

for i in range(len(testing_data)):
  testing_data[i][0] = testing_data[i][0] / width
  testing_data[i][1] = testing_data[i][1] / length
  testing_data[i][2] = testing_data[i][2] / width
  testing_data[i][3] = testing_data[i][3] / length

# initialize weights and biases
weights_in = [random.random()/4 for _ in range(input_nodes*hidden_nodes)]
weights_out = [random.random()/4 for _ in range(output_nodes*hidden_nodes)]
bias_hidden = [random.random()/4 for _ in range(hidden_nodes)]
bias_out = [random.random()/4 for _ in range(output_nodes)]

# train the network
for data in training_data:
  # evaluation/activation of hidden layer
  hidden_evaluation = []
  hidden_activation = []
  for node in range(hidden_nodes):
    sum = 0
    for input in range(input_nodes):
      sum += weights_in[node*hidden_nodes + input] * data[0]
      sum += weights_in[node*hidden_nodes + input + 1] * data[1]
      input += 1
    sum += bias_hidden[node]
    hidden_evaluation.append(sum)
    hidden_activation.append(sigmoid(sum))

  # evaluation/activation of outputs
  output_evaluation = []
  output_activation = []
  for node in range(output_nodes):
    sum = 0
    for output in range(output_nodes):
      for hidden_node in range(hidden_nodes):
        node_id = output * output_nodes + hidden_node
        sum += hidden_activation[node_id] * weights_out[node_id]
    sum += bias_out[node]
    output_evaluation.append(sum)
    output_activation.append(sigmoid(sum))

  # weight calculation from the output layer
  for node_out in range(output_nodes):
    for node_in in range(hidden_nodes):
      weight_id = node_out * hidden_nodes + node_in
      error_d = (data[3] - output_activation[node_out]) * sigmoid_derivative(hidden_activation[node_in])
      weights_out[weight_id] += learning_rate * error_d * hidden_activation[weight_id]
      node_in += 1
      weight_id += 1
      error_d = (data[4] - output_activation[node_out]) * sigmoid_derivative(hidden_activation[node_in])
      weights_out[weight_id] += learning_rate * error_d * hidden_activation[weight_id]

  # weight calculation from the hidden layer
  for node_out in range(hidden_nodes):
    for node_in in range(input_nodes):
      weight_id = node_out * input_nodes + node_in
      error_d = (data[3] - output_activation[node_out]) * sigmoid_derivative(output_activation[node_out])
      delta_weight = sigmoid_derivative(hidden_evaluation[node_in])

        
        w6 = w6 + learning_rate * in2 * d_sigmoid(hidden_neuron_sum_3) * w9 * 
        
        d_sigmoid(out_neuron_activation) * (out - out_neuron_activation);