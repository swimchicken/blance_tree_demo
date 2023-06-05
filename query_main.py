import csv


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BalancedBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)

        else:
            current = self.root
            while 1:
                # ----------
                if data[0] < current.data[0]:
                    if current.left is None:
                        current.left = Node(data)
                        break
                    else:
                        current = current.left

                # ----------
                else:
                    if current.right is None:
                        current.right = Node(data)
                        break
                    else:
                        current = current.right

    def search(self, key):

        result_serch = []
        current = self.root
        while current is not None:
            if current.data[0] == key:
                result_serch.append(current.data[2])
            elif key < current.data[0]:
                current = current.left
            else:
                current = current.right

        return result_serch


tree = BalancedBinaryTree()

for i in range(0, 4653):
    file_name = f"reset_data_total/reset_data_total_{i}.csv"
    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            tree.insert(line)

search = "D000373050"
results = tree.search(search)

print(results)

if results:
    for result in results:
        print(result)
else:
    print("None")
