import os
import csv

# 讀取檔案
with open("DB_students_tc_utf8.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    data = list(reader)

'''
header = data[0]
data = data[1:]
'''

sorted_data = sorted(data[1:], key=lambda x: int(x[0][1:]))

# print(sorted_data)

output_directory = 'reset_data_total'
os.makedirs(output_directory, exist_ok=True)

for i in range(0, len(sorted_data), 100):
    out_file = os.path.join(output_directory, f"reset_data_total_{i // 100}.csv")
    with open(out_file, "w", newline='', encoding="utf-8") as file:
        w = csv.writer(file)
        w.writerow(data[0])
        w.writerows(sorted_data[i:i + 100])
