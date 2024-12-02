#Q.1 Create a list of city names  add 8 elements in it and perform CRUD operation on it
cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Pune", "Hyderabad", "Ahmedabad"]
print("List of cities:", cities)

cities[4] = "Lucknow"
print("Updated list of cities:", cities)

cities.append("Jaipur")
print("List of cities after adding a new city:", cities)

cities.remove("Ahmedabad")
print("List of cities after removing a city:", cities)

print("The third city in the list is:", cities[2])

#Q.2 Create a mixed list and change the value of third index to another data type value
mixed_list = [10, "Hello", 3.14, True, [1, 2, 3], {"name": "John"}, None]

print("Original mixed list:", mixed_list)

mixed_list[3] = "Changed to a string"

print("Updated mixed list:", mixed_list)

#Q.3 Create a list of Countries name , reverse the list and print only middle elements from the list
countries = ["USA", "Canada", "Germany", "France", "Japan", "India", "Brazil", "Australia"]

countries.reverse()

print("Reversed list of countries:", countries)

length = len(countries)
if length % 2 == 0:

    middle_elements = countries[length // 2 - 1:length // 2 + 1]
else:
    middle_elements = countries[length // 2]

print("Middle element(s) from the list:", middle_elements)

#Q.4 Create a list of pin-codes , delete the last pincode and the user required pincode from the list
pin_codes = ["110001", "400001", "600001", "500001", "700001", "800001"]

print("Original list of pin codes:", pin_codes)

pin_codes.pop()
print("List after deleting the last pin code:", pin_codes)

user_pin_code = input("Enter the pin code you want to delete: ")

if user_pin_code in pin_codes:
    pin_codes.remove(user_pin_code)
    print(f"Deleted pin code: {user_pin_code}")
else:
    print(f"Pin code {user_pin_code} not found in the list.")

print("Updated list of pin codes:", pin_codes)

#Q.5 Create a list of studentsName and perform all the pre-defined method and operation on it
students = ["Afrin", "seema", "riya", "mohinee", "anchal"]
print("Original List:", students)
students.append("Frank")
print("\nAfter Append:", students)
students.insert(2, "maha")
print("After Insert:", students)
students.remove("anchal")
print("After Remove:", students)
last_student = students.pop()
print(f"After Pop (Removed '{last_student}'):", students)
index_of_riya = students.index("riya")
print(f"Index of 'riya': {index_of_riya}")
count_of_riya = students.count("riya")
print(f"Count of 'riya': {count_of_riya}")
students.sort()
print("After Sort:", students)
students.reverse()
print("After Reverse:", students)
students.clear()
print("After Clear:", students)


