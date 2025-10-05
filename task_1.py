class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"Node({self.value})"


class SinglyLinkedList:
    def __init__(self, iterable=None):
        self.head = None
        if iterable:
            for v in reversed(list(iterable)):
                self.push_front(v)

    def push_front(self, value):
        self.head = Node(value, self.head)

    def to_list(self):
        out = []
        curr = self.head
        while curr:
            out.append(curr.value)
            curr = curr.next
        return out

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev
        return self

    @staticmethod
    def _split(head):
        if not head or not head.next:
            return head, None
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow.next
        slow.next = None
        return head, middle

    @staticmethod
    def _merge_sorted(a, b):
        dummy = Node(0)
        tail = dummy
        while a and b:
            if a.value <= b.value:
                tail.next, a = a, a.next
            else:
                tail.next, b = b, b.next
            tail = tail.next
        tail.next = a or b
        return dummy.next

    def sort(self):
        def merge_sort(head):
            if not head or not head.next:
                return head
            left, right = self._split(head)
            left = merge_sort(left)
            right = merge_sort(right)
            return self._merge_sorted(left, right)

        self.head = merge_sort(self.head)
        return self

    @staticmethod
    def merge_two_sorted(list1, list2):
        a = list1.head if isinstance(list1, SinglyLinkedList) else list1
        b = list2.head if isinstance(list2, SinglyLinkedList) else list2
        head = SinglyLinkedList()
        head.head = SinglyLinkedList._merge_sorted(a, b)
        return head


if __name__ == "__main__":
    # Demo
    lst = SinglyLinkedList([4, 2, 5, 1, 3])
    print("Initial:", lst.to_list())
    lst.reverse()
    print("Reversed:", lst.to_list())
    lst.sort()
    print("Sorted:", lst.to_list())

    a = SinglyLinkedList([1, 3, 5])
    b = SinglyLinkedList([2, 4, 6, 7])
    merged = SinglyLinkedList.merge_two_sorted(a, b)
    print("Merged:", merged.to_list())
