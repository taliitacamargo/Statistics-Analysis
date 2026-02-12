import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
# Read csv files starting from the first row, not the unnamed one
        df1 = pd.read_csv("Random_Walks1.csv",index_col=0)
        df2 = pd.read_csv("Random_Walks2.csv",index_col=0)
        df3 = pd.read_csv("Random_Walks3.csv",index_col=0)
# Creates the figure and axis
fig ,ax = plt.subplots()

# Set variable names for the last rows for each file
df1row = df1.iloc[-1]
df2row = df2.iloc[-1]
df3row = df3.iloc[-1]

# Title on the graph
ax.set_title("Box-and-Whisker Plot", fontweight = 'bold')

# Label on x axis
ax.set_xlabel("Probability Parameter", size = 10, fontweight = 'bold')

# Setting a range to the Y-axis so we can read the data better
ax.set_yticks(range(-15,15,1))

# Setting Y-Axis Label
ax.set_ylabel("Final Position", size = 10, fontweight = 'bold')

# Creating a horizontal grid (y-axis)
ax.grid(True, axis = 'y')

# Gets each file to plot them, and add labels to each tick
ax.boxplot(
[df1row, df2row, df3row],
whis = [0,100],
tick_labels = ["Probability 0.5", "Probability 0.7", "Probability 0.3"])

# print(df1row)
# print(df2row)
# print(df3row)

# Prints the mean, variance, and standard deviation for each final rows.
print((f"0.5 Probability Mean: {df1row.mean()}, " f"Variance: {df1row.var()}, " f"Standard Deviation: {df1row.std()}"))
print((f"0.7 Probability Mean: {df2row.mean()}, " f"Variance: {df2row.var()}, " f"Standard Deviation: {df2row.std()}"))
print((f"0.3 Probability Mean: {df3row.mean()}, " f"Variance: {df3row.var()}, " f"Standard Deviation: {df3row.std()}"))

# Displays plotted Graph
plt.show()


