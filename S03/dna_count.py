sequence = input("Introduce the sequence: ")
print("Total length:", len(sequence))

bases_dict = {"A": 0, "C": 0, "G": 0, "T": 0}
for letter in sequence:
    if letter in bases_dict:
        bases_dict[letter] += 1

for letter, count in bases_dict.items():
    print("{}: {}".format(letter, count))