const readFASTA = text => {
  /*
  Function that allows for the reading of a FASTA formatted sequence entry.
  The function takes the text as input and returns a
  dictionary containing the header and sequence for each entry.
  */
  let text1 = text.split('\n')
  return text1
}

console.log(readFASTA('>seq1\natcgcgatatagcgcta'));
