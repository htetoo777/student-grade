name = input("Enter student's name: ")

mark1 = float(input("Enter mark for subject 1: "))
mark2 = float(input("Enter mark for subject 2: "))

average = (mark1 + mark2) / 2

print("Student Name:", name)
print("Average Mark:", average)

if average >= 50:
    print("Result: Passed")
else:
    print("Result: Failed")
