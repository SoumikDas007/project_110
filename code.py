import pandas as pd
import csv
import statistics
import plotly.figure_factory as ff
import random
import plotly.graph_objects as go

df = pd.read_csv("data2.csv")
data = df["temp"].tolist()

def random_mean(counter):
    dataSet = []
    for i in range(0,counter):
        random_add = random.randint(0,len(data)-1)
        value = data[random_add]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean

def show_graph(mean_list):
    df  = mean_list
    mean = statistics.mean(df)
    line = ff.create_distplot([df],["temperature"],show_hist=False)
    line.add_trace(go.Scatter(x=[mean,mean],y = [0,1], mode = "lines", name = "mean"))
    line.show()

def main():
    mean_list= []
    for i in range(0,1000):
        dataSet_mean = random_mean(100)
        mean_list.append(dataSet_mean)
    show_graph(mean_list)
    mean = statistics.mean(mean_list)
    print("mean of sampling distribution",mean)    

main() 

full_mean = statistics.mean(data)
print("THE MEAN OF FULL DATA IS:",full_mean)

def standard_dev():
    mean_list = []
    for i in range(0,1000):
        dataSet_mean = random_mean(100)
        mean_list.append(dataSet_mean)
    std_deviation = statistics.stdev(mean_list)
    print("THE STD DEVIATION OF SAMPLING DATA IS",std_deviation)
    
standard_dev()