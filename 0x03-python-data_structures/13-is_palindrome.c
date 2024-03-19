#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - is linked list a palindrome
 * @head: point to list head
 * Return: node number
 */

int is_palindrome(listint_t **head)
{
	listint_t *i = *head, *j = *head;
	listint_t *nxt = NULL, *prv = NULL;
	listint_t *left = NULL, *right = NULL;

	if (*head == NULL || (*head)->nxt == NULL)
		return (1);
	/*Find the middle of linked list*/
	while (j != NULL && j->nxt != NULL)
	{
		j = j->nxt->nxt;
		prv = i;
		i = i->next;
	}
	/*Reverse the second part of the linked list*/
	prv->nxt = NULL;
	while (i != NULL)
	{
		nxt = i->nxt;
		i->nxt = prv;
		prev = slow;
		i = nxt;
	}
	/*is it palindrome*/
	left = *head;
	right = prev;
	while (left != NULL && right != NULL)
	{
		if (left->n != right->n)
			return (0);
		left = left->nxt;
		right = right->nxt;
	}
	return (1);
}
