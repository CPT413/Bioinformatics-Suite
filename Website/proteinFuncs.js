const proteinSeqCheck = sequence => {
  /*
  This function will check to make sure that only applicable characters are
  in the sequence. Will also convert the string to upper-case, which is
  standard for working with amino acids.
  */

}

const molecularWeight = sequence => {
  /*
  This function will take a sequence of amino acids (single letter
  abbrevation and upper case) and will return the molecular weight of the
  protein (g/mol).
  */
  //dictionary or residues and their corresponding molecular weight in g/mol
  const residueMasses = {
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

  let mass = 0; //creat variable to sum up all masses of the residues

  //loopo over every residue in the sequence
  for (var residue = 0; residue < sequence.length; residue++) {
    //for each residue, add the corresponding mass to the mass sum
    mass += residueMasses[sequence[residue]];
  }
  return (mass); //return value
}

const oneToThree = sequence => {
  /*
  Converts a sequence of amino acids in single-letter abbreviation to the
  corresponding three-letter abbreviation
  */
  //dictionary of the one-letter abbreviations and the corresponding
  //three-letter abbreviations
  const oneLetter = {
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

    let threeLetter = []; //create empty array to push three letter to

    //loop over entire sequence
    for (var residue = 0; residue < sequence.length; residue++) {
      //if the residue is last in the sequence, push three letter with out '-'
      if (residue === sequence.length - 1) {
        threeLetter.push(oneLetter[sequence[residue]]);
      }
      //otherwise, push three letter followed by '-'
      else {
        threeLetter.push(oneLetter[sequence[residue]] + '-');
      }
    }
    //convert array to sting, replace ',' with '', return string
    return (threeLetter.toString().replace(/,/g, ''));
}

const threeToOne = sequence => {
  /*
  Converts a sequence of amino acids in three-letter abbreviation to the
  corresponding single-letter abbreviation
  */
  //dictionary of the three-letter abbreviations and the corresponding
  //one-letter abbreviations
  const threeLetter = {
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

    let oneLetter = []; //create empyt array to push one letter to

    //loop over sequence split at the '-'
    for (var residue = 0; residue < sequence.split('-').length; residue++) {
      //push the correspondind one letter to the array
      oneLetter.push(threeLetter[sequence.split('-')[residue]]);
    }
    //convert array to string, replace ',' with '', return value
    return (oneLetter.toString().replace(/,/g, ''));
}

const isoelectricPoint = sequence => {
  /*
  This function will determine the isoelectric point of the given amino acids
  sequence. The calculation will be made assuming body temperature (37C) and
  standard conditions.
  */

}

const netCharge = (sequence, pH) => {
  /*
  This function will be used to determine the net charge of a protein at a
  specified pH value.
  */
  const pKaDict = {
    'G': [2.34,9.60, undefined],
    'A': [2.34, 9.69, undefined],
    'V': [2.32,9.62, undefined],
    'L': [2.36, 9.60, undefined],
    'I': [2.36, 9.60, undefined],
    'S': [2.21, 9.15, undefined],
    'T': [2.63, 10.43, undefined],
    'M': [2.28, 9.21, undefined],
    'F': [1.83, 9.13, undefined],
    'W': [2.83, 9.39, undefined],
    'N': [2.02, 8.80, undefined],
    'Q': [2.17, 9.13, undefined],
    'P': [1.99, 10.60, undefined],
    'C': [1.71, 10.78, 8.33],
    'H': [1.82, 9.17, 6.00],
    'D': [2.09, 9.82, 3.86],
    'E': [2.19, 9.67, 4.25],
    'Y': [2.20, 9.11, 10.07],
    'K': [2.18, 8.95, 10.79],
    'R': [2.17, 9.04, 12.48]
  };
    let charge = 0;
    for (var residue = 0; residue < sequence.length; residue++) {
//------------------------first residue----------------------------------------
      if(residue === 0) {
        if(pH <= pKaDict[sequence[residue]][1]) {
          charge++;
          if(pKaDict[sequence[residue]][2] != undefined) {
            if(sequence[residue] === 'C' || sequence[residue] === 'Y') {
              if(pH >= pKaDict[sequence[residue]][2]) {
                charge--;
              }
            }
            else if (sequence[residue] === 'D' || sequence[residue] === 'E') {
              if(pH >= pKaDict[sequence[residue]][2]) {
                charge--;
              }
            }
            else if (sequence[residue] === 'K' || sequence[residue] === 'R' || sequence[residue] === 'H') {
              if(pH <= pKaDict[sequence[residue]][2]) {
                charge++;
              }
            }
          }
        }
        else {
          if(pKaDict[sequence[residue]][2] != undefined) {
            if(sequence[residue] === 'C' || sequence[residue] === 'Y') {
              if(pH >= pKaDict[sequence[residue]][2]) {
                charge--;
              }
            }
            else if (sequence[residue] === 'D' || sequence[residue] === 'E') {
              if(pH >= pKaDict[sequence[residue]][2]) {
                charge--;
              }
            }
            else if (sequence[residue] === 'K' || sequence[residue] === 'R' || sequence[residue] === 'H') {
              if(pH <= pKaDict[sequence[residue]][2]) {
                charge++;
              }
            }
          }
        }
      }
//---------------------------last residue--------------------------------------
      else if (residue === sequence.length-1) {
        if(pH >= pKaDict[sequence[residue]][0]) {
          charge--;
          if(pKaDict[sequence[residue]][2] != undefined) {
            if(sequence[residue] === 'C' || sequence[residue] === 'Y') {
              if(pH >= pKaDict[sequence[residue]][2]) {
                charge--;
              }
            }
            else if (sequence[residue] === 'D' ||sequence[residue] === 'E') {
              if(pH >= pKaDict[sequence[residue]][2]) {
                charge--;
              }
            }
            else if (sequence[residue] === 'K' || sequence[residue] === 'R' || sequence[residue] === 'H') {
              if(pH <= pKaDict[sequence[residue]][2]) {
                charge++;
              }
            }
          }
        }
        else{
          if(pKaDict[sequence[residue]][2] != undefined) {
            if(sequence[residue] === 'C' || sequence[residue] === 'Y') {
              if(pH >= pKaDict[sequence[residue]][2]) {
                charge--;
              }
            }
            else if (sequence[residue] === 'D' || sequence[residue] === 'E') {
              if(pH >= pKaDict[sequence[residue]][2]) {
                charge--;
              }
            }
            else if (sequence[residue] === 'K' || sequence[residue] === 'R' || sequence[residue] === 'H') {
              if(pH <= pKaDict[sequence[residue]][2]) {
                charge++;
              }
            }
          }
        }
      }
//-----------------------------all other residues------------------------------
      else {
        if(pKaDict[sequence[residue]][2] != undefined) {
          if(sequence[residue] === 'C' || sequence[residue] === 'Y') {
            if(pH >= pKaDict[sequence[residue]][2]) {
              charge--;
            }
          }
          else if (sequence[residue] === 'D' || sequence[residue] === 'E') {
            if(pH >= pKaDict[sequence[residue]][2]) {
              charge--;
            }
          }
          else if (sequence[residue] === 'K' || sequence[residue] === 'R' || sequence[residue] === 'H') {
            if(pH <= pKaDict[sequence[residue]][2]) {
              charge++;
            }
          }
        }
      }
    }
    return (charge);
}
console.log(netCharge('NDDCYTILV',7))
