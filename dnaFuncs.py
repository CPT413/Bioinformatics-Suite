def dnaSeqCheck(sequence):
    """
    This function will be used to proofread the entered sequence before
    processing. The function qill return a sequence in lower-case format
    """

    baseList = ['a', 't', 'g', 'c'] #list to compare each character to

    sequence = sequence.lower() #converts sequence to lower-case

    #loops over each character in the sequence
    for base in sequence:
        #if the base is not in the list
        if base not in baseList:
            #throws error and terminates code
            raise ValueError('A base in your sequence is not a nucleotide')

    return(sequence) #returns sequence is all characters are a, t, g, or c


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


def transcription(sequence):
    """
    This funcion allows for the transcription of dna to rna for the input
    sequence. Returns a string that is the rna transcript.
    """
    transcript = [] #creates empty list to append the bases to

    for base in sequence: #iterates over sequnece
        if base == 't': #replaces t with u in transcript
            transcript.append('u')
        else: #all other bases remain the same
            transcript.append(base)

    transcript = ''.join(transcript)

    return(transcript)


def translation(sequence):
    """
    This function will allow for the DNA sequence to be translated into the
    corresponding protein sequence. It finds the first start codon (ATG) in the
    sequence and all of the stop codons (TAA, TAG, TGA). The protein will be
    translated using the start and first stop codon, the code will check if the
    length is divisible by 3. If it is then the translation will be done.
    If not that combination is ignored. The translated protein is in the
    1-letter code.
    """
    #sets dictionary for the codons and the corresponding amino acid. stop
    #codons are correspond to ''
    codons = {
    'ttt': 'F',
    'ttc': 'F',
    'tta': 'L',
    'ttg': 'L',
    'ctt': 'L',
    'ctc': 'L',
    'cta': 'L',
    'ctg': 'L',
    'att': 'I',
    'atc': 'I',
    'ata': 'I',
    'atg': 'M',
    'gtt': 'V',
    'gtc': 'V',
    'gta': 'V',
    'gtg': 'V',
    'tct': 'S',
    'tcc': 'S',
    'tca': 'S',
    'tcg': 'S',
    'cct': 'P',
    'ccc': 'P',
    'cca': 'P',
    'ccg': 'P',
    'act': 'T',
    'acc': 'T',
    'aca': 'T',
    'acg': 'T',
    'gct': 'A',
    'gcc': 'A',
    'gca': 'A',
    'gcg': 'A',
    'tat': 'Y',
    'tac': 'Y',
    'taa': '',
    'tag': '',
    'cat': 'H',
    'cac': 'H',
    'caa': 'Q',
    'cag': 'Q',
    'aat': 'N',
    'aac': 'N',
    'aaa': 'K',
    'aag': 'K',
    'gat': 'D',
    'gac': 'D',
    'gaa': 'E',
    'gag': 'E',
    'tgt': 'C',
    'tgc': 'C',
    'tga': '',
    'tgg': 'W',
    'cgt': 'R',
    'cgc': 'R',
    'cga': 'R',
    'cgg': 'R',
    'agt': 'S',
    'agc': 'S',
    'aga': 'R',
    'agg': 'R',
    'ggt': 'G',
    'ggc': 'G',
    'gga': 'G',
    'ggg': 'G'
    }

    #finds start site in dna sequence
    startSite = sequence.find('atg') #this returns the index of the 'a'

    protein = [] #creates empyt list for protein sequence

    #creates a new list that reads the entered sequence in sets of 3 starting
    #with the start codon. This produces a list of codons in frame with the
    #start codon.
    codonList = [sequence[i:i+3] for i in range(startSite, len(sequence), 3)]

    #loops over that codon list and performs an action for each codon
    for codon in codonList:
        #checks to see if the current codon is one of the 3 stop codons
        #if it is then it breaks out of the loop and translation stops
        if (codon == 'taa') or (codon == 'tag') or (codon == 'tga'):
            break
        #if the codon is not a stop, then the corresponding amino acid is added
        #to the protein list
        else:
            protein.append(codons[codon])
    protein = ''.join(protein) #final protein list is changed into a string
    return(protein)
