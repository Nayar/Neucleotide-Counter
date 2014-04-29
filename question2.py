sequences_array = [] # Initialising 1D array to store sequences

sequence_file = open('sequence.dat', 'r') # Reading sequence.dat and put into variable

for sequence in sequence_file:
  sequences_array.append(sequence) # Put each line in the array
  
total = []

for s in sequences_array: 
  count_a = 0
  count_c = 0
  count_t = 0
  count_g = 0
  for neucleotide in s:
    if (neucleotide ==  'A'):
      #print("A")
      count_a = count_a + 1
    elif (neucleotide == 'C'):
      #print("C")
      count_c = count_c + 1

    elif (neucleotide == 'T'):
      #print("T")
      count_t = count_t + 1
    elif (neucleotide == 'G'):
      #print("G")
      count_g = count_g + 1
  total_length = count_a + count_c + count_t + count_g
  total.append([count_a,count_c,count_t,count_g,total_length])
  
for sequence in sequences_array:
  print (sequence)
  
for t in total:
  print ("%d %d %d %d %d" % (t[0],t[1],t[2],t[3],t[4]))
      
