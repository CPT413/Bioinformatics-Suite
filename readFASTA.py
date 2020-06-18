def readFASTA(filePath):
    """
    Function that allows for the reading of a FASTA formatted file.
    The function takes the filepath of the file as input and returns a
    dictionary containing the header and sequence for each entry.
    """
    sequenceDictionary = {} #creates a new dictionary to add header and seq data
    with open(filePath) as file: #opens the file at the given file path
        for line in file: #loops over every line in the file
            if line[0] == ">": #the lines containing the header info star with
                               #">"
                header = ''.join(line[1:].strip()) #takes everything after the
                                                   #">" and makes into a string
                                                   #the strip removes \n
                sequence = 'holder' #creates a holder variable for the sequence
            else: #if a line does not start with ">" then it is a seq
                sequence = ''.join(line[:].strip())

            sequenceDictionary[header] = sequence #first pass, the holder is
                                            #added, second time the seq is added

    return(sequenceDictionary)
