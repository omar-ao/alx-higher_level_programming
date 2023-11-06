#include "lists.h"

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

	current = origin = *head;

	if (head == NULL || (*head)->next == NULL)
		return (1);

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
			return (1);
		reverse = reverse->next;
		origin = origin->next;
	}
	return (1);
}
