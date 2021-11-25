import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))
def predictionFunction(age):
    z = 0.042 * age - 1.53
    y = sigmoid(z)
    return y # when y returned is greater than 0.5, neuron is on, else it's off

def gradient_descent(x, y):
    m_curr = b_curr = 0
    iterations = 10000
    n = len(x)
    learning_rate = 0.07  # CAN CHANGE
    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = 1/n * sum([val**2 for val in (y - y_predicted)])
        md = -(2 / n) * sum(x * (y - y_predicted))
        bd = -(2 / n) * sum((y - y_predicted))
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd

        print("m {}, b {}, cost {} iteration {}".format(m_curr, b_curr, cost, i))

def get_score(model, x_train, x_test, y_train, y_test ):
    model.fit(x_train, y_train)
    return model.score(x_test, y_test)
