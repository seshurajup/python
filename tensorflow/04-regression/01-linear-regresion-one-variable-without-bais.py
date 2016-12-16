import tensorflow as tf 
import numpy as np 
import matplotlib.pyplot as plot

training_sample_count = 100

# total epoch
total_epoch = 100
# learning rate for gradient descent
learning_rate = 0.01


training_X =  range(1,training_sample_count)
training_Y =  [ ((value*5) + np.random.random()*value) for value in training_X]

plot.scatter(training_X,training_Y)
plot.show()

# placeholders for tensorflow
X = tf.placeholder("float")
Y = tf.placeholder("float")

# variables
W = tf.Variable(np.random.randn(),name="weight")

# model
pred = tf.mul(X,W)

# cost = loss function
cost = tf.reduce_sum(tf.pow(pred-Y, 2))/(2*training_sample_count)


# Gradient descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

init_variables = tf.initialize_all_variables()

cost_Y = np.ndarray((total_epoch,),float)
weight_X = np.ndarray((total_epoch,),float)

# Launch the graph
with tf.Session() as sess:
    sess.run(init_variables)

    # Fit all training data
    for epoch in range(total_epoch):
        for (x, y) in zip(training_X, training_Y):
            sess.run(optimizer, feed_dict={X: x, Y: y})
        training_cost = sess.run(cost, feed_dict={X: training_X, Y:training_Y})
        print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(training_cost), "W=", sess.run(W))
        cost_Y[epoch] = training_cost
        weight_X[epoch] = sess.run(W)

    training_cost = sess.run(cost, feed_dict={X: training_X, Y: training_Y})
    print("Training cost=", training_cost, "W=", sess.run(W), '\n')
    predicted_weights = sess.run(W)

    plot.scatter(training_X,training_Y)
    plot.plot(training_X, [ value_X * sess.run(W) for value_X in training_X ], label='Fitted line')
    plot.show()

    plot.plot(weight_X, cost_Y)
    plot.show()
    

