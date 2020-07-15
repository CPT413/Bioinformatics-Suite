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
  let mass = 0;

  for (var residue = 0; residue < sequence.length; residue++) {
    mass += residueMasses[sequence[residue]];
  }
  console.log(mass);
}

molecularWeight('GGG')
const oneToThree = sequence => {
  /*
  Converts a sequence of amino acids in single-letter abbreviation to the
  corresponding three-letter abbreviation
  */

}

const threeToOne = sequence => {
  /*
  Converts a sequence of amino acids in three-letter abbreviation to the
  corresponding single-letter abbreviation
  */

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

}
