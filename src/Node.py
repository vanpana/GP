class Node:
    def __init__(self, data, left=None, right=None):
        self.value = data
        self.left = left
        self.right = right

    def __str__(self):
        if self.left is not None and self.right is not Node:
            return "(" + str(self.left) + " " + str(self.value) + " " + str(self.right) + ")"
        return str(self.value)

    def __repr__(self):
        return self.__str__()
