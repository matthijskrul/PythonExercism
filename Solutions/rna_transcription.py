def to_rna(dna_strand):
    conversions = {"G": "C", "C": "G", "T": "A", "A": "U"}
    result = dna_strand.maketrans(conversions)
    return dna_strand.translate(result)
