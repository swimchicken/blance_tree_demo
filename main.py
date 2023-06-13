import os
import csv

# 讀取檔案
with open("DB_students_tc_utf8.csv", "r") as file:
    reader = csv.reader(file)
    data = list(reader)

'''
header = data[0]
data = data[1:]
'''

sorted_data = sorted(data[1:], key=lambda x: int(x[0][1:]))  # 透過學生id去掉最一開始的D,且將後面的數字轉換int並排序

# print(sorted_data)


# 建立輸出檔案
output_d = 'reset_data_total'
os.makedirs(output_d, exist_ok=True)

# 切割輸出資料,每100筆
for i in range(0, len(sorted_data), 100):
    out_file = os.path.join(output_d, f"reset_data_total_{i // 100}.csv")
    with open(out_file, "w", newline='') as file:
        w = csv.writer(file)
        w.writerow(data[0])
        w.writerows(sorted_data[i:i + 100])
