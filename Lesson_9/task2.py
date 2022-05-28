"""Write a program that checks that DNA sequence is valid (consists only of the characters
'A', 'C', 'G', ’T’). If not - raise an Exception."""

DNA = 'ACGT'
nucleotides = ['A', 'C', 'G', 'T']
for base in DNA:
    if base not in nucleotides:
        raise Exception
    else:
        print('DNA is valid')
