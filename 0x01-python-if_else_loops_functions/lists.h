#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct Node - singly linked list
 * @data: integer
 * @next_node: points to the next node
 *
 * Description: singly linked list node structure
 *
 */
typedef struct Node
{
	int data;
	struct Node *next_node;
} Node;

size_t print_linked_list(const Node *head);
Node *add_node_to_end(Node **head, const int data);
void free_linked_list(Node *head);
Node *insert_node_sorted(Node **head, int data);

#endif /* LISTS_H */
