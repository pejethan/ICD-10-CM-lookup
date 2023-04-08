import csv

with open('icd10cm.txt', 'r') as f:
    tabreader = csv.reader(f, delimiter='\t')
    icd10cm_data = list(tabreader)

search = input("Please enter a search string: ")

matching_results = []
for row in icd10cm_data:
    code = row[0]
    description = row[1]
    if search.lower() in code.lower() or search.lower() in description.lower():
        matching_results.append((code, description))

if matching_results:
    for code, description in matching_results:
        print(f"{code} - {description}")
else:
    print("No matching codes or descriptions found.")