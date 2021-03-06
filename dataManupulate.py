"""
author : james.bondu
description : data from mnist
"""
import pandas as pd
import os
import gzip
import wget
import matplotlib.pyplot as plt
from random import randint
import cPickle

def load_data():
    if not os.path.exists(os.path.join(os.curdir, "data")):
        os.mkdir(os.path.join(os.curdir,"data"))
        wget.download("http://deeplearning.net/data/mnist/mnist.pkl.gz", out="data")

    data_file = gzip.open(os.path.join (os.curdir ,"data", "mnist.pkl.gz"), "rb" )
    train_data, validation_data ,test_data = cPickle.load(data_file)
    data_file.close()
    return train_data

def show_demo(train_data):
    #devide the train data to input data and lables
    train_x,train_y = train_data
    #randomly showing a number
    print "hello from the demo"
    plt.imshow(train_x[randint(0,train_y.size-1)].reshape(28 , 28))
    plt.show()


if __name__ == "__main__":
    train_data = load_data()
    show_demo(train_data)
