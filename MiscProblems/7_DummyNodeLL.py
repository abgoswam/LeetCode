'''
(1)
Implement a non-generic data structure MyQueue of dynamic, unspecified size that has the following interface:
  void push_back(int): Add the element to the back of the queue. Runtime: O(1)
  int pop_front(): Remove and return the value at the front of the queue. If queue is empty, return -1. Runtime: O(1)
  string stringify(): Return the values in the queue, from front to back, as a string with no delimiter. Return an empty string if the queue is empty. Runtime: O(N)

* Do not use any built-in data structures. This means you cannot use Javascript arrays, Swift arrays, Java ArrayLists, Python lists, etc. You are free to build any data structures you want.
* Run-time requirements are _not_ amortized. This means that worst case (not average case) has to be O(1) for push_back and pop_front.
* Assume input is well-formed
* Only use the Run button after you’ve implemented the required methods

(2)
Add the following method to your data structure:
  int pop_back(): Remove and return the value at the tail of the queue. If queue is empty, return -1. Runtime: O(1)
'''

# import pytest


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class MyQueue():
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def push_back(self, value):
        node = Node(value)

        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

        return

    def _pop(self, n):
        n_prev = n.prev
        n_next = n.next
        n_prev.next = n_next
        n_next.prev = n_prev

        return n.value

    def pop_front(self):
        if self.head.next == self.tail:
            return -1
        return self._pop(self.head.next)

    def pop_back(self):
        if self.head.next == self.tail:
            return -1
        return self._pop(self.tail.prev)

    def stringify(self):
        return_string = ""
        temp = self.head.next

        while temp != self.tail:
            return_string += str(temp.value)
            temp = temp.next

        return return_string

def test1():
    q = MyQueue()
    q.push_back(1)
    print(q.stringify())
    q.push_back(2)
    print(q.stringify())
    q.push_back(3)
    print(q.stringify())
    q.push_back(4)
    print(q.stringify())

    assert "1234" == q.stringify()
    assert 1 == q.pop_front()  # pop 1
    print(q.stringify())

    assert 2 == q.pop_front()  # pop 2
    print(q.stringify())

    assert 3 == q.pop_front()  # pop 3
    print(q.stringify())

    assert 4 == q.pop_front()  # pop 4
    print(q.stringify())

    assert -1 == q.pop_front()  # Nothing to pop, return -1
    print(q.stringify())


def test2():
    q = MyQueue()
    q.push_back(1)
    assert  1 == q.pop_front()   # pop 1
    q.push_back(2)
    q.push_back(3)
    assert  2 == q.pop_front()   # pop 2
    assert  3 == q.pop_front()   # pop 3
    assert  "" == q.stringify()
    assert -1 == q.pop_front()   # Nothing to pop, return -1

def test3():
    q = MyQueue()
    q.push_back(1)
    q.push_back(2)
    q.push_back(3)
    q.push_back(4)
    assert  "1234" == q.stringify()
    assert  4 == q.pop_back()    # pop 4
    assert  3 == q.pop_back()    # pop 3
    assert  2 == q.pop_back()    # pop 2
    assert  1 == q.pop_back()    # pop 1
    assert -1 == q.pop_back()    # Nothing to pop, return -1

def test4():
    q = MyQueue()
    q.push_back(1)
    assert  1 == q.pop_back()   # pop 1
    q.push_back(2)
    q.push_back(3)
    assert  3 == q.pop_back()   # pop 3
    assert  2 == q.pop_back()   # pop 2
    assert  "" == q.stringify()
    assert -1 == q.pop_back()   # Nothing to pop, return -1

# pytest.main()