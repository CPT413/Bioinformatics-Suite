const proteinSeqCheck = sequence => {
  /*
  This function will check to make sure that only applicable characters are
  in the sequence. Will also convert the string to upper-case, which is
  standard for working with amino acids.
  */
  //lists to comapre the residues to when checking
  const  singleLetterList = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'L',
         'N', 'D', 'Q', 'K', 'E', 'M', 'H', 'F', 'R', 'Y', 'W'];
  const threeLetterList = ['Cys', 'Asp', 'Ser', 'Gln', 'Lys', 'Trp', 'Asn',
        'Pro', 'Thr', 'Phe', 'Ala', 'Gly', 'Ile', 'Leu', 'His', 'Arg', 'Met',
        'Val', 'Glu', 'Tyr'];
//------------------------determine style of input-----------------------------
  let style = 0;

  //if the sequnce splits at '-' marks and matches a residue in the three
  //letter list, the sequence is in three letter abbreviation
  if(threeLetterList.indexOf(sequence.split('-')[0]) != -1) {
    style = 3; //set style value to 3, means three letter
  }
  else {
    style = 1; //otherwise the style value is set to 1, means one letter
  }
//--------------------single letter abbreviation check-------------------------
  //checks to see the style, if 1 then check one letter
  if(style === 1) {
    //loopes over whole sequence and checks each residue
    for (var residue = 0; residue < sequence.length; residue++) {
      //if the residue is not in the list above
      if(singleLetterList.indexOf(sequence[residue]) === -1) {
        //throws error and terminates code
        throw new Error('A residue in your sequence is incorrect.');
      }
    }
    return [sequence, style]; //if no errors occur, returns the sequence and style
  }
//---------------------three letter abbrevation check--------------------------
  //checks to see the style, if 3 then three letter
  else if(style === 3) {
    //loops over all residues in sequence
    for (var residue = 0; residue < sequence.split('-').length; residue++) {
      //if the residue is not in the list above
      if(threeLetterList.indexOf(sequence.split('-')[residue]) === -1) {
        //throws error and terminates code
        throw new Error('A residue in your sequence is incorrect.');
      }
    }
    return [sequence, style]; //if no errors occur, returns the sequence and style
  }
}
console.log(proteinSeqCheck('Gly-His-Asn'));
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
  //dictionary of the pKas for each amino acid. Each key corresponds to a list
  //with the pKa value [carboxyl, amino, side-chain]
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
  let pKaList = []; //empty array to push all pKa values to in sequence
  let neutralpH = 0; //create variable to save the pH at which charge = 0

  //loop over all residues and add applicable pKas
  for (var residue = 0; residue < sequence.length; residue++) {
//-----------------------first residue-----------------------------------------
    if(residue === 0) {
      pKaList.push(pKaDict[sequence[residue]][1]); //push pKa pf N-terminus
      //if residue has side-chain with pka, push value
      if(pKaDict[sequence[residue]][2] != undefined) {
        pKaList.push(pKaDict[sequence[residue]][2]);
      }
    }
//-----------------------last residue------------------------------------------
    else if (residue === sequence.length-1) {
      pKaList.push(pKaDict[sequence[residue]][0]); //push pKa pf C-terminus
      //if residue has side-chain with pka, push value
      if(pKaDict[sequence[residue]][2] != undefined) {
        pKaList.push(pKaDict[sequence[residue]][2]);
      }
    }
//-------------------------all other residues----------------------------------
    else {
      //if residue has side-chain with pka, push value
      if(pKaDict[sequence[residue]][2] != undefined) {
        pKaList.push(pKaDict[sequence[residue]][2]);
      }
    }
  }
  //loop to find the pH at which the sequence has no net charge
  for (let pH = 1; pH <= 12; pH++) {
    //if the sequence is neutral at given pH
    if (netCharge(sequence, pH) === 0) {
      //push that pH to pKa list
      pKaList.push(pH)
      neutralpH = pH //save the value of the pH to the variable neutralpH
    }
  }

  pKaList = pKaList.sort((a,b) => a-b)//sort pka list
  //finds average of pKas on either side of neutral pH, this is the agreed on
  //easy way to determine isoelectic point
  let isoPoint = (pKaList[pKaList.indexOf(neutralpH) - 1] +
                 pKaList[pKaList.indexOf(neutralpH) + 1])/2;
  return (isoPoint);
}


const netCharge = (sequence, pH) => {
  /*
  This function will be used to determine the net charge of a protein at a
  specified pH value.
  */
  //dictionary of the pKas for each amino acid. Each key corresponds to a list
  //with the pKa value [carboxyl, amino, side-chain]
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
    let charge = 0; //create variable to keep track of charge
    //loop over every residue in the sequence
    for (var residue = 0; residue < sequence.length; residue++) {
//------------------------first residue----------------------------------------
      if(residue === 0) {
        //checks to see if the pH is less than the pKa associated with the
        //N-terminus
        if(pH <= pKaDict[sequence[residue]][1]) {
          //if it is, add +1 to the charge
          charge++;
          //logic for side chain pKa
          //check to see if the residue does have a sidechain with pKa
          if(pKaDict[sequence[residue]][2] != undefined) {
            //if the residue is a C or Y
            if(sequence[residue] === 'C' || sequence[residue] === 'Y') {
              //if pH greater than the pKa of residue, subtract 1
              if(pH >= pKaDict[sequence[residue]][2]) {
                charge--;
              }
            }
            //if the residue is a D or E
            else if (sequence[residue] === 'D' || sequence[residue] === 'E') {
              //if pH greater than pKa, subtract 1
              if(pH >= pKaDict[sequence[residue]][2]) {
                charge--;
              }
            }
            //if residue is a K, R, or H
            else if (sequence[residue] === 'K' || sequence[residue] === 'R' ||
                     sequence[residue] === 'H') {
              //if pH less than pKa, add 1
              if(pH <= pKaDict[sequence[residue]][2]) {
                charge++;
              }
            }
          }
        }
        //if the pH > pKa
        else {
          //run through side chain logic, see above
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
            else if (sequence[residue] === 'K' || sequence[residue] === 'R' ||
                     sequence[residue] === 'H') {
              if(pH <= pKaDict[sequence[residue]][2]) {
                charge++;
              }
            }
          }
        }
      }
//---------------------------last residue--------------------------------------
      else if (residue === sequence.length-1) {
        //checks to see if pH is greater than pKa associated with the C-
        //terminus
        if(pH >= pKaDict[sequence[residue]][0]) {
          //subtract 1 if it is
          charge--;
          //run through sidechain logic, see above
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
            else if (sequence[residue] === 'K' || sequence[residue] === 'R' ||
                     sequence[residue] === 'H') {
              if(pH <= pKaDict[sequence[residue]][2]) {
                charge++;
              }
            }
          }
        }
        //if pH < pKa
        else{
          //run through sidechain logic, see above
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
            else if (sequence[residue] === 'K' || sequence[residue] === 'R' ||
                     sequence[residue] === 'H') {
              if(pH <= pKaDict[sequence[residue]][2]) {
                charge++;
              }
            }
          }
        }
      }
//-----------------------------all other residues------------------------------
      else {
        //run through sidechain logic, see above
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
          else if (sequence[residue] === 'K' || sequence[residue] === 'R' ||
                   sequence[residue] === 'H') {
            if(pH <= pKaDict[sequence[residue]][2]) {
              charge++;
            }
          }
        }
      }
    }
    return (charge); //return value of charge
}
