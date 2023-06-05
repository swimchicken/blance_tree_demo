import csv

couse_id = "2168"
search = "D000373050"


class hash_index:
    def __init__(self):
        self.data_dict = {}
        self.data_dict2 = {}

    def insert(self, data):
        student_id = data[0]
        if student_id not in self.data_dict:
            self.data_dict[student_id] = []
        self.data_dict[student_id].append([data[1], data[2]])

    def insert2(self, data):
        couse_id = data[1]
        if couse_id not in self.data_dict:
            self.data_dict[couse_id] = []
        self.data_dict[couse_id].append(data[0])

    def search(self, key):
        if key in self.data_dict:
            return self.data_dict[key]
        else:
            return None

    def search2(self, couse_id):
        if couse_id in self.data_dict:
            return self.data_dict[couse_id]
        else:
            return None


tree = hash_index()

# student_id screach

for i in range(0, 4654):
    file_name = f"reset_data_total/reset_data_total_{i}.csv"
    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            tree.insert(line)

results = tree.search(search)

# print(results)
print("學號:", search)

for result in results:
    print(result)

# course_id screach

for i in range(0, 4654):
    file_name = f"reset_data_total/reset_data_total_{i}.csv"
    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            tree.insert2(line)

student = tree.search2(couse_id)

print(student)
print("人數總共:", len(student))
