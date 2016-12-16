# import tensorflow package
import tensorflow as tf 

constant = tf.constant("Hellow World");
with tf.Session() as session :
    print(session.run(constant))

firstVariable = tf.constant(3)
secondVariable = tf.constant(5)
with tf.Session() as session :
    print(session.run(firstVariable * secondVariable))
