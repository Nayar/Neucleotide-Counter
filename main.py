sequences_array = [] # Initialising 1D array to store sequences

sequence_file = open('sequence.dat', 'r') # Reading sequence.dat and put into variable

for sequence in sequence_file:
  sequences_array.append(sequence) # Put each line in the array
  
for l in sequences_array:
  print l