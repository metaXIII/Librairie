const promptSync =require( 'prompt-sync')
const prompt = promptSync({})

const Q = require( './questions.json')

let CAN = { firstName: '' }
const CAT = []

const TECHNICAL_WORKSHOP = {
  candidate : { ...CAN },
  cat: CAT,
  addCat: (label) => {
    console.log(`Adding ${label} in categories`)

    this?.cat?.push(label)
  },
  addCandidate: (firstName, lastName, email) => {
    console.log(`Adding ${firstName} as candidate`)
    this.candidate = {
      firstName,
      lastName,
      email
    }
  },
  getCandidate: () => this?.candidate,
  loadQuestion: () => {
    return [...Q]
  },
  loadQuestionsByCategory(category) {
    const CATEGORY = this?.loadQuestion().find(question => question.label === category)
    return CATEGORY?.questions
  }
}

module.exports = TECHNICAL_WORKSHOP
