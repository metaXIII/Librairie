#include <Python.h>
#include <stdio.h>

int main(int argc, char* argv[]) {
	FILE *fp;
	Py_Initialize();
	fp = fopen("my_script.py", "r");
	PyRun_SimpleFile(fp, "my_script.py");
	Py_Finalize();
	fclose(fp);
}
