#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 *
 * @head: Pointer to pointer to list
 * Return: 0 if list is not palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *reverse, *origin, *current, *next;
	listint_t *prev = NULL;

	if (*head == NULL)
		return (1);
	else if ((*head)->next == NULL)
		return (1);

	current = origin = *head;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	reverse = prev;

	while (reverse != NULL && origin == NULL)
	{
		if (reverse->n != origin->n)
			return (0);
		printf("%d\n%d\n", reverse->n, origin->n);
		reverse = reverse->next;
		origin = origin->next;
	}
	return (1);
}
