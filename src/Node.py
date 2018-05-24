class Node:
    def __init__(self, data, left=None, right=None):
        self.value = data
        self.left = left
        self.right = right

    def __str__(self):
        print("d: {0}, l: {1}, r: {2}".format(self.value, self.left, self.right))

    def __repr__(self):
        return self.__str__()
