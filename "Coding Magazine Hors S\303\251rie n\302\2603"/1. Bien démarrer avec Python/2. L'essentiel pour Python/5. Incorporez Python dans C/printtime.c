#include <Python.h>

int main(int argc, char* argv[]) {
	Py_SetProgramName(argv[0]);
	Py_Initialize();
	PyRun_SimpleString("from time import time, ctime\n"
	"print 'today is ', ctime(time()); ");
	Py_Finalize();
	return 0;
}
