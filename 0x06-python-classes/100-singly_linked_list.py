#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, value, next_node=None):
        """Initialize a new Node.

        Args:
            value (int): The value of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.value = value
        self.next_node = next_node

    @property
    def value(self):
        """Get/set the value of the Node."""
        return self.__value

    @value.setter
    def value(self, value):
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        self.__value = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.value > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.value < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.value))
            tmp = tmp.next_node
        return '\n'.join(values)
