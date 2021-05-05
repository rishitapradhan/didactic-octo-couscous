function calculateAnswer(message) {
  var result = []
  var algorithm =  ['S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R'] 
  var alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  var messageCaps = message.toUpperCase();
  messageCaps.split('').forEach(letter => {
    if(letter === ' ') {
       result.push(letter);
    } else if(alphabet.includes(letter)) {
      var index = alphabet.findIndex(alphaLetter => alphaLetter === letter)
      var alletter = algorithm[index];
      result.push(alletter)
    }
  });
  return result.join("")
}
var message =  "ABCDEFG"

var cypher = calculateAnswer(message);

console.log(output)
