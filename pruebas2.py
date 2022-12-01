class TreeNode:

    def __init__(self,data,children=[]):
        self.data = data
        self.children = children

    def __str__():
        

    def addChild(self,Treenode):
        self.children.append(Treenode)

        
tree = TreeNode("Drinks",[])
print(tree)
cold = TreeNode("cold",[])
hot = TreeNode("hot",[])
tree.addChild(hot)
tree.addChild(cold)

coffee = TreeNode("coffee",[])
tea = TreeNode("tea",[])
hot.addChild(coffee)
hot.addChild(tea)

cola = TreeNode("cola",[])
fanta = TreeNode("fanta",[])
cold.addChild(cola)
cold.addChild(fanta)
print(tree)