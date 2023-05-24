#include "InitializeGraph.h"

main(int argc, char **argv) {
    Py_Initialize();
    FILE* fp;
    fp = fopen("WikiWebScraping.py", "r");
    PyRun_AnyFile(fp, " ");
    Py_Finalize();
    return 0;
}