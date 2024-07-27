#!/usr/bin/python3
"""This is the `100-singly_linked_list.py` module"""


class Node:
    """Defines node class"""
    
    def __init__(self, data, next_node=None):
        """Instantiates a new node"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Retrevies data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets data"""
        if not isinstance(value, int):
            raise Exception("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets next_node"""
        if value is not None or not isinstance(self):
            raise Exception("next_node must be a Node object")


class SinglyLinkedList:
    """Defines SinglyLinkedList class"""
    
    def __init__(self):
        """Instantiates new linked list"""
        self.__head = None
    
    def __str__(self):
        lst = []
        current = self.__head
        while current:
            lst.append(current.data)
            current = current.next_node
        return "{}".format(lst)

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in
        the list (increasing order)
        """
        if self.__head is None:
            self.__head = Node(value)
        head = self.__head
        new_node = Node(value, head)
        self.__head = new_node
