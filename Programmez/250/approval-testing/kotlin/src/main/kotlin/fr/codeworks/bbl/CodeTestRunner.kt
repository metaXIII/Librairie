package fr.codeworks.bbl

import fr.codeworks.bbl.codeTest.TechnicalWorkshop

fun main() {
    val codeTest = TechnicalWorkshop()
    codeTest.addCat("SQL")
    codeTest.addCan("Toto", "Titi", "titi@mail.fr")
    val score = codeTest.runCodeTest("Java")
    println("The candidate as a total of $score points.")
}




