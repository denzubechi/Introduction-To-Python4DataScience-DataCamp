# np_baseball is available
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]
# Import numpy
import numpy as np

# Print mean height (first column)
avg = np.mean(baseball[:,0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(baseball[:, 0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(baseball[:, 0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(baseball[:,0], baseball[:,1])
print("Correlation: " + str(corr))
