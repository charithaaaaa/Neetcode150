class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_node(head, pos):

    if head is None:
        return None

    # Delete first node
    if pos == 1:
        return head.next

    # Delete last node
    if pos == -1:
        if head.next is None:
            return None

        temp = head
        while temp.next.next:
            temp = temp.next

        temp.next = None
        return head

    # Delete node at given position
    temp = head
    for i in range(pos - 2):
        temp = temp.next

    if temp.next:
        temp.next = temp.next.next

    return head


def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")


# Create Linked List
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

print("Original List:")
print_list(head)


# Example 1: Delete first node
head = delete_node(head, 1)
print("After deleting first node:")
print_list(head)


# Example 2: Delete last node
head = delete_node(head, -1)
print("After deleting last node:")
print_list(head)


# Example 3: Delete node at position 2
head = delete_node(head, 2)
print("After deleting position 2:")
print_list(head)