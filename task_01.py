class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    # Функція для реверсування зв'язного списку
    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    # Функція для сортування зв'язного списку
    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return

        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list

    # Функція для вставки вузла в зв'язний список
    def sorted_insert(self, sorted_list, new_node):
        if sorted_list is None or sorted_list.data >= new_node.data:
            new_node.next = sorted_list
            return new_node

        current = sorted_list
        while current.next and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
        return sorted_list
    
    # Функція для об'єднання двох зв'язних списків
    def merge_sorted_lists(self, list1, list2):
        merged_list = LinkedList()
        current1 = list1.head
        current2 = list2.head

        while current1 and current2:
            if current1.data < current2.data:
                merged_list.insert_at_end(current1.data)
                current1 = current1.next
            else:
                merged_list.insert_at_end(current2.data)
                current2 = current2.next

        while current1:
            merged_list.insert_at_end(current1.data)
            current1 = current1.next

        while current2:
            merged_list.insert_at_end(current2.data)
            current2 = current2.next

        return merged_list

if __name__ == "__main__":
    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)

    # Вставляємо вузли в кінець
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    # Друк зв'язного списку
    print("Зв'язний список:")
    llist.print_list()

    # Реверсуємо зв'язний список
    llist.reverse_list()

    print("\nЗв'язний список після реверсування:")
    llist.print_list()

    # Сортуємо зв'язний список
    llist.insertion_sort()

    print("\nЗв'язний список після сортування:")
    llist.print_list()

    llist1 = LinkedList()
    llist1.insert_at_end(1)
    llist1.insert_at_end(2)
    llist1.insert_at_end(3)
    llist1.insert_at_end(4)
    llist1.insert_at_end(5)
    llist1.insert_at_end(6)

    print("\nДругий відсортований список:")
    llist1.print_list()

    merged_list = llist1.merge_sorted_lists(llist, llist1)
    print("\nОб'єднаний відсортований список:")
    merged_list.print_list()