def distance(dna_strand1, dna_strand2):
    if len(dna_strand1) != len(dna_strand2):
        raise ValueError('DNA strands are not of equal length')
    return [nucleotide1 == nucleotide2 for (nucleotide1, nucleotide2) in zip(dna_strand1, dna_strand2)].count(False)
