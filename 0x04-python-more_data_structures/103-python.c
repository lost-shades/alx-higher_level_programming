#include <Python.h>

/**
 * print_python_list - Print information about a Python list
 * @p: A PyObject pointer to a Python list
 */

void print_python_list(PyObject *p)
{
Py_ssize_t i, size;
PyObject *item;

size = PyList_Size(p);
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
}
}

/**
 * print_python_bytes - Print information about a Python bytes object
 * @p: A PyObject pointer to a Python bytes object
 */

void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;

printf("[.] bytes object info\n");
if (PyBytes_Check(p))
{
size = PyBytes_Size(p);

printf("  size: %zd\n", size);
printf("  trying string: %s\n", PyBytes_AS_STRING(p));
printf("  first %zd bytes: ", (size < 10) ? size : 10);

for (i = 0; i < size && i < 10; i++)
{
printf(
"%02x%s",
(unsigned char)PyBytes_AS_STRING(p)[i],
(i + 1 < size) ? " " : "\n"
);
}
}
else
{
printf("  [ERROR] Invalid Bytes Object\n");
}
}
