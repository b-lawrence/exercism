"""
DNA to RNA transcription
"""

NUCLEOTIDE_MAP = str.maketrans('GCTA', 'CGAU')


def to_rna(dna):
    """Transcribe to RNA"""
    return dna.translate(NUCLEOTIDE_MAP)
