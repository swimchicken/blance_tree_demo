import csv

# 設定初始值
course_id = "3780"
search = "D000373050"


class HashIndex:

    # 建立空的字典陣列，其中分成兩種搜尋方式的字元陣列
    def __init__(self):
        self.data_dict = {}
        self.data_dict2 = {}

    # hash_function ==> 取魔術

    def hash_function(self, key):
        return int(key[1:]) % 100001

    def fun2(self, key):
        return int(key) % 10001
    # 指定key:value，其中value是array()
    def insert(self, data):
        student_id = data[0]
        hash_key = self.hash_function(student_id)
        if hash_key not in self.data_dict:
            self.data_dict[hash_key] = []
        self.data_dict[hash_key].append([data[1], data[2]])

    def insert2(self, data):
        course_id = data[1]
        hash_key = self.fun2(course_id)
        if hash_key not in self.data_dict2:
            self.data_dict2[hash_key] = []
        self.data_dict2[hash_key].append(data[0])

    # 透過查找字典上的"key-index相符合，去輸出相關資料"
    def search(self, key):
        hash_key = self.hash_function(key)
        if hash_key in self.data_dict:
            return self.data_dict[hash_key]
        else:
            return None

    def search2(self, key):
        hash_key = self.fun2(key)
        if hash_key in self.data_dict2:
            return self.data_dict2[hash_key]
        else:
            return None


tree = HashIndex()

# student_id search

for i in range(0, 4654):
    file_name = f"reset_data_total/reset_data_total_{i}.csv"
    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # 跳過開頭
        for line in reader:
            tree.insert(line)

results = tree.search(search)

print("學號:", search)

if results:
    for result in results:
        print(result)
else:
    print("找不到該學號的相關資料")

# course_id search

for i in range(0, 4654):
    file_name = f"reset_data_total/reset_data_total_{i}.csv"
    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            tree.insert2(line)

students = tree.search2(course_id)

print("課程編號:", course_id)

print(sorted(list(dict.fromkeys(students))))

print(len(sorted(list(dict.fromkeys(students)))))
