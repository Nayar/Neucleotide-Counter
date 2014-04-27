sequences_array = []

sequence_file = open('sequence.dat', 'r')

for sequence in sequence_file:
  sequences_array.append(sequence)
  
for l in sequences_array:
  print l