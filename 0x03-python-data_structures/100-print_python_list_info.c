#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints python list info
 * @p: PyObject
 */
void print_python_list_info(PyObject *p)
{
	long int i = 0, size = PyList_Size(p);
	PyListObject *obj = (PyListObject *)p;
	PyObject *item;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %li: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
