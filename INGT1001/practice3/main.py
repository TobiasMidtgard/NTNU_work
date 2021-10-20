import pandas as pd
import functions
import calendar


df = pd.read_csv("meteringvalues-mp-xxxxx-consumption-202011.csv",
                 sep=";", index_col=False)
total_days = functions.get_total_days(df)
mean_df = functions.get_average_consumption(df)
max_index = functions.get_largest_usage(df)
time = list(df.iloc[max_index, 0:2])

print(f"Number of days in the month: {total_days} days")
print(f"Average usage per hour: {round(mean_df, 3)} kWh")
print(f"The time with the highest usage: From {time[0]} to {time[1]}")

print(calendar.month_name[3])
