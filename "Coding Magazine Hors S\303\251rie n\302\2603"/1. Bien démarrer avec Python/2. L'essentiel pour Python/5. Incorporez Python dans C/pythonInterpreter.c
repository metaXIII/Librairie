#include <Python.h>

int main(int argc, char* argv[]) {
	Py_Initialize();
	Py_Main(argc, argv);
	Py_Finalize();
}
