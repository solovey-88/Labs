import sys
import json
import csv

try:
    json_name = sys.argv[1]
except:
    json_name = input("Введите название файла, например file.json: ")

with open(json_name, "r", encoding="utf-8") as json_file:
    json_data = json.load(json_file)

csv_name = list(json_data.keys())[0] + ".csv"
data = list(json_data.values())[0]
headers = data[0].keys()

with open(csv_name, "w", encoding="utf-8", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(headers)
    for row in data:
        csv_writer.writerow(row.values())

print(f"Конвертация, {json_name}, в, {csv_name}, прошла успешно!")
