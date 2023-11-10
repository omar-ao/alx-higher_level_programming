#include "Python.h"

void print_python_bytes(PyObject *p);
/**
 * print_python_list - Prints some basic infor about python lists
 *
 * @p: Pointer to python object
 */
void print_python_list(PyObject *p)
{
	PyListObject *pp;
	int i;

	pp = (PyListObject *) p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", pp->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", pp->allocated);
	for (i = 0; i < (int) pp->ob_base.ob_size; i++)
	{
		printf("Element %d: %s\n", i, pp->ob_item[i]->ob_type->tp_name);
		if (PyBytes_Check(pp->ob_item[i]))
		{
			print_python_bytes(pp->ob_item[i]);
		}
	}
}

/**
 * print_python_bytes - Prints byte objects
 *
 * @p: Pointer to p
 */
void print_python_bytes(PyObject *p)
{
	char *s;
	int size, bytes, i;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		size = PyBytes_Size(p);
		s = PyBytes_AsString(p);
		printf("  size: %d\n", size);
		printf("  trying string: %s\n", s);
		bytes = (size < 10) ? size + 1 : 10;
		printf("  first %d bytes: ", bytes);
		for (i = 0; i < bytes ; i++)
		{
			printf("%02x", s[i] & 0xff);
			if ((i + 1) != bytes)
				printf(" ");
		}
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}
