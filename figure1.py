import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
  
# Reads file, making sure the first column is not the unnamed one
    df1 = pd.read_csv("Random_Walks1.csv", index_col=0)
# Creates Figure and axis, which contains a constrained layout
    fig, ax = plt.subplots(layout="constrained") 
# Creates the main title for the figure "Random Walks"       
    fig.suptitle("Random Walks 0.5", fontweight = 'bold')
# Creates label for the x-axis
    ax.set_xlabel("Time", size = 10, fontweight = 'bold')
# Limits the x-axis size so it's not unnecessarily taking up space
    ax.set_xlim(0,14)
# Creates ticks range so it shows the data better
    ax.set_xticks(range(0,15,1))
# Creates label for Y-axis
    ax.set_ylabel("Position", size = 10, fontweight = 'bold')
# Creates ticks range for the y-axis so we can have a better view of the data
    ax.set_yticks(range(-8,13,1))
# Creates X and Y grid
    ax.grid(True, axis = 'y')
    ax.grid(True, axis = 'x')
# Plots The lines for each walk
    ax.plot(
                    df1["Walk 1"],
                     label="Walk 1",
                     color = "yellow") 
     
    ax.plot(
                    df1["Walk 2"],
                     label="Walk 2 ",
                     color = "blue") 
     
    ax.plot(
                    df1["Walk 3"],
                     label="Walk 3",
                     color = "red") 
    ax.plot(
                    df1["Walk 4"],
                     label="Walk 4",
                     color = "violet")
    ax.plot(
                    df1["Walk 5"],
                     label="Walk 5",
                     color = "orange")  
# Creates the box that shows each walk's color and name
    plt.legend()
    plt.show()

