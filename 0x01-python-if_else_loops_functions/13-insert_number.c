#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a number into sorted singly linked list
 *
 * @head: Pointer to head pointer
 * @number: Number to be inserted
 * Return: The address of the new node, or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *n;

	current = *head;

	n = malloc(sizeof(listint_t));
	if (n == NULL)
		return (NULL);

	n->n = number;
	n->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		n->next = *head;
		*head = n;
	}
	else
	{
		while (current->next != NULL && current->next->n < number)
			current = current->next;
		n->next = current->next;
		current->next = n;
	}

	return (n);
}
