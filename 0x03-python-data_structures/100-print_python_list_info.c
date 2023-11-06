#include "Python.h"

/**
 * print_python_list_info - Prints some basic info about Python lists
 *
 * @p: Pointer to Python Object
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *pp;
	int i;

	pp = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", pp->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", pp->allocated);

	for (i = 0; i < (int) pp->ob_base.ob_size; i++)
	{
		printf("Element %d: %s\n", i, pp->ob_item[i]->ob_type->tp_name);
	}
}
