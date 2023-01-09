#include <Python.h>
#include <stdio.h>

void print_list_info(PyObject *p)
{
	// Get the length of the list
	int len = PyList_Size(p);
	// Get the allocated size of the list
	int alloc_size = PyList_GET_ALLOCATED_SIZE(p);
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
