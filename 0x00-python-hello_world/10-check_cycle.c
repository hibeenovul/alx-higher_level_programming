#include "lists.h"

/**
 * check_cycle - function to checks cycle
 * @list: pointer to the list
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *t2;
	listint_t *prev;

	t2 = list;
	prev = list;
	while (list && t2 && t2->next)
	{
		list = list->next;
		t2 = t2->next->next;

		if (list == t2)
		{
			list = prev;
			prev =  t2;
			while (1)
			{
				t2 = prev;
				while (t2->next != list && t2->next != prev)
				{
					t2 = t2->next;
				}
				if (t2->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
