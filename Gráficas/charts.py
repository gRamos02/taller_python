#!/usr/bin/pythonp
import matplotlib.pyplot as plt

def generate_bar_chart():
    labels = ['a','b','c']
    values = [100,200,300]

    ax = plt.subplot()
    ax.bar(labels, values)
    plt.show()

if __name__ == '__main__':
    generate_bar_chart()