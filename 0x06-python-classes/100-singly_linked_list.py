#!/usr/bin/python3
"""
This is a simple module and it only has
one class called Node
"""


class Node:
    """
    This class defines a node of a singly linked list

    Args:
        data(int): Data of the node
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) != Node and value != None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """
    This class defines  singly linked list

    Args:
        data(int): Data of the node
    """

    def __init__(self):
        self.__head = None

    def test(self):
        aux = self.__head
        data = ''
        while aux != None:
            # data += str(aux.data) + '\n'
            print(aux.data)
            aux = aux.next_node

    def sorted_insert(self, value):
        if self.__head == None:
            self.__head = Node(value)
        else:
            next = self.__head.next_node
            while next != None:
                next = next.next_node
            next = Node(value)
