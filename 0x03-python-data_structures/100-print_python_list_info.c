#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info -  prints some basic info about Python lists.
 * @p: the python list object
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	// Get the length of the list
	int len = PyList_Size(p);
	// Get the allocated size of the list
	int alloc_size = ((PyListObject *)p)->allocated;
	int i;
	PyObject *item;

	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", alloc_size);

	// Iterate over the items in the list
	for (i = 0; i < len; i++)
	{
		// Get the item at the current index
		item = PyList_GetItem(p, i);

		// Print the type of the item
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
