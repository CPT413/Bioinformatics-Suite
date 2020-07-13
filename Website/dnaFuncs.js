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
  let reverse = [];
  for(let i = sequence.length-1; i >=0; i--) {
    if(sequence[i] === 'a') {
      reverse.push('t')
    }
    else if (sequence[i] === 'c') {
      reverse.push('g')
    }
    else if (sequence[i] === 'g') {
      reverse.push('c')
    }
    else{
      reverse.push('a')
    }
  }
  return (reverse.toString().replace(/,/g,''))

}
console.log(reverseComp('atcgatatcgcgatatcg'))
const transcription = sequence => {
  /*
  This funcion allows for the transcription of dna to rna for the input
  sequence. Returns a string that is the rna transcript.
  */

}

const translation = sequence => {
  /*
  This function will allow for the DNA sequence to be translated into the
  corresponding protein sequence. It finds the first start codon (ATG) in the
  sequence and all of the stop codons (TAA, TAG, TGA). The protein will be
  translated using the start and first stop codon. The translated protein
  is in the 1-letter code.
  */

}
