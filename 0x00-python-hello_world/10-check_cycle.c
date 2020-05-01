#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: the list of nodes
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *aux = list;
	listint_t *current = list;

	while (aux != '\0' && aux->next != '\0')
	{
		current = current->next;
		aux = aux->next;
		aux = aux->next;
		if ((aux - current) == 0)
		{
			return (1);
		}
	}
	return (0);
}
