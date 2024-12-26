import csv

# Create a csv file with contents
data = [
    ["ram", "shrestha", 24, "single"],
    ["sita", "yadav", 27, "married"],
    ["hari", "gurung", 14, "single"],
    ["shyam", "shrestha", 25, "single"],
]
with open("data.csv", "w") as data_csv:
    writer = csv.writer(data_csv)
    writer.writerows(data)

# Create a csv file with dictonary content
users = [
    {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
    {
        "name": "Lio Nelson",
        "username": "lion",
        "department": "User Experience Research",
    },
    {"name": "Charlie Grey", "username": "greyc", "department": "Development"},
]

keys = users[0].keys()

with open("dict_data.csv", "w") as dict_data:
    writer = csv.DictWriter(dict_data, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)


# Read content from csv file
with open("dict_data.csv", "r") as dict_data:
    reader = csv.DictReader(dict_data)
    for row in reader:
        print(row)