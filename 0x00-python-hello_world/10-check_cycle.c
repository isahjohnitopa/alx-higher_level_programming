#include "lists.h"


/**
 * _realloc - Function that reallocates a memory block
 * @ptr: The pointer to the previous memory block
 * @old_size: The size of the old memory block
 * @new_size: The size of the new memory block
 *
 * Return: Return the pointer to the new memory block, otherwise NULL
 */
void *_realloc(void *ptr, unsigned int old_size, unsigned int new_size)
{
	void *new_ptr;
	unsigned int min_size = old_size < new_size ? old_size : new_size;
	unsigned int i;

	if (new_size == old_size)
		return (ptr);
	if (ptr != NULL)
	{
		if (new_size == 0)
		{
			free(ptr);
			return (NULL);
		}
		new_ptr = malloc(new_size);
		if (new_ptr != NULL)
		{
			for (i = 0; i < min_size; i++)
				*((char *)new_ptr + i) = *((char *)ptr + i);
			free(ptr);
			return (new_ptr);
		}
		free(ptr);
		return (NULL);
	}
	else
	{
		new_ptr = malloc(new_size);
		return (new_ptr);
	}
}


/**
 * check_cycle - Function that checks if a singly linked list has a cycle in it
 * @list: The list head
 *
 * Return: Return 1 if yes and 0 if no
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow = list;

	if (!list)
		return (0);

	fast = list->next;
	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}


/**
 * print_listint - Function to prints all elements of a lintint_t list
 * @h: The pointer to the head of the list
 *
 * Return: Return the number of nodes
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n;

	current = h;
	n = 0;
	while (current != NULL)
	{
		printf("%i\n", current->n);
		current = current->next;
		n++;
	}
	return (n);
}


/**
 * add_nodeint - Function to add a new node at the beginning
 *		of a listint_t list
 * @head: The pointer to a pointer of the start of the list
 * @n: The integer to be add to the node
 *
 * Return: Return the address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = n;
	new->next = *head;
	*head = new;

	return (new);
}


/**
 * free_listint - Function to free a listint_t list
 * @head: The pointer to list to be freed
 *
 * Return: nothing
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
