#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a node in a sorted linked list
 * @head: the head of the linked list
 * @number: the number to insert
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cur = *head, *next;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	while ((next = cur->next))
	{
		
		if (next->n >= number)
		{
			new->n = number;
			new->next = next;
			cur->next = new;
			return (new);
		}
		cur = next;
	}
	return (NULL);
}

