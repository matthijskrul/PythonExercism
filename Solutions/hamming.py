def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        exception = ValueError("The lengths of both strands must be equal!")
        raise exception
    hammondcounter = 0
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            hammondcounter += 1
    return hammondcounter
