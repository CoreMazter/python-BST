class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        node = Node(data)
        if self.root == None:
            self.root = node
        else:
            aux = self.root
            while True:
                if node.data < aux.data:
                    if not aux.left_child:
                        node.parent = aux
                        aux.left_child = node
                        return
                    else:
                        aux = aux.left_child 
                else:
                    if not aux.right_child:
                        node.parent = aux
                        aux.right_child = node
                        return
                    else:
                        aux = aux.right_child

    @staticmethod
    def postorder(node):
        if not node: return
        
        BinarySearchTree.postorder(node.left_child)
        BinarySearchTree.postorder(node.right_child)
        print(node.data)

    def print_postorder(self):
        self.postorder(self.root)
        
    
    
    
        

class Node:
    def __init__(self,data):
        self.data=data
        self.left_child = None
        self.right_child = None
        self.parent = None
    
if __name__ == "__main__":
    bst = BinarySearchTree()
    for i in [1,1.1,0.9]:
        bst.insert(i)
    bst.print_postorder()