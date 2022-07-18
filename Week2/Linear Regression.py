import pandas as pd
import random as r
import matplotlib.pyplot as plt

# read the dataset
dataset = pd.read_csv('/PranavSoftwares/PyCharm Code/UTD AI Camp/Week2/data.train')

# define the values and set length of set
x = dataset.iloc[:, 0]
y = dataset.iloc[:, 1]
n = len(x)
der_ab = []
learning_rate = 10 ** -6

# assign a random value to [a, b]
der_ab = [r.randint(0, 10), r.randint(0, 10)]


# update a and b values with derivatives
def derivative_ab():
    a = 0
    b = 0
    for i in range(n):
        a += 2 * x[i] * ((der_ab[0] * x[i] + der_ab[1]) - y[i])
        b += 2 * (der_ab[0] * x[i] + der_ab[1] - y[i])
    der_ab[0] = der_ab[0] - (learning_rate * (a / n))
    der_ab[1] = der_ab[1] - (learning_rate * (b / n))


# make a main function to check loss and update accordingly
def main():
    curr_loss = 0
    z = 0
    while z < 1000:
        prev_loss = curr_loss
        curr_loss = 0
        for i in range(n):
            curr_loss += ((der_ab[0] * x[i] + der_ab[1]) - y[i]) ** 2
        curr_loss /= n
        if curr_loss > prev_loss != 0:
            break
        else:
            print(f'Run: {z}, Loss: {curr_loss}')
            derivative_ab()
        z += 1
    print(f'Final: f(x) = {der_ab[0]}x + {der_ab[1]}')
    y_pred = der_ab[0] * x + der_ab[1]

    plt.scatter(x, y)
    plt.plot([min(x), max(x)], [min(y_pred), max(y_pred)], color='orange')
    plt.show()


# call the main function
main()
