class TreeNode:
    def __init__(self, name):
        self.name = name 
        self.children = [] 

    def add_child(self, child_node):
        self.children.append(child_node)
    def display(self, level=0):
        print(" " * (level * 4) + f"- {self.name}")
        for child in self.children:
            child.display(level + 1)
root = TreeNode("Building Management System")
hvac = TreeNode("HVAC System")
lighting = TreeNode("Lighting System")
elevators = TreeNode("Elevator System")
security = TreeNode("Security System")

root.add_child(hvac)
root.add_child(lighting)
root.add_child(elevators)
root.add_child(security)
hvac.add_child(TreeNode("Temperature Control"))
hvac.add_child(TreeNode("Air Quality Monitoring"))
lighting.add_child(TreeNode("Energy Optimization"))
lighting.add_child(TreeNode("Fault Detection"))
security.add_child(TreeNode("Fire Alarms"))
security.add_child(TreeNode("Surveillance Cameras"))
security.add_child(TreeNode("Access Control"))
print("Hierarchical Structure of Building Management System:")
root.display()
