def molecularWeight(sequence):
    """
    This function will take a sequence of amino acids (single letter
    abbrevation and upper case) and will return the molecular weight of the
    protein (g/mol).
    """
    #dictionary or residues and their corresponding molecular weight in g/mol
    residueMasses = {
    'G': 57.02,
    'A': 71.04,
    'S': 87.03,
    'P': 97.05,
    'V': 99.07,
    'T': 101.05,
    'C': 103.01,
    'I': 113.08,
    'L': 113.08,
    'N': 114.04,
    'D': 115.03,
    'Q': 128.06,
    'K': 128.09,
    'E': 129.04,
    'M': 131.04,
    'H': 137.06,
    'F': 147.07,
    'R': 156.10,
    'Y': 163.06,
    'W': 186.08
    }

    mass = 0 #initiate mass to 0

    #loops over all residues in the sequence
    for residue in sequence:
        mass += residueMasses[residue] #adds the mass of the residue

    return(mass) #returns final mass

def oneToThree(sequence):
    """
    Converts a sequence of amino acids in single-letter abbreviation to the
    corresponding three-letter abbreviation
    """

    #dictionary of the one-letter abbreviations and the corresponding
    #three-letter abbreviations
    oneLetter = {
    'A': 'Ala',
    'R': 'Arg',
    'N': 'Asn',
    'D': 'Asp',
    'C': 'Cys',
    'E': 'Glu',
    'Q': 'Gln',
    'G': 'Gly',
    'H': 'His',
    'I': 'Ile',
    'L': 'Leu',
    'K': 'Lys',
    'M': 'Met',
    'F': 'Phe',
    'P': 'Pro',
    'S': 'Ser',
    'T': 'Thr',
    'W': 'Trp',
    'Y': 'Tyr',
    'V': 'Val'
    }

    threeLetter = [] #creates a list to append the three-letter abbreviations
    index = 0 #create an index variable to keep track where in the sequence

    #loop over all of the sequence
    for residue in sequence:
        #if the loop is at the end of the sequence, append the abbreviation
        #withouth '-'
        if index == (len(sequence) - 1):
            threeLetter.append(oneLetter[residue])
        #otherwise append the abbreviation plus '-'
        else:
            threeLetter.append(oneLetter[residue] + '-')

        index += 1 #iterate the index variable to keep track of position

    threeLetter = ''.join(threeLetter)#join the list into a string

    return(threeLetter)

def threeToOne(sequence):
    """
    Converts a sequence of amino acids in three-letter abbreviation to the
    corresponding single-letter abbreviation
    """
    #dictionary of the three-letter abbreviations and the corresponding
    #one-letter abbreviations
    threeLetter = {
    'Cys': 'C',
    'Asp': 'D',
    'Ser': 'S',
    'Gln': 'Q',
    'Lys': 'K',
    'Trp': 'W',
    'Asn': 'N',
    'Pro': 'P',
    'Thr': 'T',
    'Phe': 'F',
    'Ala': 'A',
    'Gly': 'G',
    'Ile': 'I',
    'Leu': 'L',
    'His': 'H',
    'Arg': 'R',
    'Met': 'M',
    'Val': 'V',
    'Glu': 'E',
    'Tyr': 'Y'}

    oneLetter = [] #created new list to append the one-letter abbreviation

    #loop over every residue in sequence, splits string at the '-'
    for residue in sequence.split('-'):
    #appends the corresponding one-letter abbreviation
        oneLetter.append(threeLetter[residue])

    oneLetter = ''.join(oneLetter) #converts list to a string

    return(oneLetter)


def isoelectricPoint(sequence):
    """
    This function will determine the isoelectric point of the given amino acids
    sequence. The calculation will be made assuming body temperature (37C) and
    standard conditions.
    """
