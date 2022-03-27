import unittest
import time
from logger import Logger
from dq import Deque, Node

log = Logger("deque_test")

class NodeTest(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_object_not_none(self):
        log("Started node existance test")
        start_time = time.perf_counter()
        node = Node(1, 'a')
        log(f"[+] Created node {node}", 'd')
        self.assertIsNotNone(node)
        elapsed_time = time.perf_counter() - start_time
        log(f"Completed existance test in {elapsed_time:.5f}")

    def test_create_single_instance(self):
        log("Started create single node instance test")
        start_time = time.perf_counter()
        node = Node(1, 'a')
        log(f"[+] Created new node {node}]", 'd')
        self.assertEqual(node.key, 1)
        self.assertEqual(node.val, 'a')
        elapsed_time = time.perf_counter() - start_time
        log(f"Completed create single instance test in {elapsed_time:.5f}")

    def test_create_multiple_instances(self):
        log("Started multiple node instance test")
        start_time = time.perf_counter()
        n1 = Node(1, 'a')
        log(f"[+] Created new node {n1}", 'd')
        n2 = Node(2, 'b')
        log(f"[+] Created new node {n2}", 'd')
        self.assertNotEqual(n1, n2)
        self.assertNotIsInstance(n1, n2)
        elapsed_time = time.perf_counter() - start_time
        log(f"Completed multiple instance test in {elapsed_time:.5f}")        

    def test_two_linked_nodes(self):
        log("Started linked nodes test")
        start_time = time.perf_counter()
        node = Node(1, 'a')
        log(f"[+] Created new node {node}", 'd')
        next_node = Node(2, 'b')
        log(f"[+] Created new node {next_node}", 'd')
        node.next = next_node
        self.assertNotEqual(node, next_node)
        self.assertEqual(next_node, node.next)
        self.assertEqual(node.key, 1)
        self.assertEqual(node.val, 'a')
        self.assertEqual(next_node.key, 2)
        self.assertEqual(next_node.val, 'b')
        self.assertEqual(node.next.key, 2)
        self.assertEqual(node.next.val, 'b')
        log(f"[*] Linked nodes {node} -> {next_node}", 'd')
        elapsed_time = time.perf_counter() - start_time
        log(f"Completed linked nodes test in {elapsed_time:.5f}")

class DequeTest(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_object_not_none(self):
        log("Started deque existance test")
        start_time = time.perf_counter()
        dq = Deque()
        self.assertIsNotNone(node)
        elapsed_time = time.perf_counter() - start_time
        log(f"Completed existance test in {elapsed_time:.5f}")