const readFASTA = text => {
  /*
  Function that allows for the reading of a FASTA formatted sequence entry.
  The function takes the text as input and returns a
  dictionary containing the header and sequence for each entry.
  */

  //creats empty object to add the header and sequence data to.
  let sequences = {};

  //loops over whole line of text, focuses on every other entry these hold
  //the header information
  for (let line = 0; line < text.split('\n').length; line += 2) {
    //crated object entry with the header as the key and the sequence as
    //the value
    sequences[text.split('\n')[line].slice(1)] = text.split('\n')[line + 1];
  }
  return sequences; //return the object
}
