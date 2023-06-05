import csv

# Read Departments data
departments = {}
with open('Departments.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        departments[row['ID']] = row['NAME']

# Read Employees data
employees = {}
with open('Employees.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        employees[row['ID']] = row['DEPT ID']

# Read Salaries data
salaries = {}
with open('Salaries.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        emp_id = row['EMP_ID']
        if emp_id not in salaries:
            salaries[emp_id] = []
        salaries[emp_id].append(float(row['AMT (USD)']))

# Calculate average monthly salary for each department
department_salaries = {}
for emp_id, dept_id in employees.items():
    if emp_id in salaries:
        if dept_id not in department_salaries:
            department_salaries[dept_id] = []
        department_salaries[dept_id].extend(salaries[emp_id])

# Calculate average monthly salary for each department
avg_salaries = {}
for dept_id, emp_salaries in department_salaries.items():
    avg_salaries[dept_id] = sum(emp_salaries) / len(emp_salaries)

# Sort departments by average salary in descending order
sorted_departments = sorted(avg_salaries.items(), key=lambda x: x[1], reverse=True)

# Generate the report
print("DEPT_NAME")
print("AVG_MONTHLY_SALARY (USD)")
for dept_id, avg_salary in sorted_departments[:3]:
    dept_name = departments[dept_id]
    print(dept_name)
    print(avg_salary)
    print()
