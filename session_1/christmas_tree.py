import math

# Get the tree height
tree_height = int(input("Enter the height of the tree: "))

# Print the top of the tree
print(f"{"_"*((4*tree_height)+9)}")

for i in range(tree_height):
    # Print each row of the tree branches
    print(f"| {" "*((2*tree_height+1)-((i)-1))}{"*"*(2*i+1)}{" "*((2*tree_height+1)-((i)-1))} |")


for i in range(math.floor(tree_height/5)):
    print(f"| {" "*(2*tree_height-math.floor(tree_height/10))}|{" "*math.floor(tree_height)}|{" "*(2*tree_height-math.floor(tree_height/10))} |")

print(f"{"_"*((4*tree_height)+9)}")
