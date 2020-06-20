def gcContent(sequence):
    """
    This function will calculate the gc content for a given sequence.
    Returns the percent gc.
    """
    #adds the number of c and g and divides by the total length of the sequence
    #then multiplies by 100 to get a percent
    gc = ((sequence.count('c') + sequence.count('g'))/(float(len(sequence))))*100
    return(gc)


def reverseComp(sequence):
    """
    This function will allow for the reverse complement of an input sequence to
    be determined. Returns a string that is reverse complement.
    """
    reverse = [] #creates empty list to append bases to

    for base in sequence[::-1]: #iterates over sequence backwards
        if base == 'a': #if base is a it appends t
            reverse.append('t')
        elif base == 't': #if base is t it appends a
            reverse.append('a')
        elif base == 'g': #if base is g it appends c
            reverse.append('c')
        elif base == 'c': #if base is c it appends g
            reverse.append('g')

    reverse = ''.join(reverse) #changes the list to a string

    return(reverse)
