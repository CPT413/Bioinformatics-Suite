const readFASTA = text => {
  /*
  Function that allows for the reading of a FASTA formatted sequence entry.
  The function takes the text as input and returns a
  dictionary containing the header and sequence for each entry.
  */
  let sequences = {};

  for (let line = 0; line < text.split('\n').length; line += 2) {
    sequences[text.split('\n')[line].slice(1)] = text.split('\n')[line + 1];
  }
  console.log(sequences)
}

readFASTA('>seq1\natcgcgatatagcgcta\n>seq2\natcgatctattacgt');
