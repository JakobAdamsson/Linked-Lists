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
        prev_ele = self.prev_node(node.value)
        while node.next != None:
            print(node.value)
            node = node.next
            prev_ele = self.prev_node(node.value)
    
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
                print(f'Properties of chosen value: |{prev_node.value}|<---left node|{value}|right node--->|{cur_node.next.value}|')
                return
            cur_node = cur_node.next
        cur_node.next = node
        return 'Value not found'
                
    
    def swap(self, value, value2):
        if value == value2:
            return

        prev_value = None
        cur_value = self.first
        while cur_value != None and cur_value.value != value:
            prev_value = cur_value
            cur_value = cur_value.next
        
        prev_value2 = None
        cur_value2 = self.first
        while cur_value2 != None and cur_value2.value != value2:
            prev_value2 = cur_value2
            cur_value2 = cur_value2.next
        if cur_value == None or cur_value2 == None:
            return
        
        if prev_value != None:
            prev_value.next == cur_value2
        else:
            self.head = prev_value
        if prev_value2 != None:
            prev_value2.next == cur_value
        else:
            self.head = cur_value
        temp = cur_value.next
        cur_value.next = cur_value2.next
        cur_value2.next = temp
        
                
                
    def update(self, value, new_val):
        """Updates value of a node"""
        new_node = Node(value)
        cur_node = self.first
        prev_node = self.prev_node(cur_node.value)
        replaced = False
        while cur_node.next != None:
            if replaced == False:
                if cur_node.value == value:
                    cur_node.value = new_val
                    replaced = True
            cur_node = cur_node.next
        cur_node.next = new_node
        
                
                        

lst = [2,3,5,67,98,92,1,2,3,5,7]
link = Linklst()
for i in lst:
    link.append(i)


link.update(67, 13)

link.show_link()



