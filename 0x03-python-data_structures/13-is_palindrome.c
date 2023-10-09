#include "lists.h"
#include <stddef.h>

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
