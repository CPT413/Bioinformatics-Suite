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
    #dictionary of the pKas for each amino acid. Each key corresponds to a list
    #with the pKa value [carboxyl, amino, side-chain]
    pKaDict = {
    'G': [2.34,9.60, None],
    'A': [2.34, 9.69, None],
    'V': [2.32,9.62, None],
    'L': [2.36, 9.60, None],
    'I': [2.36, 9.60, None],
    'S': [2.21, 9.15, None],
    'T': [2.63, 10.43, None],
    'M': [2.28, 9.21, None],
    'F': [1.83, 9.13, None],
    'W': [2.83, 9.39, None],
    'N': [2.02, 8.80, None],
    'Q': [2.17, 9.13, None],
    'P': [1.99, 10.60, None],
    'C': [1.71, 10.78, 8.33],
    'H': [1.82, 9.17, 6.00],
    'D': [2.09, 9.82, 3.86],
    'E': [2.19, 9.67, 4.25],
    'Y': [2.20, 9.11, 10.07],
    'K': [2.18, 8.95, 10.79],
    'R': [2.17, 9.04, 12.48]
    }

    pKaList = [] #list to append all pKa values to in sequence
    index = 0 #index variable to keep track of location in list

    #loop over all residues and add applicable pKas
    for residue in sequence:
#---------------------------first residue--------------------------------------
        if index == 0:
            pKaList.append(pKaDict[residue][1]) #append pKa of N-terminus
            if pKaDict[residue][2] != None:
                #if the residue has a pKa for side chain, append value
                pKaList.append(pKaDict[residue][2])
#--------------------------last residue----------------------------------------
        elif index == (len(sequence) - 1):
            pKaList.append(pKaDict[residue][0]) #append pKa of C-terminus
            if pKaDict[residue][2] != None:
                #if the residue has a pKa for side chain, append value
                pKaList.append(pKaDict[residue][2])
#--------------------------all other residues----------------------------------
        else:
            #if the residue has a pKa for side chain, append value
            if pKaDict[residue][2] != None:
                pKaList.append(pKaDict[residue][2])
#------------------------------------------------------------------------------
        index += 1 #increment index to keep track of spot

    #loop to find the pH at which the sequence has no net charge
    for pH in range(1,13):
        #if the sequence is neutral at a given pH
        if netCharge(sequence, pH) == 0:
            #append that value to the pKa list
            pKaList.append(pH)
            neutralpH = pH #make the pH variable available to the rest of code

    pKaList = sorted(pKaList) #sort list in ascending order

    #finds average of pKas on either side of neutral pH, this is the agreed on
    #easy way to determine isoelectic point
    isoPoint = (pKaList[pKaList.index(neutralpH) - 1] + pKaList[pKaList.index(neutralpH) + 1]) / 2


    return(isoPoint)


def netCharge(sequence, pH):
    """
    This function will be used to determine the net charge of a protein at a
    specified pH value.
    """
    #dictionary of the pKas for each amino acid. Each key corresponds to a list
    #with the pKa value [carboxyl, amino, side-chain]
    pKaDict = {
    'G': [2.34,9.60, None],
    'A': [2.34, 9.69, None],
    'V': [2.32,9.62, None],
    'L': [2.36, 9.60, None],
    'I': [2.36, 9.60, None],
    'S': [2.21, 9.15, None],
    'T': [2.63, 10.43, None],
    'M': [2.28, 9.21, None],
    'F': [1.83, 9.13, None],
    'W': [2.83, 9.39, None],
    'N': [2.02, 8.80, None],
    'Q': [2.17, 9.13, None],
    'P': [1.99, 10.60, None],
    'C': [1.71, 10.78, 8.33],
    'H': [1.82, 9.17, 6.00],
    'D': [2.09, 9.82, 3.86],
    'E': [2.19, 9.67, 4.25],
    'Y': [2.20, 9.11, 10.07],
    'K': [2.18, 8.95, 10.79],
    'R': [2.17, 9.04, 12.48]
    }

    index = 0 #create variable to keep track of location in sequence
    charge = 0 #create vaiable to keep track of charge
    for residue in sequence: #loop over all residues of the protein
#---------------------------first amino acid-----------------------------------
        if index == 0:
        #checks to see if the pH is less than the pKa associated with the
        #N-terminus
            if pH <= pKaDict[residue][1]:
                #if it is, add 1 to the charge
                charge += 1
                #logic for side chain pKa
                #check to see if the residue does have a sidechain with pKa
                if pKaDict[residue][2] != None:
                    #if the residue is a C or Y
                    if (residue == 'C') or (residue == 'Y'):
                        #if pH greater than the pKa of residue, subtract 1
                        if pH >= pKaDict[residue][2]:
                            charge += -1
                    #if the residue is a D or E
                    elif (residue == 'D') or (residue == 'E'):
                        #if pH greater than pKa, subtract 1
                        if pH >= pKaDict[residue][2]:
                            charge += -1
                    #if residue is a K, R, or H
                    elif (residue == 'K') or (residue == 'R') or (residue == 'H'):
                        #if pH less than pKa, add 1
                        if pH <= pKaDict[residue][2]:
                            charge += 1
            #if the pH > pKa
            else:
                #run through side chain logic, see above
                if pKaDict[residue][2] != None:
                    if (residue == 'C') or (residue == 'Y'):
                        if pH >= pKaDict[residue][2]:
                            charge += -1
                    elif (residue == 'D') or (residue == 'E'):
                        if pH >= pKaDict[residue][2]:
                            charge += -1
                    elif (residue == 'K') or (residue == 'R') or (residue == 'H'):
                        if pH <= pKaDict[residue][2]:
                            charge += 1
#----------------------------last amino acid-----------------------------------
        elif index == (len(sequence) - 1):
            #checks to see if pH is greater than pKa associated with the C-
            #terminus
            if pH >= pKaDict[residue][0]:
                #subtract 1 if it is
                charge += -1
                #run through sidechain logic, see above
                if pKaDict[residue][2] != None:
                    if (residue == 'C') or (residue == 'Y'):
                        if pH >= pKaDict[residue][2]:
                            charge += -1
                    elif (residue == 'D') or (residue == 'E'):
                        if pH >= pKaDict[residue][2]:
                            charge += -1
                    elif (residue == 'K') or (residue == 'R') or (residue == 'H'):
                        if pH <= pKaDict[residue][2]:
                            charge += 1
            #if pH < pKa
            else:
                #run through sidechain logic, see above
                if pKaDict[residue][2] != None:
                    if (residue == 'C') or (residue == 'Y'):
                        if pH >= pKaDict[residue][2]:
                            charge += -1
                    elif (residue == 'D') or (residue == 'E'):
                        if pH >= pKaDict[residue][2]:
                            charge += -1
                    elif (residue == 'K') or (residue == 'R') or (residue == 'H'):
                        if pH <= pKaDict[residue][2]:
                            charge += 1
#------------------------------all other amino acids---------------------------
        else:
            #run through sidechain logic, see above
            if pKaDict[residue][2] != None:
                if (residue == 'C') or (residue == 'Y'):
                    if pH >= pKaDict[residue][2]:
                        charge += -1
                elif (residue == 'D') or (residue == 'E'):
                    if pH >= pKaDict[residue][2]:
                        charge += -1
                elif (residue == 'K') or (residue == 'R') or (residue == 'H'):
                    if pH <= pKaDict[residue][2]:
                        charge += 1

        index += 1 #increment the index for the next residue

    return(charge)
isoelectricPoint('WGRGFDQNTYVILPNRYT')
