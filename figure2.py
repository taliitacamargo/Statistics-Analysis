import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
  

    df1 = pd.read_csv("Random_Walks2.csv",index_col=0)


   
    fig, ax = plt.subplots(layout="constrained") 
            
    fig.suptitle("Random Walks 0.7", fontweight = 'bold')

    ax.set_xlabel("Time", size = 10, fontweight = 'bold')
    ax.set_xlim(0,14)
    ax.set_xticks(range(0,15,1))
    
    ax.set_ylabel("Position", size = 10, fontweight = 'bold')
    ax.set_yticks(range(-8,13,1))


    ax.grid(True, axis = 'y')
    ax.grid(True, axis = 'x')
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
    
    plt.legend()
    plt.show()