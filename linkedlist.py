class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None
    

class Linklst:
    def __init__(self):
        self.first = Node()
    
    def append(self, value):
        new_node = Node(value)
        cur_node = self.first
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node
    
    def show_link(self):
        node = self.first
        while node.next != None:
            print(node.value, node.next.value)
            node = node.next
    
    def count_elems(self):
        node = self.first
        counter = 0
        while node.next != None:
            counter += 1
            node = node.next
        return counter


    def prev_node(self, value):
        node = Node(value)
        cur_node = self.first
        while cur_node.next != None:
            if cur_node.next.value == node.value:
                return cur_node
            cur_node = cur_node.next
        cur_node.next = node


    def pop(self, value):
        node = Node(value)
        cur_node = self.first
        prev_node = self.prev_node(value)
        while cur_node.next != None:
            if cur_node.value == node.value:
                prev_node.next = cur_node.next
            cur_node = cur_node.next
        cur_node.next = node.next                
                
    
    def peek(self, value):
        node = Node(value)
        cur_node = self.first
        prev_node = self.prev_node(value)
        while cur_node.next != None:
            if cur_node.value == node.value:
                print(f'Properties of chosen value: value -> {node.value}, next node -> {cur_node.next.value}, prev node -> {prev_node.value}')
                return
            cur_node = cur_node.next
        cur_node.next = node
        return 'Value not found'
                
    
    def swap(self, value, value2):
        node = Node(value)
        node2 = Node(value2)
        node_prev = self.prev_node(value)
        node2_prev = self.prev_node(value2)
        cur_node = self.first
        while cur_node.next != None:
            if cur_node.value == node.value:
                node = node2
                node.prev = node2_prev
                node.next = node2.next
                node2 = cur_node
                node2.prev = node_prev
                node2.next = node.next
                break
            cur_node = cur_node.next
        cur_node.next = node
                
                
                

lst = [2,3,5,67,98,92,1,2,3,5,7]
link = Linklst()
for i in lst:
    link.append(i)
link.show_link()
print('---------')
link.swap(98,1)
link.show_link()
#print(link.prev_node(98))
#link.show_link()
