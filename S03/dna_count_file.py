bases_dict = {"A": 0, "C": 0, "G": 0, "T": 0}
total_bases = 0

with open('dna.txt', 'r') as f:
    for sequence in f:
        total_bases += len(sequence)
        for letter in sequence:
            if letter in bases_dict:
                bases_dict[letter] += 1

print("Total number of bases:", total_bases)
for letter, count in bases_dict.items():
    print("{}: {}".format(letter, count))
