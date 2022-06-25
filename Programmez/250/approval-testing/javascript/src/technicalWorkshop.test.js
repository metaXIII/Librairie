const TECHNICAL_WORKSHOP = require("./technicalWorkshop")

describe("Code Test", () => {
    describe("Technical Workshop", () => {
        it("add Cat", () => {
            TECHNICAL_WORKSHOP.addCat("SQL")
            expect(TECHNICAL_WORKSHOP.cat.length).toBe(0)
        })
    })

    describe("add candidate", () => {
        it("should return undefined, given an empty string", () => {
            expect(TECHNICAL_WORKSHOP.loadQuestionsByCategory("")).toBe(undefined)
        })
        it("should return a collection of 1 item given SQL", () => {
            const question = TECHNICAL_WORKSHOP.loadQuestionsByCategory("SQL");
            expect(question.length).toBe(1)
        })
        it("should return a collection of 8 item given Java", () => {
            const question = TECHNICAL_WORKSHOP.loadQuestionsByCategory("Java");
            expect(question.length).toBe(8)
        })
    })
})
