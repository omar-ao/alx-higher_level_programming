#include "lists.h"

/**
 * check_cycle - Checks if a single linked list has a cycle in it
 *
 * @list: Pointer to list head
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *bolt = list; /* usain bolt */
	listint_t *hart = list; /* kevin hart */

	while (bolt != NULL && bolt->next != NULL)
	{
		bolt = bolt->next->next;
		hart = hart->next;

		if (bolt == hart)
			return (1);
	}
	return (0);
}
