#### ----------------- Input -----------------

# input is currently commented out, when required put it back in
age = 18 # int(input("What is your age? "))

if age >= 18:
    print("adult")

elif age < 18 and age >=16:
    print("teenager allowed to drink beer")

elif age < 16 and age >=13:
    print("teenager not allowed to drink beer")

else:
    print("child")


#### ----------------- LIST -----------------
list_students = ["Alice", "Bob", "Charly"]
student_count = len(list_students)

print("Student count: " + str(student_count))

print("---")


#### ----------------- WHILE -----------------
print("")
print("----------")
print("WHILE LOOP")
print("----------")

# runner variable, required to iterate through the lisrt
i= 0
while i<student_count:
    print("iteration no. " + str(i))
    print("Student is " + str(list_students[i]))
    i+=1

#### ----------------- FOR -----------------
print("")
print("--------")
print("FOR LOOP")
print("--------")

for x in list_students:
    print("Student is " + str(x))

#### ----------------- Dictionary -----------------
# store name as key
# store age as value
student_dict = {"Thomas":12, "Katherina":14, "Sophie":17}

print("")
print("----------")
print("Dictionary")
print("----------")
# print("Age of Thomas: " + str(student_dict.get("Thomas")))
# print("Age of Katherina: " + str(student_dict["Katherina"]))

# key -> name
# value -> age
for key, value in student_dict.items():
    print("Age of {}: ".format(key) + str(value))