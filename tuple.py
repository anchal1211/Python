#Q.1 Write a Python program to find the number of times 4 appears in the tuple.
tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7 )
count_4 = tuplex.count(4)
print(f"The number 4 appears {count_4} times in the tuple.")


#Q.2 Write a Python program to convert a list to a tuple.
listx = [5, 10, 7, 4, 15, 3]
tuplex = tuple(listx)
print("The converted tuple is:", tuplex)


#Q.3 Write a Python program to calculate the sum of the numbers in a given tuple.
tuples_list = [(1, 2), (3, 4), (5, 6)]
total_sum = sum(sum(tup) for tup in tuples_list)
print("The sum of the numbers in the tuple list is:", total_sum)


#Q.4 Write a python program and iterate the given tuples
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)

employees = [employee1, employee2, employee3]

for employee in employees:
    name, emp_id, department, salary = employee
    print(f"Name: {name}, Employee ID: {emp_id}, Department: {department}, Salary: ${salary}")
