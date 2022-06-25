package fr.codeworks.bbl

import org.assertj.core.api.Assertions
import org.junit.jupiter.api.AfterEach
import org.junit.jupiter.api.Test

import org.junit.jupiter.api.BeforeEach
import org.junit.jupiter.api.DisplayName
import java.io.*

internal class CodeTestRunnerKtTest {
    lateinit var out: PrintStream
    val filePath = "src/test/resources/init"

    @BeforeEach
    fun setup(){
        out = System.out
        System.setOut(PrintStream(FileOutputStream("$filePath/lead.txt")))

    }
    @AfterEach
    fun destroy(){
        System.setOut(out)
    }

    @Test
    @DisplayName("Should make sure the last outputs matches gold")
    fun shouldRunMain() {
        val lead = BufferedReader(FileReader("$filePath/lead.txt"))
        val gold = BufferedReader(FileReader("$filePath/gold.txt"))

        main()

        var line: String?
        while (gold.readLine().also { line = it } != null) {
            Assertions.assertThat(line).isEqualTo(lead.readLine())
        }

    }
}
