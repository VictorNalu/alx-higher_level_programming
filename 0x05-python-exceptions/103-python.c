#include <Python.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        PyErr_Print();
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        PyErr_Print();
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    Py_ssize_t i;

    printf("[.] Bytes object info\n");
    printf("size: %ld\n", size);
    printf("trying string: %s\n", PyBytes_AsString(p));

    printf("first 10 bytes: ");
    for (i = 0; i < size && i < 10; i++) {
        printf("%02hhx", *((char *)PyBytes_AsString(p) + i));
        if (i < 9 && i + 1 < size) {
            printf(" ");
        }
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        PyErr_Print();
        return;
    }

    printf("[.] Float object info\n");

    printf("value: %f\n", ((PyFloatObject *)p)->ob_fval);
}
