### This Python script reads a .txt file, count things in the file, and output a new txt file

# Read the txt file
fhand = open('romeo-full.txt')

# Define variables to count things
count = 0 # count lines
# more variables to count other things

# Loop through each line to count things
for line in fhand:
    count = count + 1
    # more code to count things

# Create an output.txt file
fout = open('output.txt', 'w')
fout.write(count)

# Close the file
fout.close()
