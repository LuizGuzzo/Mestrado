# problema: https://open.kattis.com/problems/joinstrings

class Node:
    def __init__(self, string):
        self.string = string
        self.next = None

class LinkedList:
    def __init__(self,node):
        self.head = node
        self.tail = node

def append_to(l1, l2):
    l1.tail.next = l2.head
    l1.tail = l2.tail


# import sys
# input = sys.stdin.readline #fast input

n = int(input())

lists = [LinkedList(Node(input())) for _ in range(n)]
ultimo = 0


for i in range(n - 1):
    a, b = input().split()
    a = int(a)-1
    b = int(b)-1
    ultimo = a
    append_to(lists[a], lists[b])

current = lists[ultimo].head
while current:
    print(current.string.strip(), end='')
    current = current.next

"""
4
cute
cat
kattis
is
3 2
4 1
3 4
"""