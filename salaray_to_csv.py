import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split 
df = pd.read_csv("data_reg_age_salary.csv")


x = df.values #returns a numpy array
min_max_scaler = preprocessing.MinMaxScaler()
pd.DataFrame(min_max_scaler.fit_transform(df.T), columns=df.columns, index=df.index)
df = pd.DataFrame(x_scaled)
df.to_csv("data_reg_age_salary.csv", index=False)
