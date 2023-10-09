#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - check's if a linked list is a palindrome
 * @head: the lists head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tortue = *head, *lievre = *head, *temp, *prev = NULL;

	while (lievre && lievre->next)
	{
		lievre = lievre->next->next;
		tortue = tortue->next;
	}
	while (tortue)
	{
		temp = tortue->next;
		tortue->next = prev;
		prev = tortue;
		tortue = temp;
	}
	tortue = *head;
	lievre = prev;
	while (lievre)
	{
		if (tortue->n != lievre->n)
			return (0);
		lievre = lievre->next;
		tortue = tortue->next;
	}
	return (1);
}
