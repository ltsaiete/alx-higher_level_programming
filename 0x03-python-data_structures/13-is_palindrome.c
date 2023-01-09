#include "lists.h"
#include <stdlib.h>

/**
 * _is_palindrome - Recursively traverse till the end of the list.
 * When returning from the last NULL, will be at the last node.
 * The last node is to be compared with the first node of the list.
 * @left: left node
 * @right: right node
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int _is_palindrome(listint_t **left, listint_t *right)
{
	int isp;

	if (right == NULL)
		return (1);

	if (_is_palindrome(left, right->next) == 0)
		return (0);

	isp = right->n == (*left)->n;
	*left = (*left)->next;

	return isp;
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: Head node of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);

	return (_is_palindrome(head, *head));
}
