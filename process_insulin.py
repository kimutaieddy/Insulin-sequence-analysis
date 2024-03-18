# Read the content of the cleaned file
with open('preproinsulin-seq-clean.txt', 'r') as file:
    content = file.read()

# Extract segments of the amino acid sequence
ls_insulin = content[:24]
b_insulin = content[24:54]
c_insulin = content[54:89]
a_insulin = content[89:]

# Print the lengths of extracted segments for debugging
print("Length of ls_insulin:", len(ls_insulin))
print("Length of b_insulin:", len(b_insulin))
print("Length of c_insulin:", len(c_insulin))
print("Length of a_insulin:", len(a_insulin))

# Write the segments to separate files
with open('lsinsulin-seq-clean.txt', 'w') as file:
    file.write(ls_insulin)

with open('binsulin-seq-clean.txt', 'w') as file:
    file.write(b_insulin)

with open('cinsulin-seq-clean.txt', 'w') as file:
    file.write(c_insulin)

with open('ainsulin-seq-clean.txt', 'w') as file:
    file.write(a_insulin)
