#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: address of the head of the linked list
 * @number: number to insert in the linked list
 *
 * Return: Address of the new node or null if it fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *aux = *head;
	listint_t *m;

	m = malloc(sizeof(listint_t));
	if (m == '\0')
	{
		return ('\0');
	}
	m->n = number;
	if (*head == '\0' || aux->n >= number)
	{
		m->next = aux;
		*head = m;
		return (m);
	}
	while (aux->next != '\0' && aux->next->n <= number)
	{
		aux = aux->next;
	}
	m->next = aux->next;
	aux->next = m;
	return (m);
}
