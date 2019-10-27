#!/usr/bin/python3
# -*- coding: UTF-8 -*-

class MyArray(object):
    def __init__(self, capacity):
        # 生成一个capacity长度的列表数组
        self.__array = [0 for _ in range(capacity)] 
        self.__size = 0

    def insert(self, element, index):
        if index < 0 or index > self.__size:
            raise RuntimeError("超出数组实际元素范围！")

        # 如果实际元素达到数组容量上限，则对数组进行扩容
        if self.__size >= len(self.__array):
            self.__resize()

        n = self.__size -1;
        while n >= index :
            self.__array[n+1] = self.__array[n]
            n=n-1
        self.__array[index] = element
        self.__size = self.__size + 1

    def delete(self, index):
        if index < 0 or index > self.__size:
            raise RuntimeError("超出数组实际元素范围！")

        deleteElement = self.__array[index];
        n = index
        while n < self.__size-1:
            self.__array[n] = self.__array[n+1]
            n = n+1;

        self.__size = self.__size - 1
        return deleteElement

    def __resize(self):
        arrayNew = [0 for _ in range(len(self.__array))]
        self.__array[len(self.__array):len(self.__array)] = arrayNew;


    def output(self):
        n = 0
        while n < self.__size:
            print(self.__array[n])
            n = n + 1


myArray = MyArray(4);
myArray.insert(3,0);
myArray.insert(7,1);
myArray.insert(9,2);
myArray.insert(5,3);
myArray.insert(6,1);
myArray.output();
myArray.delete(2);
print("删除index：2后的数组");
myArray.output();
