import csv
import os
import random


def load_csv_file(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            data.append(row)
    return data


def show(data, display_type='top', num_rows=5, separator=','):
    if display_type == 'bottom':
        data = data[-num_rows:]
    elif display_type == 'random':
        if num_rows > len(data):
            num_rows = len(data)
        data = random.sample(data, num_rows)

    for row in data:
        print(separator.join(row))


def info(data):
    num_rows = len(data) - 1
    num_cols = len(data[0])
    print(f"Количество строк с данными: {num_rows}")
    print(f"Количество колонок в таблице: {num_cols}")

    header = data[0]
    for col_index, col_name in enumerate(header):
        non_empty_count = sum(1 for row in data[1:] if row[col_index] != '')
        col_type = type(data[1][col_index]).__name__
        print(f"{col_name:10} {non_empty_count:5} {col_type}")


def del_nan(data):
    data = [row for row in data if all(field != '' for field in row)]
    return data


def make_ds(data):
    random.shuffle(data)
    split_index = int(0.7 * len(data))
    learning_data = data[:split_index]
    testing_data = data[split_index:]

    base_dir = os.path.dirname(os.path.abspath(__file__))
    work_dir = os.path.join(base_dir, 'workdata')
    learning_dir = os.path.join(work_dir, 'Learning')
    testing_dir = os.path.join(work_dir, 'Testing')

    os.makedirs(learning_dir, exist_ok=True)
    os.makedirs(testing_dir, exist_ok=True)

    learning_file = os.path.join(learning_dir, 'train.csv')
    testing_file = os.path.join(testing_dir, 'test.csv')

    write_csv_file(learning_file, learning_data)
    write_csv_file(testing_file, testing_data)


def write_csv_file(file_path, data):
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)


file_path = 'data.csv'

data = load_csv_file(file_path)

show(data, display_type='top', num_rows=5, separator=',')
print()

info(data)
print()

data = del_nan(data)

make_ds(data)