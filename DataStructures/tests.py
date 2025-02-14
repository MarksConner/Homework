import unittest
from List import List
from Queue import Queue
from Stack import Stack

class TestList(unittest.TestCase):
    def test_add(self):
        list1 = List()
        list1.add(5)
        self.assertEqual(list1.get_all(), [5])
    
    def test_remove(self):
        lst = List()
        lst.add(5)
        lst.remove(5)
        self.assertEqual(lst.get_all(), [0])

class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.peek(), 1)
    
    def test_pop(self):
        stack = Stack()
        stack.push(2)
        stack.pop()
        self.assertEqual(stack.peek(), 1)
        stack.pop()
        self.assertTrue(stack.is_empty())

class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(5)
        self.assertEqual(queue.peek(), 5)
    
    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(5)
        queue.dequeue()
        self.assertEqual(queue.peek(), 4)
        queue.dequeue(4)
        self.assertTrue(queue.is_empty())

if __name__ == '__main__':
    unittest.main()
