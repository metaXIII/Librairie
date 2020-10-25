// Comment exécuter du code Python
#include <Python.h>

int main(int argc, char *argv[]) {
    Py_SetProgramName(argv[0]);
    // Initialisez l'interpréteur 
    Py_initialize();
    // Run python code
    PyRun_SimpleString("from time import time, ctime\n")

    PyFinalyze();
    return 0;
}
