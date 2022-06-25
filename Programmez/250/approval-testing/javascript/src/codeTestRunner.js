const TECHNICAL_WORKSHOP = require('./technicalWorkshop.js')

function runCodeTest(){
  TECHNICAL_WORKSHOP.addCat('Java')
  TECHNICAL_WORKSHOP.addCandidate('Toto', 'Titi', 'titi@mail.fr')

  const SCORE = TECHNICAL_WORKSHOP.run('Java')
  console.log(`The candidate as a total of ${SCORE} points.`)
}

module.exports = runCodeTest
