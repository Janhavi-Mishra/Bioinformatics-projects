genome = input('Enter DNA sequence here: \n').upper()
genome_list = []
genome_list[:0] = genome

for i in range(len(genome_list)):
    nucleic_acid = genome_list[i]
    if nucleic_acid == 'T':
        genome_list[i] = 'U'

print("".join(genome_list))
