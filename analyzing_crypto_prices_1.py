#This project was done in Google Colab, if you want to check it there you can click here: https://colab.research.google.com/drive/1DjeRB8I8_B7-OnEIpl2gcGg0KsJvnKqp?usp=sharing

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_old = pd.read_csv("file_name_path", skiprows = [0])

#df_old must contain a column name "date" and another one name "close"
temporal = []
for i in range(len(df_old)):
  if ("2021" in df_old["date"][i]) or ("2022" in df_old["date"][i]):
    temporal.append([df_old["date"][i], df_old["close"][i]])

df_new = pd.DataFrame(temporal, columns = ["Date", "Price"])
del temporal, df_old

print(len(df_new))

df_new.to_csv("file_name_path_1", index = False)

print(df_new.head(5))

#In order for this to work the "date" column should have the following format: YYYY-MM-DD HH:MM:SS
df_new["Year"] = [int(df_new["Date"][i][0:4]) for i in range(len(df_new))]
df_new["Month"] = [int(df_new["Date"][i][5:7]) for i in range(len(df_new))]
df_new["Day"] = [int(df_new["Date"][i][8:10]) for i in range(len(df_new))]
df_new["Hour"] = [int(df_new["Date"][i][11:13]) for i in range(len(df_new))]
df_new["Minute"] = [int(df_new["Date"][i][14:16]) for i in range(len(df_new))]

print(df_new.head(10))

temp = len(df_new)
df_new["Index"] = [temp-i for i in range(len(df_new))]
del temp

print(df_new.head(10))

df_new.to_csv("file_name_path_2", index = False)

df_new.drop(columns="Date", inplace = True)

original_value = df_new["Price"][0]
df_new["Price"] = [df_new["Price"][i]*1000/original_value for i in range(len(df_new))]
del original_value

print(df_new.head(10))

df_new.to_csv("file_name_path_3", index = False)

crypto_series = pd.Series(list(df_new["Price"]), index = list(df_new["Index"]))

print(df_new.head(5))

print(crypto_series.head(5))

crypto_series.plot()
