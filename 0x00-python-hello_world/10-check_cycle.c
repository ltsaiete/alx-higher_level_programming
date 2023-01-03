#include "lists.h"

/**
 * _check_cycle - checks if current node is equal to head node.
 * @head: head node
 * @current: Current node
 *
 * Return: 1 if current node is equal to head node,0 if not.
 */

int _check_cycle(listint_t *head, listint_t *current)
{
	if (current == head)
		return (1);
	if (current == NULL)
		return (0);

	return (_check_cycle(head, current->next));
}

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: The list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;
	int result = 0;

	if (list == NULL)
		return (0);

	temp = list;
	while (temp != NULL)
	{
		result = _check_cycle(temp, temp->next);
		if (result == 1)
			break;
		temp = temp->next;
	}
	return (result);
}
