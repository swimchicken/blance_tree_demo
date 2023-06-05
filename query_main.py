import csv


class BalancedBinaryTree:
    def __init__(self):
        self.data_dict = {}

    def insert(self, data):
        student_id = data[0]
        if student_id not in self.data_dict:
            self.data_dict[student_id] = []
        self.data_dict[student_id].append(data[2])  # 存儲課程名稱

    def search(self, key):
        if key in self.data_dict:
            return self.data_dict[key]
        else:
            return None


tree = BalancedBinaryTree()

for i in range(0, 4654):
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
