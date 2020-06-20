def gcContent(sequence):
    """
    Thie function will calculate the gc content for a given sequence.
    Returns the percent gc.
    """
    #adds the number of c and g and divides by the total length of the sequence
    #then multiplies by 100 to get a percent
    gc = ((sequence.count('c') + sequence.count('g'))/(float(len(sequence))))*100
    return(gc)
