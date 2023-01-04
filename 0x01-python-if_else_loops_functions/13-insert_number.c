#include "lists.h"
#include <stdio.h>

/**
 * insert_node -  inserts a number into a sorted singly linked list.
 * @head: head node of the list
 * @number: number to add to the list
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new;

	current = malloc(sizeof(listint_t));
	new = malloc(sizeof(listint_t));
	if (current == NULL || new == NULL)
	{
		return (NULL);
	}

	current = *head;
	new->n = number;
	new->next = NULL;
	if (current == NULL || current->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (current != NULL)
	{
		if (current->next == NULL)
		{
			current->next = new;
			break;
		}
		if (current->next->n > number)
		{
			new->next = current->next;
			current->next = new;
			break;
		}
		current = current->next;
	}
	current = NULL;
	free(current);
	return (new);
}
