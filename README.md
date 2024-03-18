
Obtaining the Protein Sequence of Human Insulin
1. Access NCBI

Visit NCBI and select "Protein" from the dropdown menu next to the search bar. Search for "human insulin" and choose the relevant search result.

2. Copy the Insulin Sequence

Copy the insulin sequence from the search record, starting with the word "ORIGIN" and ending with "//".

3. Create preproinsulin-seq.txt

In AWS Cloud9 IDE, create a new file named "preproinsulin-seq.txt" and paste the insulin sequence into it.

4. Bonus: Cleaning the Sequence Programmatically

Programmatically clean the "preproinsulin-seq.txt" file to remove "ORIGIN", numbers, slashes, spaces, and line breaks. Ensure the file contains exactly 110 characters.

5. Retrieve Insulin Amino Acids

Manually or programmatically delete "ORIGIN", numbers, "//", spaces, and line breaks from "preproinsulin-seq.txt" to obtain the amino acids composing insulin.

6. Create Cleaned Files

Create new files in Cloud9 IDE for each segment of insulin amino acids:

preproinsulin-seq-clean.txt: Full sequence of preproinsulin after cleaning.
lsinsulin-seq-clean.txt: Amino acids 1–24 (24 characters).
binsulin-seq-clean.txt: Amino acids 25–54 (30 characters).
cinsulin-seq-clean.txt: Amino acids 55–89 (35 characters).
ainsulin-seq-clean.txt: Amino acids 90–110 (21 characters).
Ensure each file contains the specified number of characters and only lowercase letters representing amino acids.
