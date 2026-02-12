import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



'''
This function generates one random walk and returns a list of the walk positions at each time step


steps (int) -> The number of time steps to take

stepSize (double, default = 1.0) -> Magnitude of the step distance

probability (double in [0, 1], default = 0.5) -> Probability the entity moves down (backward). A larger probability value indicates a higher probability of moving down (backward). A smaller probability value indicates a higher probability of moving up (forward).


DO NOT CHANGE ANYTHIN IN THIS METHOD
'''#only play with the 0.5 and stepsize if wanted
def randomWalk(steps, stepSize = 1.0, probability = 0.5):
#starting at position
    walk = [0.0]

    for st in range(1, steps):
#generate a #between 0-1
        rand = np.random.uniform(0, 1)

        if(rand < probability):

            walk.append(walk[st - 1] - stepSize)

        else:

            walk.append(walk[st - 1] + stepSize)

    return walk









'''
Main method where the simulation is performed
'''
if __name__ == "__main__":

    # Number of random walk realizations to perform - you can change this value
    numWalks = 30 #change this, this will produce 5 individual random walks, you need a min 10

    # Number of steps to take during a random walk - you can change this value
    numSteps = 15 #you will also change this, since the min requested is 10 steps



    # Python dictionary to hold each random walk realization - DO NOT ALTER THIS LINE
    walkDict = {}

    # Python list to hold each random walk's column header - DO NOT ALTER THIS LINE
    headers = []



    # This loop simulates the desired number of random walks - DO NOT CHANGE THIS LOOP
    for i in range(numWalks):

        # Creates then appends the appropriate random walk header to the headers list
        headers.append(f"Walk {i + 1}")

        # Call to randomWalk produces one random walk realization
        walk = randomWalk(numSteps)

        # Appends the random walk along with its associated header to the dictionary
        walkDict[headers[i]] = walk



    # Converts the disctionary to a Pandas DataFrame
    df = pd.DataFrame(walkDict)

    # Writes the DataFrame to a .csv file (called Random_Walks.csv)
    # Includes an initial row index column
    # Provides the header row for the column headers
    df.to_csv(path_or_buf = "Random_Walks1.csv", # we will have to change the name of the file to produce another csv file, otherwise we overwrite them. 
              sep = ',',
              index = True,
              header = headers)
    
    # This is how to grab the last row of a DataFrame
    # The .iloc[] function grabs a row of a DataFrame using the row index (or row header name)
    df.iloc[df.shape[0] - 1] #rows & columns, if i want the last row, i grab the # of rows in my data and subtract 1

    # 1 csv file will be .5
    # 1 csv > .5
    # 1 csv < .5