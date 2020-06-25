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
    sequence and all of the stop codons (TAA, TAG, TGA). For each combination
    of start and stop, the code will check if the length is divisible by 3. If
    it is then the translation will be done. If not that combination is ignored.
    The translated protein is in the 1-letter code.
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

    #find the start site
    startSite = sequence.find('atg') #this returns the index of the 'a'

    #taa stop codon processing
    taaStopSite = sequence[startSite:].find('taa') + 2
    #finds the first taa after the stop site. the find returns the index of the
    #'t' so add 2 to get the index of second 'a'

    if ((taaStopSite - startSite) + 1) % 3 == 0:
        #checks if the seq is a multiple of 3

        protein = [] #creates empty list to add amino acids to

        codonList = [sequence[i:i+3] for i in range(startSite, taaStopSite, 3)]
        #determines the codons in between the start and taa stop site. does
        #this through list comprehensions, loops over all indexes in the range
        #of the start and stop codons and reads them sets of three

        for codon in codonList: #loop over all codons in the codonList
            protein.append(codons[codon]) #appends the amino acid from the dict
        protein = ''.join(protein) #changes the list of amino acids to a string
        print(protein)
    #tag stop codon processing

    #tga stop codon processing

    #3 for each combination: if length is divisble by 3 (%3 == 0) then
    #  translate, if not then skip that combination
    #report what stop codon was used in output

translation('ataatgcgtagcgagtaagatcgatc')
