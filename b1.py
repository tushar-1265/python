import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from scipy import stats

def read_data(file_path):
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format")

def scatter_plot(data,x_label,y_label):
    plt.scatter(data[x_label],data[y_label])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(f'Scatter plot of {x_label} vs {y_label}')
    plt.show()

def calculate_mean(data):
    return np.mean(data)

def calculate_median(data):
    return np.median(data)

def calculate_std(data):
    return np.std(data)

def calculate_var(data):
    return np.var(data)


def slope_intercept(data,x_label,y_label):
    slope,intercept,r_value,p_value,std_error=stats.linregress(data[x_label],data[y_label])
    return slope,intercept

def draw_regression_line(data,x_label,y_label):
    slope,intercept=slope_intercept(data,x_label,y_label)
    plt.scatter(data[x_label],data[y_label])
    plt.plot(data[x_label],slope*data[x_label]+intercept,color='red',label='Regression line')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.show()


file_path='tips.csv'
x_label='total_bill'
y_label='tip'

data=read_data(file_path)

scatter_plot(data,x_label,y_label)

