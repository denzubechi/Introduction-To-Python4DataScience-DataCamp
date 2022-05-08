# Import numpy
from audioop import avg
import numpy as np

# Create a numpy array from height_in: np_height_in
height_in = [23, 45, 23, 67, 89, 44, 69]
weight_lb = [53, 85, 83, 57, 89, 44, 69]
np_height_in = np.array(height_in)
numpy_a = np.array(weight_lb)
add = np_height_in + numpy_a
help(avg)
# Print np_height_m
print(add)





#BMI
# height_in and weight_lb are available as regular lists
# Import numpy
import numpy as np

# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg/np_height_m ** 2
