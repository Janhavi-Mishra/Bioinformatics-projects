genome = input('Enter DNA sequence here: \n').upper()
genome_list = []
genome_list[:0] = genome
genome_list.reverse()

for i in range(len(genome_list)):
    nucleic_acid = genome_list[i]
    if nucleic_acid == 'A':
        genome_list[i] = 'T'
    elif nucleic_acid == 'T':
        genome_list[i] = 'A'
    elif nucleic_acid == 'C':
        genome_list[i] = 'G'
    elif nucleic_acid == 'G':
        genome_list[i] = 'C'

print("".join(genome_list))
