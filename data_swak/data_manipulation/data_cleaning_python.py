import csv

with open('../../data_repo/data.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = list(reader)


def replace_missing_values(data, column, value):
    for row in data:
        if row[column] == '':
            row[column] = value
    return data


present_ages = [int(row['Age']) for row in data if row['Age'] != '']
mean_age = sum(present_ages) / len(present_ages)
data = replace_missing_values(data, 'Age', mean_age)


def remove_duplicates(data, column):
    seen = set()
    new_data = []
    for row in data:
        if row[column] not in seen:
            new_data.append(row)
            seen.add(row[column])
    return new_data


data = remove_duplicates(data, 'Name')

with open('../../data_repo/data_cleaned.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    for row in data:
        writer.writerow(row)
