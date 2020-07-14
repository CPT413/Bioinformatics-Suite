const dnaSeqCheck = sequence => {
  /*
  This function will be used to proofread the entered sequence before
  processing. The function qill return a sequence in lower-case format
  */

}

const gcContent = sequence => {
  /*
  This function will calculate the gc content for a given sequence. Returns
  the percent gc.
  */
  //find number of 'g': (sequence.match(/g/g) || []).length;
  //find number of 'c':  (sequence.match(/c/g) || []).length;
  //add those togther and divide by length of sequence and multiply by 100
  return ((((sequence.match(/g/g) || []).length +
  (sequence.match(/c/g) || []).length) / sequence.length) * 100);
}

const reverseComp = sequence => {
  /*
  This function will allow for the reverse complement of an input sequence to
  be determined. Returns a string that is reverse complement.
  */
  let reverse = []; //creates empty array to add reverse base to

  //loops over bases in sequence in reverse order
  for(let i = sequence.length-1; i >=0; i--) {
    //if the base is an 'a', push 't' to array
    if(sequence[i] === 'a') {
      reverse.push('t');
    }
    //if the base is an 'c', push 'g' to array
    else if (sequence[i] === 'c') {
      reverse.push('g');
    }
    //if the base is an 'g', push 'c' to array
    else if (sequence[i] === 'g') {
      reverse.push('c');
    }
    //if the base is an 't', push 'a' to array
    else{
      reverse.push('a');
    }
  }
  //convert array to string, replace commas with '', and return value
  return (reverse.toString().replace(/,/g,''));

}

const transcription = sequence => {
  /*
  This funcion allows for the transcription of dna to rna for the input
  sequence. Returns a string that is the rna transcript.
  */
  let trasncript = []; //create empty array to add bases to

  //loop over every base in sequence
  for(let i = 0; i < sequence.length; i++) {
    //if the base is a 't', push 'u' to array
    if(sequence[i] === 't') {
      trasncript.push('u');
    }
    //all other bases are pushed to array
    else {
      trasncript.push(sequence[i]);
    }
  }
  //convert array to string, replace commas with '', return value
  return (trasncript.toString().replace(/,/g, ''))
}

const translation = sequence => {
  /*
  This function will allow for the DNA sequence to be translated into the
  corresponding protein sequence. It finds the first start codon (ATG) in the
  sequence and all of the stop codons (TAA, TAG, TGA). The protein will be
  translated using the start and first stop codon. The translated protein
  is in the 1-letter code.
  */
  const codons = {
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
  };
  let startSite = sequence.indexOf('atg');
  let protein = [];
  console.log(startSite);
  
}
translation('aatg');
