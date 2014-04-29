mass_a = 135
mass_c = 111
mass_t = 151
mass_g = 126

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
  
def calc_total_sequence_mass(no_of_a, no_of_c, no_of_t, no_of_g):
  return no_of_a * mass_a + no_of_c * mass_c + no_of_t * mass_t + no_of_g * mass_g

mininum_mass = 99999999 # should be infinity
mininum_mass_sequence_number = 0
maximum_mass = 0
maximum_mass_sequence_number = 0
total_mass = 0

for i in range(len(sequences_array)):
  print(sequences_array[i])
  mass = calc_total_sequence_mass(total[i][0],total[i][1],total[i][2],total[i][3])
  print("Total Mass: %d" % mass)
  
  total_mass += mass
  if(mass < mininum_mass):
    mininum_mass = mass
    mininum_mass_sequence_number = i
  if(mass > maximum_mass):
    maximum_mass = mass
    maximum_mass_sequence_number = i
  print("---------------------")
  
print("Lowest mass is %d" % mininum_mass)
print("Highest mass is %d " % maximum_mass)
print("Average mass is %d " % (total_mass / len(sequences_array)))
print("Lowest mass sequence is: %s with mass %d" % (sequences_array[mininum_mass_sequence_number], mininum_mass))
print("Highest mass sequence is %s with mass %d" % (sequences_array[maximum_mass_sequence_number], maximum_mass))


