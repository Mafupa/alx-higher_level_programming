#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - check if a linked list has a cycle
 * @list: the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *lievre = list;
	listint_t *tortue = list;

	while (lievre && tortue)
	{
		lievre = lievre->next;
		if (!lievre)
			return (0);
		lievre = lievre->next;
		tortue = tortue->next;
		if (lievre == tortue)
			return (1);
	}
	return (0);
}
