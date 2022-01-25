#This project was done in Google Colab, if you want to check it there you can click here: https://colab.research.google.com/drive/1DjeRB8I8_B7-OnEIpl2gcGg0KsJvnKqp?usp=sharing

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_old = pd.read_csv("/content/BTC_USDT.csv", skiprows = [0])

temporal = []
for i in range(len(df_old)):
	if ("2021" in df_old["date"][i]) or ("2022" in df_old["date"][i]):
		temporal.append([df_old["date"][i], df_old["close"][i]])
df_new = pd.DataFrame(temporal, columns = ["Date", "Price"])
del temporal, df_old

df_new.to_csv("BTC_USDT_1.csv", index = False)

temp_year = []
temp_month = []
temp_day = []
temp_hour = []
temp_minute = []
for i in range(len(df_new)):
	temp_year.append(df_new["Date"][i][0:4])
	temp_month.append(df_new["Date"][i][5:7])
	temp_day.append(df_new["Date"][i][8:10])
	temp_hour.append(df_new["Date"][i][11:13])
	temp_minute.append(df_new["Date"][i][14:16])
df_new["Year"] = temp_year
del temp_year
df_new["Month"] = temp_month
del temp_month
df_new["Day"] = temp_day
del temp_day
df_new["Hour"] = temp_hour
del temp_hour
df_new["Minute"] = temp_minute
del temp_minute

temp = len(df_new)
temp_index = []
for i in range(len(df_new)):
	temp_index.append(temp-i)
df_new["Index"] = temp_index
del temp, temp_index
temp = len(df_new)
df_new["Index"] = [temp-i for i in range(len(df_new))]

def row_index(df, str_key, value_expected):
  for i in range(len(df)):
    if df[str_key][i] == value_expected: 
      return i
  raise KeyError("row not in the dataframe")
	
df_new.loc[row_index(df_new, "Index", 1)]

df_new.to_csv("BTC_USDT_2.csv", index = False)

df_new.drop(columns="Date", inplace = True)

temp = []
original_value = df_new["Price"][0]
for i in range(len(df_new)):
  temp.append(df_new["Price"][i]/original_value)

temp = list(map(lambda x: x*1000, temp))

df_new["Price"] = temp
del temp, original_value

df_new.to_csv("/content/BTC_USDT_3.csv", index = False)

crypto_series = pd.Series(list(df_new["Price"]), index = list(df_new["Index"]))

crypto_series.plot()
