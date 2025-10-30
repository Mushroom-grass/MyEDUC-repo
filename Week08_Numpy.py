import numpy as np


# Create a list of temperatures for 7 days:
temps_celsius = [15, 18, 21, 20, 16, 19, 22]

# Import the NumPy library and convert this list into a NumPy array. 
temps_array = np.array(temps_celsius)

# Find the highest and lowest temperatures of the week using NumPy functions.
highest_temp = np.max(temps_array)
lowest_temp = np.min(temps_array)

# Calculate the mean temperature.
mean_temp = np.mean(temps_array)

# Convert the temperatures from Celsius to Fahrenheit.
temps_fahrenheit = (temps_array * 9 / 5) + 32

# Count how many days had temperatures above 20°C.
days_above_20 = np.sum(temps_array > 20)

# Print
print(f"Temperatures (°C): {temps_array}")
print(f"Highest Temperature: {highest_temp}°C, Lowest Temperature: {lowest_temp}°C, Average Temperature: {mean_temp}°C, Number of days above 20°C: {days_above_20}")
print(f"Temperature (°F): {temps_fahrenheit}")