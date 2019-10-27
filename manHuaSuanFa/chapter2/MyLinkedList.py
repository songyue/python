#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 链表节点
class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# 链表
class MyLinkedList(object):
    def __init__(self):
        # 头节点指针
        self.__head = Node()
        # 尾节点指针
        self.__last = Node()
        # 链表实际长度
        self.__size = 0

    '''
    链表插入元素
    @param data  插入元素
    @param index 插入位置 
    '''
    def insert(self,data, index):
        if index < 0 or index > self.__size:
            raise RuntimeError("超出数组实际元素范围！")

        insertedNode = Node(data)
        if self.__size == 0:
            # 空链表
            self.__head = insertedNode
            self.__last = insertedNode
        elif index == 0:
            # 头部插入
            insertedNode.next = self.__head
            self.__head = insertedNode
        elif index == self.__size:
            # 尾部插入
            self.__last.next = insertedNode
            self.__last = insertedNode
        else:
            # 中间插入
            prevNode = self.get(index-1)
            insertedNode.next = prevNode.next
            prevNode.next = insertedNode

        self.__size = self.__size+1

    def remove(self,index):
        if index < 0 or index > self.__size:
            raise RuntimeError("超出数组实际元素范围！")

        removeNode = None
        if index == 0:
            # 删除头节点
            removeNode = self.__head
            self.__head = self.__head.next
        elif index == self.__size -1:
            #删除尾节点
            prevNode = self.get(index-1)
            removeNode = prevNode.next
            prevNode.next = None
            last = prevNode
        else:
            #删除中间节点
            prevNode = self.get(index-1)
            nextNode = prevNode.next.next
            removeNode = prevNode.next
            prevNode.next = nextNode

        self.__size = self.__size + 1 
        return removeNode

    def get(self,index):
        if index < 0 or index > self.__size:
            raise RuntimeError("超出数组实际元素范围！")

        temp = self.__head
        n = 0
        while n < index:
            temp = temp.next
            n =n+1

        return temp


    def output(self):
        temp = self.__head
        while temp != None:
            print(temp.data)
            temp = temp.next



myLinkedList = MyLinkedList()
myLinkedList.insert(3,0)
myLinkedList.insert(7,1)
myLinkedList.insert(9,2)
myLinkedList.insert(5,3)
myLinkedList.insert(6,1)
myLinkedList.output()
myLinkedList.remove(2)
print("删除index：2后的数组")
myLinkedList.output()


