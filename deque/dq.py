from logger import Logger

log = Logger("deque")


class Node:
    def __init__(self, key: any, val: any, next_node=None) -> None:
        """Instantiate a Node object

        Args:
            key (any): Value stored in the Node
            val (any): Value stored in the Node
            next_node (Node, optional): Node that is next in the deque. Defaults to None.
        """
        self.__key = key
        self.__val = val
        self.__next = next_node

    @property
    def key(self) -> any:
        return self.__key

    @key.setter
    def key(self, new_key) -> None:
        if new_key is not None:
            self.__key = new_key

    @property
    def val(self) -> any:
        return self.__val

    @val.setter
    def val(self, new_value) -> None:
        if new_value is not None:
            self.__val = new_value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, new_next):
        if new_next is not None:
            self.__next = new_next

    def __str__(self) -> str:
        return f"[{self.key}|{self.val}]"


class Deque:
    def __init__(self, head: Node = None, size: int = 0) -> None:
        self.__head = head
        self.__size = size

    @property
    def head(self) -> Node:
        return self.__head

    @head.setter
    def head(self, new_head) -> None:
        self.__head = new_head

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, new_size) -> None:
        self.__size = new_size

    @property
    def tail(self) -> Node | None:
        if self.size == 0:
            return None
        if self.size == 1:
            return self.head

        cur = self.head
        while cur is not None:
            cur = cur.next

        return cur

    def append(self, append_node: Node = None) -> None:
        self.tail.next = append_node

    def push(self, key: any, value: any) -> None:
        new_head = Node(key, value, self.head)
        self.head = new_head

    def pop_front(self) -> Node:
        pass

    def pop_back(self) -> Node:
        pass

    def __str__(self) -> str:
        result = f""
        cur = self.head
        while cur.next is not None:
            result += f"{cur} -> "
            cur = cur.next
        result += f"{cur}"
        return result
